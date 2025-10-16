# Test Examples

This directory contains example files for testing the AI Code Validator.

## Files

### `bad_example.py`
Python file with **multiple issues** that the validator should catch:
- Hallucinated package import (`ai_utils_helper`)
- Hardcoded API key
- SQL injection vulnerabilities
- Missing input validation
- Outdated Python 2 patterns
- Command injection risk
- Dangerous `eval()` usage
- Hallucinated method call

### `good_example.py`
Python file with **no issues** - demonstrates best practices:
- Proper input validation
- Parameterized SQL queries
- Environment variables for secrets
- Type hints
- Error handling

### `bad_example.js`
JavaScript file with **multiple issues**:
- Hallucinated npm package
- Deprecated React lifecycle methods
- XSS vulnerabilities
- Hardcoded API key
- SQL injection patterns
- Command injection risk

## Running Tests

Test the validator on these files:

```bash
# Should find many issues (low score)
aivalidate check tests/test_examples/bad_example.py

# Should pass with high score
aivalidate check tests/test_examples/good_example.py

# Check all examples
aivalidate check tests/test_examples/
```

## Expected Results

### bad_example.py
- **Score**: ~30-40/100 (POOR/CRITICAL)
- **Issues**: 8-10 issues
- **Critical**: 3-4 (hallucinated dependency, SQL injection, hardcoded secrets)
- **High**: 2-3 (missing validation, command injection)

### good_example.py
- **Score**: 95-100/100 (EXCELLENT)
- **Issues**: 0-1 issues
- **Critical**: 0

### bad_example.js
- **Score**: ~35-45/100 (POOR)
- **Issues**: 7-9 issues
- **Critical**: 2-3
- **High/Medium**: 4-6
