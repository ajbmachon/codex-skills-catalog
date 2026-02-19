# Security Protocols (Normalized)

## Baseline
- Validate untrusted inputs.
- Avoid secret leakage in code, logs, and docs.
- Use least privilege for tools and runtime access.
- Fail explicitly; do not hide critical security errors.

## Review Checklist
- Injection risks (query, command, template, path)
- Authz/authn correctness
- Secret handling and storage
- Dangerous fallbacks and bypasses
- Logging with sensitive data redaction
