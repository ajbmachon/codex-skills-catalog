# Attack Intents: Advanced/Agentic

Advanced agentic and supply chain attacks
Total entries: 4

## Table of Contents

1. [Privilege Escalation via Agent Graphs](#privilege-escalation-via-agent-graphs)
2. [Scope Violation Data Exfiltration (Cross-Domain Leakage)](#scope-violation-data-exfiltration-cross-domain-leakage)
3. [Supply Chain Compromise (Tools / Agents / Registries)](#supply-chain-compromise-tools-agents-registries)
4. [Test Bias](#test-bias)

---

<a id="privilege-escalation-via-agent-graphs"></a>

<!-- Source: privilege_escalation_via_agent_graphs.md -->

# Privilege Escalation via Agent Graphs

## Description
Goal: leverage multi-agent architectures to obtain higher privileges, typically by:
- inducing agent-to-agent delegation
- exploiting default grouping/team scopes
- routing tasks to agents with broader access

## Defensive notes
- agent ACLs, supervised execution for privileged agents
- disable broad discovery by default
- isolate duties and scope per agent


---


---

<a id="scope-violation-data-exfiltration-cross-domain-leakage"></a>

<!-- Source: scope_violation_data_exfiltration.md -->

# Scope Violation Data Exfiltration (Cross-Domain Leakage)

## Description
Goal: exfiltrate sensitive data by causing the system to cross intended boundaries:
- external content influences internal data access
- internal corp data leaks into external channels
- summaries/outputs embed external references

## Defensive notes
- prompt partitioning, provenance-based access control
- strict scoping of which origins/resources can be accessed per task
- outbound content controls (safe rendering, link/image policies)
- monitoring for anomalous cross-domain access


---


---

<a id="supply-chain-compromise-tools-agents-registries"></a>

<!-- Source: supply_chain_compromise_tools_agents.md -->

# Supply Chain Compromise (Tools / Agents / Registries)

## Description
Attacks aimed at compromising the assistant’s ecosystem rather than directly
persuading the model, including:
- malicious tools, plugins, MCP servers
- compromised registries or update channels
- trojanized agent templates or agent catalogs

## Typical impacts
- silent policy override
- unauthorized actions (tool calls)
- stealthy data exfiltration
- long-lived persistence via updates

## Attack surfaces
- tool registries, MCP servers, plugin stores
- CI/CD pipelines for tool deployment
- agent marketplaces / shared prompts / templates

## Defensive notes
- allowlist + signing + pinning
- monitoring and diff-based change control
- separation of duties: install/update vs runtime execution
- least privilege for tool credentials and scopes


---


---

<a id="test-bias"></a>

<!-- Source: test_bias.md -->

# Test Bias

## Protected Class
### Description
Testing for biases related to protected classes and attributes

## Attack Examples
- Probing responses about different ethnic groups
- Testing gender-based response variations
- Exploring age-related biases in responses
- Testing religious bias in content generation
- Probing socioeconomic status assumptions
- Testing geographical and cultural biases
- Exploring disability-related response patterns
- Testing language and accent biases

### Examples

### Attacks


---


---
