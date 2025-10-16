# Makefile for AI Code Validator

.PHONY: help install install-dev test test-cov lint format clean build publish

help:  ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-20s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install:  ## Install package
	pip install -e .

install-dev:  ## Install package with development dependencies
	pip install -e .
	pip install -r requirements-dev.txt
	pre-commit install

test:  ## Run tests
	pytest -v

test-cov:  ## Run tests with coverage
	pytest --cov=ai_code_validator --cov-report=html --cov-report=term

test-examples:  ## Test on example files
	@echo "Testing bad example (should find issues):"
	aivalidate check tests/test_examples/bad_example.py --no-deps || true
	@echo "\nTesting good example (should pass):"
	aivalidate check tests/test_examples/good_example.py --no-deps

lint:  ## Run linters
	flake8 ai_code_validator tests --max-line-length=100
	black --check ai_code_validator tests
	isort --check-only ai_code_validator tests

format:  ## Format code with black and isort
	black ai_code_validator tests
	isort ai_code_validator tests

clean:  ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .mypy_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete

build:  ## Build distribution packages
	python -m build

publish-test:  ## Publish to TestPyPI
	twine upload --repository testpypi dist/*

publish:  ## Publish to PyPI
	twine upload dist/*

check:  ## Run all checks (lint + test)
	make lint
	make test

pre-commit:  ## Run pre-commit hooks on all files
	pre-commit run --all-files

security:  ## Run security checks
	bandit -r ai_code_validator
	safety check

validate:  ## Validate project (check + security)
	make check
	make security

init:  ## Initialize development environment
	make install-dev
	pre-commit install
	@echo "Development environment ready!"

ci:  ## Run CI checks locally
	make lint
	make test-cov
	make test-examples
