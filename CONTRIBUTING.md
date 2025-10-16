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

3. **Install development dependencies and setup**
   ```bash
   # Quick setup
   make init

   # Or manually:
   pip install -r requirements-dev.txt
   pip install -e .
   pre-commit install
   ```

4. **Make your changes**
   - Create a new branch: `git checkout -b feature-name`
   - Make your changes
   - Write tests for new functionality
   - Run tests and linters locally

5. **Run tests locally**
   ```bash
   # Run all tests
   make test
   # or: pytest

   # Run with coverage
   make test-cov
   # or: pytest --cov=ai_code_validator --cov-report=html

   # Run specific test file
   pytest tests/test_analyzer.py

   # Run specific test function
   pytest tests/test_analyzer.py::TestCodeAnalyzer::test_analyze_python_file
   ```

6. **Ensure code quality**
   ```bash
   # Run all quality checks
   make check

   # Run linters
   make lint

   # Format code
   make format

   # Run pre-commit hooks
   make pre-commit
   ```

## Code Style & Standards

- **Formatting**: Use `black` with 100 character line length
- **Import Sorting**: Use `isort` with black-compatible profile
- **Linting**: Pass `flake8` checks
- **Type Hints**: Use type hints for function signatures
- **Docstrings**: Add docstrings to all public functions and classes
- **Tests**: Maintain 70%+ code coverage

## Writing Tests

All new features must include tests. We use pytest for testing.

### Test Structure

```python
"""
Unit tests for [module name].
"""

import pytest
from ai_code_validator.your_module import YourClass


class TestYourClass:
    """Test cases for YourClass."""

    def test_initialization(self):
        """Test class initialization."""
        instance = YourClass()
        assert instance is not None

    def test_your_feature(self):
        """Test specific feature."""
        # Arrange
        instance = YourClass()
        input_data = "test data"

        # Act
        result = instance.your_method(input_data)

        # Assert
        assert result == expected_value
```

### Testing Guidelines

1. **One test per functionality**: Each test should verify one specific behavior
2. **Arrange-Act-Assert**: Structure tests clearly
3. **Descriptive names**: Test names should describe what they test
4. **Use fixtures**: Share common test data via pytest fixtures (see `tests/conftest.py`)
5. **Test edge cases**: Include tests for empty inputs, large inputs, invalid inputs
6. **Mock external calls**: Use `unittest.mock` for network requests

### Running Specific Tests

```bash
# Run tests for a specific module
pytest tests/test_analyzer.py -v

# Run tests matching a pattern
pytest -k "test_sql" -v

# Run tests and stop at first failure
pytest -x

# Run tests with detailed output
pytest -vv
```

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
