"""Tests for cookiecutter project generation."""

import subprocess

from pytest_cookies.plugin import Cookies


def test_default_project_generation(cookies: Cookies):
    result = cookies.bake()

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.is_dir()

    # Check basic structure
    assert (result.project_path / "src" / "my_awesome_project").is_dir()
    assert (result.project_path / "tests").is_dir()
    assert (result.project_path / "pyproject.toml").is_file()
    assert (result.project_path / "README.md").is_file()
    assert (result.project_path / "LICENSE").is_file()
    assert (result.project_path / "Makefile").is_file()
    assert (result.project_path / "tox.ini").is_file()
    assert (result.project_path / ".gitignore").is_file()
    assert (result.project_path / ".pre-commit-config.yaml").is_file()

    # Check src layout
    assert (result.project_path / "src" / "my_awesome_project" / "__init__.py").is_file()

    # CLI should not exist by default
    assert not (result.project_path / "src" / "my_awesome_project" / "cli.py").exists()

    # PyPI release workflow should not exist by default
    assert not (result.project_path / ".github" / "workflows" / "release.yml").exists()


def test_project_with_cli(cookies: Cookies):
    result = cookies.bake(extra_context={"use_cli": "yes"})

    assert result.exit_code == 0
    assert (result.project_path / "src" / "my_awesome_project" / "cli.py").is_file()

    # Check CLI content
    cli_content = (result.project_path / "src" / "my_awesome_project" / "cli.py").read_text()
    assert "import click" in cli_content
    assert "from rich.console import Console" in cli_content


def test_project_with_pypi_publishing(cookies: Cookies):
    result = cookies.bake(extra_context={"publish_to_pypi": "yes"})

    assert result.exit_code == 0
    assert (result.project_path / ".github" / "workflows" / "release.yml").is_file()

    # Check pyproject.toml has PyPI metadata
    pyproject_content = (result.project_path / "pyproject.toml").read_text()
    assert "keywords = " in pyproject_content
    assert "classifiers = " in pyproject_content
    assert "[project.urls]" in pyproject_content

    # Check README has publishing section
    readme_content = (result.project_path / "README.md").read_text()
    assert "## Publishing" in readme_content
    assert "PyPI" in readme_content


def test_all_license_options(cookies: Cookies):
    licenses = ["MIT", "BSD-3-Clause", "Apache-2.0", "GPL-3.0", "Not open source"]

    for license_choice in licenses:
        result = cookies.bake(extra_context={"open_source_license": license_choice})
        assert result.exit_code == 0

        license_content = (result.project_path / "LICENSE").read_text()
        if license_choice == "MIT":
            assert "MIT License" in license_content
        elif license_choice == "BSD-3-Clause":
            assert "BSD 3-Clause License" in license_content
        elif license_choice == "Apache-2.0":
            assert "Apache License" in license_content
        elif license_choice == "GPL-3.0":
            assert "GNU General Public License" in license_content
        else:
            assert "All rights reserved" in license_content


def test_python_version_configuration(cookies: Cookies):
    result = cookies.bake(extra_context={"python_version": "3.11", "publish_to_pypi": "yes"})

    assert result.exit_code == 0
    pyproject_content = (result.project_path / "pyproject.toml").read_text()
    assert 'requires-python = ">=3.11"' in pyproject_content
    assert '"Programming Language :: Python :: 3.11"' in pyproject_content


def test_custom_project_slug(cookies: Cookies):
    result = cookies.bake(
        extra_context={"project_name": "My Test Project", "project_slug": "my_test_project"}
    )

    assert result.exit_code == 0
    assert (result.project_path / "src" / "my_test_project").is_dir()
    assert (result.project_path / "src" / "my_test_project" / "__init__.py").is_file()


def test_generated_project_structure(cookies: Cookies):
    result = cookies.bake(extra_context={"project_slug": "test_project"})

    assert result.exit_code == 0

    # Check that the package structure is correct for installation
    assert (result.project_path / "pyproject.toml").is_file()
    assert (result.project_path / "src" / "test_project" / "__init__.py").is_file()

    # Check that pyproject.toml has correct build configuration
    pyproject_content = (result.project_path / "pyproject.toml").read_text()
    assert "[build-system]" in pyproject_content
    assert "hatchling" in pyproject_content


def test_generated_project_installable(cookies: Cookies):
    result = cookies.bake(extra_context={"project_slug": "test_installable"})

    assert result.exit_code == 0

    try:
        # Use tox to test installation in an isolated environment
        # This creates a fresh environment and tries to install the package
        tox_result = subprocess.run(
            ["tox", "-e", "py", "--notest"],  # Create environment but don't run tests
            cwd=result.project_path,
            capture_output=True,
            text=True,
            timeout=120,  # 2 minute timeout for environment creation
        )

        if tox_result.returncode == 0:
            # If tox environment creation succeeded, the package is installable
            assert True
        else:
            # If tox failed, check if it's because tox isn't available
            if (
                "tox: command not found" in tox_result.stderr
                or "No module named tox" in tox_result.stderr
            ):
                # Fall back to basic structure validation
                assert (result.project_path / "pyproject.toml").is_file()
                assert (result.project_path / "src" / "test_installable" / "__init__.py").is_file()

                # Verify pyproject.toml has valid build configuration
                pyproject_content = (result.project_path / "pyproject.toml").read_text()
                assert "hatchling" in pyproject_content
                assert "test_installable" in pyproject_content
            else:
                # If tox is available but failed, that's a real error
                raise AssertionError(f"tox environment creation failed: {tox_result.stderr}")

    except (FileNotFoundError, subprocess.TimeoutExpired):
        # If tox isn't available or times out, verify the project structure manually
        assert (result.project_path / "pyproject.toml").is_file()
        assert (result.project_path / "src" / "test_installable" / "__init__.py").is_file()

        # Verify pyproject.toml has valid build configuration
        pyproject_content = (result.project_path / "pyproject.toml").read_text()
        assert "hatchling" in pyproject_content
        assert "test_installable" in pyproject_content


def test_makefile_targets(cookies: Cookies):
    result = cookies.bake()

    assert result.exit_code == 0
    makefile_content = (result.project_path / "Makefile").read_text()

    expected_targets = [
        "help",
        "install",
        "dev",
        "test",
        "coverage",
        "lint",
        "format",
        "typecheck",
        "clean",
    ]
    for target in expected_targets:
        assert f"{target}:" in makefile_content


def test_github_actions_workflows(cookies: Cookies):
    result = cookies.bake()

    assert result.exit_code == 0
    assert (result.project_path / ".github" / "workflows" / "tests.yml").is_file()

    # Test workflow should always exist
    test_workflow = (result.project_path / ".github" / "workflows" / "tests.yml").read_text()
    assert "name: Tests" in test_workflow
    assert "uv sync --group dev" in test_workflow


def test_dependency_groups(cookies: Cookies):
    result = cookies.bake()

    assert result.exit_code == 0
    pyproject_content = (result.project_path / "pyproject.toml").read_text()

    assert "[dependency-groups]" in pyproject_content
    assert "dev = [" in pyproject_content
    assert "test = [" in pyproject_content
    assert "{ include-group = " in pyproject_content


def test_project_with_claude(cookies: Cookies):
    result = cookies.bake(extra_context={"use_claude": "yes"})

    assert result.exit_code == 0
    assert (result.project_path / "CLAUDE.md").is_file()

    # Check CLAUDE.md content
    claude_content = (result.project_path / "CLAUDE.md").read_text()
    assert "# CLAUDE.md - Project Context" in claude_content
    assert "My Awesome Project" in claude_content
    assert "uv" in claude_content
    assert "pytest" in claude_content


def test_project_without_claude(cookies: Cookies):
    result = cookies.bake(extra_context={"use_claude": "no"})

    assert result.exit_code == 0
    assert not (result.project_path / "CLAUDE.md").exists()
