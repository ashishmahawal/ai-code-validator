# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Comprehensive unit test suite with pytest
- Code coverage reporting (target: 70%+)
- Pre-commit hooks for code quality
- Enhanced CI/CD pipeline with security checks
- Pull request template
- Issue templates (bug report, feature request)
- PR checks workflow for branch protection
- CODEOWNERS file
- SECURITY.md file
- CHANGELOG.md file

### Changed
- Updated CI workflow to include pytest and coverage
- Improved code quality checks in CI/CD

## [0.1.0] - 2025-10-16

### Added
- Initial release of AI Code Validator
- Core code analyzer for Python, JavaScript, TypeScript, Java, Kotlin
- Dependency checker to validate packages on PyPI and npm
- Security scanner for SQL injection, XSS, command injection, hardcoded secrets
- Confidence scoring system (0-100 scale)
- Beautiful colored CLI output with severity levels
- Git pre-commit hook support
- JSON output format for CI/CD integration
- Support for multiple severity levels (critical, high, medium, low)
- Examples and test files demonstrating tool capabilities

### Features
- Detects hallucinated functions and APIs
- Validates imported dependencies actually exist
- Scans for missing input validation
- Identifies outdated coding patterns
- Checks for hardcoded secrets
- Provides actionable suggestions for fixes

### Documentation
- Comprehensive README with examples
- Contributing guidelines
- MIT License
- Promotion guide for social media
- Installation and usage instructions

[Unreleased]: https://github.com/ashishmahawal/ai-code-validator/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/ashishmahawal/ai-code-validator/releases/tag/v0.1.0
