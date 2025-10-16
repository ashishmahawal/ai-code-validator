# Security Policy

## Supported Versions

We release patches for security vulnerabilities. Currently supported versions:

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Reporting a Vulnerability

The AI Code Validator team takes security bugs seriously. We appreciate your efforts to responsibly disclose your findings.

### How to Report

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them via one of the following methods:

1. **GitHub Security Advisories** (Preferred)
   - Go to https://github.com/ashishmahawal/ai-code-validator/security/advisories
   - Click "New draft security advisory"
   - Fill in the details

2. **Email**
   - Send an email to: [Your security email - replace this]
   - Include as much information as possible (see below)

### What to Include

To help us better understand and resolve the issue, please include:

- Type of issue (e.g., buffer overflow, SQL injection, cross-site scripting, etc.)
- Full paths of source file(s) related to the issue
- Location of the affected source code (tag/branch/commit or direct URL)
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the issue, including how an attacker might exploit it

### What to Expect

- **Acknowledgment**: We'll acknowledge your email within 48 hours
- **Updates**: We'll send you regular updates about our progress (at least every 5 business days)
- **Disclosure**: Once the issue is resolved, we'll publicly disclose the vulnerability (with credit to you, if desired)
- **Timeline**: We aim to resolve critical issues within 90 days

### Safe Harbor

We support safe harbor for security researchers who:

- Make a good faith effort to avoid privacy violations, destruction of data, and interruption or degradation of our service
- Only interact with accounts you own or with explicit permission of the account holder
- Do not exploit a security issue for any reason (this includes demonstrating additional risk)
- Report the vulnerability promptly
- Keep vulnerability details private until we've addressed it

We will:

- Work with you to understand and resolve the issue quickly
- Acknowledge your contribution (if desired)
- Not pursue legal action against researchers who follow this policy

## Security Best Practices

When using AI Code Validator:

### For Users

1. **Keep Updated**: Always use the latest version
2. **Review Results**: Don't blindly trust all findings - review and validate
3. **Secure Config**: Don't include secrets in `.aivalidate.yml` config files
4. **CI/CD**: Use `--format json` in automated pipelines
5. **Dependencies**: Regularly update dependencies

### For Contributors

1. **Input Validation**: Always validate user inputs
2. **No Secrets**: Never commit API keys, tokens, or credentials
3. **Dependencies**: Keep dependencies minimal and audited
4. **Code Review**: All PRs require review before merging
5. **Tests**: Write tests that include security scenarios

## Known Security Considerations

### Network Requests

AI Code Validator makes network requests to:
- PyPI (https://pypi.org) - to validate Python packages
- npm Registry (https://registry.npmjs.org) - to validate npm packages

These requests:
- Use HTTPS only
- Have 3-second timeouts
- Fail safely (assume package exists on error)
- Don't send any user data

### File System Access

The tool:
- Reads source code files provided by the user
- Writes git hooks only when explicitly requested
- Never modifies source files without explicit permission
- Respects `.gitignore` patterns

### Privacy

We:
- Don't collect any usage analytics
- Don't send code to external services
- Don't store or cache code contents
- Only analyze files you explicitly provide

## Vulnerability Disclosure Policy

When we receive a security bug report, we will:

1. Confirm the problem and determine affected versions
2. Audit code to find similar problems
3. Prepare fixes for all supported versions
4. Release new versions as soon as possible
5. Publicly announce the vulnerability

## Security Hall of Fame

We'd like to thank the following researchers for responsibly disclosing security issues:

<!-- This section will be populated as security researchers contribute -->

*No security issues have been reported yet.*

---

Thank you for helping keep AI Code Validator and its users safe!

**Last Updated**: 2025-10-16
