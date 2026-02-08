/**
 * Judge Provider
 * Runs model-based grading using the OpenAI Responses API when configured.
 */

export type JudgeLevel = 'fast' | 'standard' | 'smart';

export interface JudgeRequest {
  systemPrompt: string;
  userPrompt: string;
  level?: JudgeLevel;
  model?: string;
  timeoutMs?: number;
}

export interface JudgeResponse {
  success: boolean;
  output: string;
  model: string;
  error?: string;
}

function resolveModel(request: JudgeRequest): string {
  if (request.model) return request.model;

  const byLevel: Record<JudgeLevel, string> = {
    fast: process.env.EVALS_MODEL_FAST || 'gpt-5-mini',
    standard: process.env.EVALS_MODEL_STANDARD || 'gpt-5',
    smart: process.env.EVALS_MODEL_SMART || 'gpt-5',
  };

  return byLevel[request.level || 'standard'];
}

function extractOutputText(payload: any): string {
  if (typeof payload?.output_text === 'string' && payload.output_text.length > 0) {
    return payload.output_text;
  }

  const output = payload?.output;
  if (!Array.isArray(output)) return '';

  const chunks: string[] = [];
  for (const item of output) {
    if (!Array.isArray(item?.content)) continue;
    for (const block of item.content) {
      if (typeof block?.text === 'string') chunks.push(block.text);
      if (typeof block?.output_text === 'string') chunks.push(block.output_text);
    }
  }

  return chunks.join('\n').trim();
}

export async function runJudge(request: JudgeRequest): Promise<JudgeResponse> {
  const apiKey = process.env.OPENAI_API_KEY;
  if (!apiKey) {
    return {
      success: false,
      output: '',
      model: resolveModel(request),
      error: 'OPENAI_API_KEY is not set. Model-based graders require an API key.',
    };
  }

  const baseUrl = (process.env.OPENAI_BASE_URL || 'https://api.openai.com/v1').replace(/\/$/, '');
  const model = resolveModel(request);
  const timeoutMs = request.timeoutMs ?? 30000;
  const effort: 'low' | 'medium' | 'high' =
    request.level === 'smart' ? 'high' : request.level === 'fast' ? 'low' : 'medium';

  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), timeoutMs);

  try {
    const response = await fetch(`${baseUrl}/responses`, {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${apiKey}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model,
        input: [
          { role: 'system', content: [{ type: 'input_text', text: request.systemPrompt }] },
          { role: 'user', content: [{ type: 'input_text', text: request.userPrompt }] },
        ],
        reasoning: { effort },
      }),
      signal: controller.signal,
    });

    const payload = await response.json().catch(() => ({}));
    if (!response.ok) {
      return {
        success: false,
        output: '',
        model,
        error: `Judge request failed (${response.status}): ${JSON.stringify(payload)}`,
      };
    }

    const text = extractOutputText(payload);
    if (!text) {
      return {
        success: false,
        output: '',
        model,
        error: 'Judge response did not contain text output.',
      };
    }

    return {
      success: true,
      output: text,
      model: payload?.model || model,
    };
  } catch (error) {
    return {
      success: false,
      output: '',
      model,
      error: `Judge request error: ${String(error)}`,
    };
  } finally {
    clearTimeout(timeoutId);
  }
}
