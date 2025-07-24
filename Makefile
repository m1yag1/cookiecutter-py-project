.PHONY: help install dev test lint format clean template-test

help:  ## Show this help message
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install:  ## Install the package
	uv sync

dev:  ## Install development dependencies
	uv sync --group dev
	pre-commit install

test:  ## Run tests
	tox


lint:  ## Run linting
	ruff check hooks tests

format:  ## Format code
	ruff check --fix hooks tests
	ruff format hooks tests

clean:  ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache/
	rm -rf .tox/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

template-test:  ## Test template generation with cookiecutter
	cookiecutter . --no-input --overwrite-if-exists
