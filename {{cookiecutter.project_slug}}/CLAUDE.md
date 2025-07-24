# CLAUDE.md - Project Context

## Project Overview
**{{ cookiecutter.project_name }}** - {{ cookiecutter.project_short_description }}

This project was generated using [cookiecutter-py-project](https://github.com/m1yag1/cookiecutter-py-project.git) with modern Python best practices.

## Project Structure
- **Language**: Python {{ cookiecutter.python_version }}+
- **Package Manager**: uv
- **Testing**: pytest with tox automation
- **Code Quality**: ruff (linting + formatting), mypy (type checking)
- **CI/CD**: GitHub Actions
{%- if cookiecutter.use_cli == "yes" %}
- **CLI**: Click-based command line interface in `src/{{ cookiecutter.project_slug }}/cli.py`
{%- endif %}
{%- if cookiecutter.publish_to_pypi == "yes" %}
- **Publishing**: PyPI publishing workflow configured
{%- endif %}

## Key Commands
{%- if cookiecutter.use_cli == "yes" %}

### CLI Usage
```bash
# Install in development mode
uv sync --all-extras

# Run the CLI
uv run python -m {{ cookiecutter.project_slug }} --help
```
{%- endif %}

### Development Commands
```bash
# Install dependencies and setup development environment
make install

# Run tests
make test

# Run tests with coverage
make coverage

# Format code
make format

# Run linting
make lint

# Run type checking
make typecheck

# Clean build artifacts
make clean
```

## Development Workflow
1. **Setup**: Run `make install` to install dependencies and pre-commit hooks
2. **Development**: Make changes to code in `src/{{ cookiecutter.project_slug }}/`
3. **Testing**: Add tests in `tests/` and run `make test`
4. **Quality**: Run `make format` and `make lint` before committing
5. **Commit**: Pre-commit hooks will run automatically

## Project Architecture
- **src/{{ cookiecutter.project_slug }}/**: Main package code
  - `__init__.py`: Package initialization
{%- if cookiecutter.use_cli == "yes" %}
  - `cli.py`: Command line interface
{%- endif %}
- **tests/**: Test suite
  - `unit/`: Unit tests
  - `integration/`: Integration tests
- **pyproject.toml**: Project configuration and dependencies
- **tox.ini**: Test automation configuration
- **Makefile**: Development commands

## Dependencies
The project uses dependency groups for organization:
- **dev**: Development tools (includes test + type groups, pre-commit, tox)
- **test**: Testing tools (pytest, coverage, ruff)
- **type**: Type checking tools (mypy)
{%- if cookiecutter.use_cli == "yes" %}
- **cli**: CLI dependencies (click, rich) - automatically included in main dependencies
{%- endif %}

## Testing Strategy
- Unit tests for individual functions/classes
- Integration tests for component interactions
- Pytest fixtures in `tests/conftest.py`
- Coverage reporting enabled
- Tests run on Python {{ cookiecutter.python_version }} via GitHub Actions

{%- if cookiecutter.publish_to_pypi == "yes" %}

## Publishing to PyPI
This project is configured for PyPI publishing with Test PyPI validation:

1. **Setup**: Configure tokens in GitHub repository secrets:
   - `TEST_PYPI_API_TOKEN`: Token for https://test.pypi.org
   - `PYPI_API_TOKEN`: Token for https://pypi.org
2. **Release Process**: Create a GitHub release with a version tag (e.g., `v1.0.0`)
3. **Automation**: GitHub Actions will automatically:
   - Build the package
   - Create GitHub release
   - Publish to Test PyPI first
   - If successful, publish to production PyPI

### Manual Publishing
```bash
# Build the package
uv build

# Test on Test PyPI first
uv publish --publish-url https://test.pypi.org/legacy/

# Publish to production PyPI
uv publish
```

### Test PyPI Setup
1. Create account at https://test.pypi.org
2. Generate API token at https://test.pypi.org/manage/account/token/
3. Add token as `TEST_PYPI_API_TOKEN` in GitHub repository secrets
{%- endif %}

## Project Conventions

### Docstring Style
- Use reStructuredText (reST) style for docstrings, NOT Google or NumPy style
- Do NOT include type information in docstrings (types are handled by type hints)
- Tests generally don't need docstrings unless they're particularly complex
- Do NOT add docstrings to test functions explaining what they do - the test name should be self-documenting
- Example of correct docstring:
```python
def function_name(param1: str, param2: int) -> bool:
    """
    Brief description of function.

    Longer description if needed.

    :param param1: Description of param1
    :param param2: Description of param2
    :return: Description of return value
    """
```

### Git Workflow Notes for Claude
- Pre-commit hooks can modify files, causing commits to fail
- If a commit fails due to pre-commit changes:
  1. Stage the modified files with `git add`
  2. Retry the exact same commit command
  3. Do NOT create new commits or amend for hook changes
- Always check `git status` before and after commits

### Git Commit Conventions
Follow these patterns:

#### Commit Message Format
- **Use imperative mood**: "Add feature" not "Added feature" or "Adding feature"
- **Keep subject line concise**: Usually under 50 characters
- **No trailing punctuation**: Don't end subject with period
- **Focus on what was done**: Describe the change, not the problem

#### Examples of Good Commit Messages
```
Add user authentication module
Fix validation error in form submission
Update API endpoint documentation
Remove deprecated configuration options
```

#### Commit Body Format
- **Use present tense**: "This removes..." not "This removed..."
- **Explain what and why**: Include context if the change isn't obvious
- **Reference code elements**: Use backticks for code names, classes, methods
- **Multi-line when needed**: Break into logical paragraphs for complex changes

#### Code References in Commits
- Use backticks for code elements: `{{ cookiecutter.project_slug }}`, `main()` function
- Reference files with paths: `src/{{ cookiecutter.project_slug }}/core.py`
- Use quotes for strings or user-facing text

### Code Quality Standards
- Line length: {{ cookiecutter.line_length }} characters (enforced by ruff)
- Python version: {{ cookiecutter.python_version }}+ support
- Type hints required for all public functions
- Pre-commit hooks must pass before committing
- All tests must pass before merging
- **uv.lock should be committed** for reproducible builds (unlike poetry.lock)

## Contributing Guidelines
1. Follow the existing code style (enforced by ruff)
2. Add tests for new functionality
3. Update documentation as needed
4. Ensure all tests pass before submitting PR
5. Pre-commit hooks must pass
6. Follow the git commit conventions above

## Next Steps
{%- if cookiecutter.use_cli == "yes" %}
- Implement CLI commands in `src/{{ cookiecutter.project_slug }}/cli.py`
{%- endif %}
- Add your core functionality to `src/{{ cookiecutter.project_slug }}/`
- Write comprehensive tests in `tests/`
- Update this CLAUDE.md with project-specific details
{%- if cookiecutter.publish_to_pypi == "yes" %}
- Configure PyPI publishing credentials
{%- endif %}
- Set up GitHub repository and push initial code

---
*This project follows modern Python best practices and is optimized for development with AI coding assistants like Claude.*
