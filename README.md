# Cookiecutter Python Project

A modern Python project template using cookiecutter, designed for professional Python development with opinionated defaults and best practices.

## Features

- **Modern Python packaging** with `pyproject.toml` and `uv`
- **src layout** for better package management
- **Pre-configured tools**:
  - `ruff` for linting and formatting
  - `mypy` for type checking
  - `pytest` for testing
  - `tox` for test automation
  - `pre-commit` hooks
- **GitHub Actions** workflows for CI/CD
- **Optional CLI** support with Click and Rich
- **Comprehensive project structure** with tests, docs, and more

## Requirements

- Python 3.11+
- [cookiecutter](https://cookiecutter.readthedocs.io/) (`pip install cookiecutter` or `uv tool install cookiecutter`)
- [uv](https://github.com/astral-sh/uv) (recommended for the generated project)

## Usage

### Interactive Mode

Generate a new project with prompts:

```bash
cookiecutter https://github.com/m1yag1/cookiecutter-py-project.git
```

### Non-Interactive Mode (AI Agent Friendly)

Generate a project without prompts by specifying all options:

```bash
# Basic Python project
cookiecutter https://github.com/m1yag1/cookiecutter-py-project.git \
  --no-input \
  project_name="my-awesome-project" \
  full_name="Your Name" \
  email="your.email@example.com" \
  github_username="yourusername"

# Python project with CLI and PyPI publishing
cookiecutter https://github.com/m1yag1/cookiecutter-py-project.git \
  --no-input \
  project_name="my-cli-tool" \
  use_cli="yes" \
  publish_to_pypi="yes" \
  full_name="Your Name" \
  email="your.email@example.com" \
  github_username="yourusername" \
  project_short_description="A CLI tool for awesome things"
```

### Available Options

When using interactive mode, you'll be prompted for:

- `full_name`: Your name
- `email`: Your email address
- `github_username`: Your GitHub username
- `project_name`: Name of your project
- `project_slug`: Python package name (auto-generated)
- `project_short_description`: Brief project description
- `version`: Initial version (default: 0.1.0)
- `python_version`: Python version to target (default: 3.12)
- `line_length`: Maximum line length (default: 100)
- `use_cli`: Whether to include CLI boilerplate
- `use_claude`: Whether to include CLAUDE.md for AI development
- `publish_to_pypi`: Whether to include PyPI publishing setup with Test PyPI validation
- `open_source_license`: License choice

## Generated Project Structure

```
your_project/
├── src/
│   └── your_project/
│       ├── __init__.py
│       └── cli.py          # If CLI enabled
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── unit/
│   └── integration/
├── docs/
├── .github/
│   └── workflows/
│       ├── tests.yml
│       └── release.yml
├── .gitignore
├── .pre-commit-config.yaml
├── LICENSE
├── Makefile
├── README.md
├── pyproject.toml
└── tox.ini
```

## AI Agent Instructions

This template is designed to work seamlessly with AI coding assistants. When an AI agent needs to create a Python project, it should use the non-interactive mode:

**Example AI Agent Commands:**

For a basic Python project:
```bash
cookiecutter https://github.com/m1yag1/cookiecutter-py-project.git --no-input project_name="project-name" full_name="Developer Name" email="dev@example.com" github_username="devuser"
```

For a CLI tool with PyPI publishing:
```bash
cookiecutter https://github.com/m1yag1/cookiecutter-py-project.git --no-input project_name="my-cli-tool" use_cli="yes" publish_to_pypi="yes" full_name="Developer Name" email="dev@example.com" github_username="devuser"
```

For AI development with Claude Code:
```bash
cookiecutter https://github.com/m1yag1/cookiecutter-py-project.git --no-input project_name="my-ai-project" use_claude="yes" full_name="Developer Name" email="dev@example.com" github_username="devuser"
```

**Required Parameters for AI Agents:**
- `project_name` - The project name (will auto-generate project_slug)
- `full_name` - Developer's name
- `email` - Developer's email
- `github_username` - GitHub username

**Optional Parameters:**
- `use_cli="yes"` - Include CLI boilerplate with Click
- `use_claude="yes"` - Include CLAUDE.md file for AI development context
- `publish_to_pypi="yes"` - Include PyPI publishing setup with Test PyPI validation
- `python_version="3.11"` - Target Python version (default: 3.12)
- `open_source_license="MIT"` - License choice (default: MIT)

## Post-Generation

After generation, the template will:
1. Initialize a git repository
2. Create an initial commit
3. Provide next steps for setting up the development environment

## Development Workflow

In your generated project:

```bash
# Install development dependencies
uv sync --all-extras

# Install pre-commit hooks
pre-commit install

# Run tests
make test

# Format and lint code
make format

# Run type checking
make typecheck
```

## Development

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/m1yag1/cookiecutter-py-project.git
   cd cookiecutter-py-project
   ```

2. Install development dependencies:
   ```bash
   make dev
   ```

### Testing

This project uses comprehensive testing to ensure the cookiecutter template works correctly:

```bash
# Run all tests
make test

# Run tests with coverage
make coverage

# Test template generation manually
make template-test

# Run linting
make lint

# Format code
make format
```

### Test Structure

- `tests/test_project_generation.py`: Tests for cookiecutter template generation
- Uses `pytest-cookies` to test different cookiecutter configurations
- Tests cover all template options and generated project structure

### Making Changes

1. Make your changes to the template files
2. Run tests to ensure everything works: `make test`
3. Test the template manually: `make template-test`
4. Run linting and formatting: `make format`
5. Commit your changes

## License

This cookiecutter template is released under the MIT License.
