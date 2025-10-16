# Contributing to AI Code Validator

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing.

## Ways to Contribute

### 🐛 Report Bugs
- Use GitHub Issues to report bugs
- Include the file that triggered the issue
- Describe expected vs actual behavior
- Include your Python version and OS

### 💡 Suggest Features
- Open a GitHub Issue with the "enhancement" label
- Describe the use case and benefit
- Provide examples if possible

### 🔍 Add Detection Patterns
Help us detect more AI code issues:
- Add new hallucination patterns
- Improve security checks
- Support more languages

### 📖 Improve Documentation
- Fix typos or unclear instructions
- Add examples
- Improve the README

## Development Setup

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-code-validator.git
   cd ai-code-validator
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install in development mode**
   ```bash
   pip install -e .
   ```

4. **Make your changes**
   - Create a new branch: `git checkout -b feature-name`
   - Make your changes
   - Test thoroughly

5. **Test your changes**
   ```bash
   # Test on example files
   aivalidate check tests/test_examples/

   # Test specific functionality
   python -m ai_code_validator.cli check your_test_file.py
   ```

## Code Style

- Follow PEP 8 for Python code
- Use type hints where appropriate
- Add docstrings to functions and classes
- Keep functions focused and small

## Adding New Detection Patterns

### 1. Add to Analyzer (`analyzer.py`)
For code structure issues and hallucinations:
```python
def _check_your_pattern(self, content: str, filepath: str):
    """Check for specific pattern."""
    lines = content.split('\n')
    for i, line in enumerate(lines, 1):
        if 'pattern' in line:
            self.issues.append({
                'type': 'your_issue_type',
                'severity': 'high',  # critical, high, medium, low
                'message': 'Description of the issue',
                'file': filepath,
                'line': i,
                'suggestion': 'How to fix it'
            })
```

### 2. Add to Security Scanner (`security_scanner.py`)
For security vulnerabilities:
```python
def _check_your_vulnerability(self, content: str, filepath: str):
    """Check for specific vulnerability."""
    # Similar structure as above
```

### 3. Add to Dependency Checker (`dependency_checker.py`)
For package/import validation:
```python
def _check_your_package_manager(self, package: str) -> bool:
    """Check if package exists on registry."""
    # Return True if exists, False otherwise
```

### 4. Update Scoring (`scorer.py`)
If your issue type needs special weight:
```python
type_multipliers = {
    'your_issue_type': 1.5,  # Adjust weight
}
```

## Pull Request Process

1. **Update documentation** if needed
2. **Test thoroughly** on various file types
3. **Create a pull request** with:
   - Clear title describing the change
   - Description of what changed and why
   - Reference any related issues

4. **PR Checklist**:
   - [ ] Code follows style guidelines
   - [ ] Self-review completed
   - [ ] Comments added for complex code
   - [ ] Documentation updated
   - [ ] Tested on example files
   - [ ] No breaking changes (or documented)

## Questions?

Open an issue or discussion on GitHub. We're happy to help!

## Code of Conduct

Be respectful and constructive. We're all here to make better tools.
