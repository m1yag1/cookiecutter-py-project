# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}

## Installation

This project uses [uv](https://github.com/astral-sh/uv) for package management.

```bash
# Clone the repository
git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.git
cd {{cookiecutter.project_slug}}

# Install dependencies
uv sync

# Install in development mode
uv pip install -e .
```

## Development

### Setup

1. Install development dependencies:
   ```bash
   uv sync --group dev
   ```

2. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

### Running Tests

```bash
# Run tests
tox

# Run tests with coverage
tox -e coverage

# Run specific test environment
tox -e py{{cookiecutter.python_version.replace('.', '')}}
```

### Code Quality

```bash
# Format and lint code
tox -e fix

# Type checking
tox -e mypy

# Run all pre-commit hooks
pre-commit run --all-files
```

{%- if cookiecutter.use_cli == 'yes' %}

## Usage

After installation, you can use the CLI:

```bash
{{cookiecutter.project_slug}} --help
```
{%- endif %}

## Project Structure

```
{{cookiecutter.project_slug}}/
├── src/
│   └── {{cookiecutter.project_slug}}/
│       ├── __init__.py
{%- if cookiecutter.use_cli == 'yes' %}
│       ├── cli.py
{%- endif %}
│       └── ...
├── tests/
│   ├── unit/
│   └── integration/
├── docs/
├── pyproject.toml
├── tox.ini
├── README.md
└── ...
```

{%- if cookiecutter.publish_to_pypi == 'yes' %}

## Publishing

### To PyPI

This project is set up for automated publishing to PyPI via GitHub Actions:

1. Update the version in `pyproject.toml`
2. Create and push a git tag:
   ```bash
   git tag v0.1.0
   git push origin v0.1.0
   ```
3. The GitHub Actions workflow will automatically:
   - Build the package
   - Create a GitHub release
   - Publish to PyPI

### Manual Publishing

You can also publish manually using `uv`:

```bash
# Build the package
uv build

# Publish to PyPI (requires PYPI_API_TOKEN)
uv publish
```
{%- endif %}

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and ensure they pass (`tox`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## License

{%- if cookiecutter.open_source_license != "Not open source" %}
This project is licensed under the {{cookiecutter.open_source_license}} License - see the LICENSE file for details.
{%- else %}
This project is proprietary and confidential.
{%- endif %}

## Author

- {{cookiecutter.full_name}} - {{cookiecutter.email}}
