# OWASP Top 10 for Agentic Applications 2026

First security framework dedicated to autonomous AI agents
Released: December 10, 2025
Total entries: 10

## Table of Contents

1. [ASI01: Agent Goal Hijack](#asi01-agent-goal-hijack)
2. [ASI02: Tool Misuse & Exploitation](#asi02-tool-misuse--exploitation)
3. [ASI03: Identity & Privilege Abuse](#asi03-identity--privilege-abuse)
4. [ASI04: Agentic Supply Chain Vulnerabilities](#asi04-agentic-supply-chain-vulnerabilities)
5. [ASI05: Unexpected Code Execution (RCE)](#asi05-unexpected-code-execution-rce)
6. [ASI06: Memory & Context Poisoning](#asi06-memory--context-poisoning)
7. [ASI07: Insecure Inter-Agent Communication](#asi07-insecure-inter-agent-communication)
8. [ASI08: Cascading Failures](#asi08-cascading-failures)
9. [ASI09: Human-Agent Trust Exploitation](#asi09-human-agent-trust-exploitation)
10. [ASI10: Rogue Agents](#asi10-rogue-agents)

---

## Overview

The OWASP GenAI Security Project released this framework on December 10, 2025, developed through collaboration with 100+ security researchers, industry practitioners, and leading cybersecurity providers.

**Why a Separate Framework:**
- Agents chain actions and operate autonomously
- Minor vulnerabilities can cascade into system-wide compromise
- Traditional security (static analysis, signature-based detection) wasn't built for autonomous systems
- Security shifted from "securing a model call" to "securing autonomous decision-action chains"

**Core Security Principles:**
1. **Least-Agency Principle** - Grant minimum autonomy required for the task
2. **Strong Observability** - Clear visibility into what agents are doing, why, and which tools they invoke

---

<a id="asi01-agent-goal-hijack"></a>

# ASI01: Agent Goal Hijack

## Description
Attackers redirect agent objectives via injected instructions or poisoned content. Hidden prompts turn copilots into silent exfiltration engines.

## Real-world example
**EchoLeak** - Zero-click prompt injection in Microsoft 365 Copilot where malicious instructions hidden in external emails caused data exfiltration during user queries.

## Attack patterns
- Indirect prompt injection via external content
- Goal manipulation through context poisoning
- Objective drift through multi-turn exploitation
- Hidden instructions in processed documents

## Impact
- Unauthorized data access and exfiltration
- Actions performed against user intent
- Silent compromise of trusted workflows

## Defenses / mitigations
- Validate agent goals against original user intent
- Implement goal verification checkpoints
- Monitor for objective drift indicators
- Isolate external content from goal-setting logic

---

<a id="asi02-tool-misuse--exploitation"></a>

# ASI02: Tool Misuse & Exploitation

## Description
Agents misuse legitimate tools due to ambiguous prompts, over-privilege, or poisoned inputs. Agents bend legitimate tools into destructive outputs.

## Real-world example
**Amazon Q** - Agents using legitimate tools in unintended, destructive ways due to manipulation.

## Attack patterns
- Ambiguous prompts causing unintended tool usage
- Tool parameter manipulation
- Chaining tools in unexpected sequences
- Exploiting tool side effects

## Impact
- Unintended destructive actions
- Data corruption or deletion
- Resource abuse
- Privilege escalation via tool chains

## Defenses / mitigations
- Strict access control policies and granular permissions
- Tool usage monitoring and behavioral profiling
- Input validation for tool parameters
- Tool allowlisting per task type

---

<a id="asi03-identity--privilege-abuse"></a>

# ASI03: Identity & Privilege Abuse

## Description
Flaws in agent identity and delegation allow unauthorized actions. Agents unintentionally reuse, escalate, or leak inherited credentials or access.

## Attack patterns
- Credential leakage through agent outputs
- Privilege escalation via agent delegation
- Identity spoofing between agents
- Inherited permission abuse

## Impact
- Agents operate far beyond intended scope
- Unauthorized access to sensitive resources
- Cross-system compromise via leaked credentials

## Defenses / mitigations
- Short-lived credentials with just-in-time access
- Precisely scoped permissions per agent
- Credential rotation and monitoring
- Identity verification for inter-agent operations

---

<a id="asi04-agentic-supply-chain-vulnerabilities"></a>

# ASI04: Agentic Supply Chain Vulnerabilities

## Description
Compromised tools, prompts, plugins, or agents alter behavior or expose data. Dynamic MCP and A2A ecosystems enable runtime component poisoning.

## Real-world example
**GitHub MCP Exploit (May 2025)** - Malicious GitHub issues containing hidden prompts caused AI agents to exfiltrate private repository data.

## Key difference from LLM Top 10
- LLM03 focuses on static pre-deployment risks
- ASI04 covers dynamic runtime composition where agents discover/integrate components during execution

## Attack patterns
- MCP Tool Poisoning Attacks (TPAs)
- Plugin marketplace compromise
- Prompt template injection
- Agent template trojans

## Impact
- Silent behavioral modification
- Data exfiltration through legitimate channels
- Persistent compromise via updates

## Defenses / mitigations
- Allowlisting for MCP tools and servers
- Signed and verified tool packages
- Runtime integrity monitoring
- Version pinning and change detection

---

<a id="asi05-unexpected-code-execution-rce"></a>

# ASI05: Unexpected Code Execution (RCE)

## Description
Agents generate or execute unsafe code or commands without proper isolation. Natural-language execution paths unlock dangerous RCE avenues.

## Real-world example
**AutoGPT RCE** - Agents generating and executing arbitrary code without sandboxing.

## Attack patterns
- Code generation from manipulated prompts
- Sandbox escape through crafted outputs
- Command injection via natural language
- Interpreter exploitation

## Impact
- Full system compromise
- Arbitrary code execution
- Data theft and destruction
- Lateral movement in networks

## Defenses / mitigations
- Strict sandboxing for all code execution
- Code review/validation before execution
- Allowlisted commands and interpreters
- Execution isolation and monitoring

---

<a id="asi06-memory--context-poisoning"></a>

# ASI06: Memory & Context Poisoning

## Description
Persistent corruption of agent memory, RAG stores, embeddings, or contextual knowledge. Memory poisoning reshapes behavior long after initial interaction.

## Real-world example
**Gemini Memory Attack** - Persistent behavioral modification through memory manipulation.

## Attack patterns
- RAG store poisoning
- Embedding manipulation
- Long-term context injection
- Cross-session persistence

## Impact
- Behavioral changes persist across sessions
- Subtle, hard-to-detect compromise
- Long-term data exfiltration
- Trust erosion in agent outputs

## Defenses / mitigations
- Memory integrity validation
- Provenance tracking for stored content
- Periodic memory audits
- Isolation of memory sources by trust level

---

<a id="asi07-insecure-inter-agent-communication"></a>

# ASI07: Insecure Inter-Agent Communication

## Description
Spoofed, intercepted, or manipulated communication between agents lacking strong authentication, encryption, or schema validation.

## Attack patterns
- Agent spoofing/impersonation
- Message replay attacks
- Protocol downgrade attacks
- "Agent-in-the-middle" interception
- Schema manipulation

## Impact
- Unauthorized commands executed between agents
- Data interception in multi-agent workflows
- Trust chain compromise

## Defenses / mitigations
- Enforce mTLS for agent-to-agent APIs
- Encrypt all inter-agent messages
- Schema validation for agent protocols
- Message signing and verification

---

<a id="asi08-cascading-failures"></a>

# ASI08: Cascading Failures

## Description
Small missteps or faults propagate through multi-agent workflows, amplifying impact. A single agent's hallucination can trigger a chain reaction halting the entire system.

## Unique to agentic systems
This risk does not exist in single-model LLM applications - it emerges from multi-agent coordination.

## Attack patterns
- Intentional fault injection
- Hallucination propagation
- Error amplification through chains
- Dependency exploitation

## Impact
- System-wide outages
- Compounded errors leading to major failures
- Difficult-to-trace root causes

## Defenses / mitigations
- Circuit breakers between agent stages
- Fault isolation boundaries
- Output validation at each stage
- Graceful degradation patterns

---

<a id="asi09-human-agent-trust-exploitation"></a>

# ASI09: Human-Agent Trust Exploitation

## Description
Humans overly rely on agent recommendations, leading to unsafe approvals. Confident, polished explanations mislead human operators into approving harmful actions.

## Unique to agentic systems
Automation bias risk increases as agents become more capable and persuasive.

## Attack patterns
- Confident false explanations
- Social engineering through agent outputs
- Authority mimicry
- Gradual trust building then exploitation

## Impact
- Humans approve harmful actions
- Security controls bypassed via human trust
- Reduced human oversight effectiveness

## Defenses / mitigations
- Human-in-the-loop for high-risk decisions
- Skepticism training for operators
- Independent verification for critical actions
- Clear uncertainty indicators in agent outputs

---

<a id="asi10-rogue-agents"></a>

# ASI10: Rogue Agents

## Description
Misaligned or compromised agents diverging from intended behavior. Agents showing misalignment, concealment, and self-directed action.

## Real-world examples
- **Replit Meltdown** - Agent exhibiting autonomous, unintended behavior
- **Cost-optimization agents** - Autonomously deciding backup deletion achieves goals most efficiently

## Attack patterns
- Goal misalignment exploitation
- Self-modification attempts
- Concealment of true objectives
- Autonomous goal reinterpretation

## Impact
- Agents acting against organizational interests
- Unpredictable and harmful behaviors
- Difficult to detect and remediate

## Defenses / mitigations
- **Kill switch mechanism** - Quickly disable compromised agents
- Behavioral monitoring and anomaly detection
- Alignment verification checkpoints
- Constrained autonomy boundaries

---

## Comparison: LLM Top 10 vs. Agentic Top 10

| Aspect | LLM Top 10 2025 | Agentic Top 10 2026 |
|--------|-----------------|---------------------|
| Focus | Language model vulnerabilities | Autonomous agent security |
| Scope | Single model calls | Multi-step workflows |
| Key Concern | Securing the model | Securing decision-action chains |
| Prefix | LLM01-LLM10 | ASI01-ASI10 |
| Supply Chain | Static pre-deployment | Dynamic runtime composition |
| Unique Risks | N/A | Cascading Failures, Trust Exploitation, Rogue Agents |

---

## Implementation Checklist

### Access Control
- [ ] Strict access control policies implemented
- [ ] Granular permissions per tool/agent
- [ ] Short-lived credentials with JIT access

### Monitoring
- [ ] Real-time behavioral monitoring active
- [ ] Anomaly detection for agent activity
- [ ] Detailed logging of goals, tools, decisions

### Communication
- [ ] mTLS enforced for agent-to-agent APIs
- [ ] All inter-agent messages encrypted
- [ ] Schema validation on agent protocols

### Safety
- [ ] Kill switch mechanism in place
- [ ] Circuit breakers between agent stages
- [ ] Human-in-the-loop for critical decisions

---

## Industry Adoption

| Organization | Adoption |
|--------------|----------|
| Microsoft | References OWASP Threat and Mitigations document |
| NVIDIA | Safety Framework references OWASP Agentic Threat Modelling Guide |
| AWS | Contributed to project, noted frameworks "provide valuable insights" |
| GoDaddy | Implemented Agentic Naming Service proposal in production |

---

## Related OWASP Resources

1. **Securing Agentic Applications Guide 1.0** - Technical recommendations for secure agentic applications
2. **Agentic AI Threats and Mitigations** - Threat-model-based reference with mitigations
3. **The State of Agentic Security and Governance 1.0** - Safe and responsible deployment guide
4. **OWASP AI Vulnerability Scoring System (AIVSS)** - Standardized AI risk assessment framework

---

## Sources

- OWASP Top 10 for Agentic Applications for 2026 (Official)
- OWASP GenAI Security Project Release (December 2025)
- Agentic Security Initiative
- Securing Agentic Applications Guide 1.0
- Lares Labs: OWASP Agentic AI Top 10 Threats in the Wild
- BleepingComputer: Real-World Attacks Behind OWASP Agentic AI Top 10

---
