#!/usr/bin/env python
"""Post-generation hook to clean up conditional files and run initial setup."""

import os
import shutil
import subprocess


def remove_file(filepath):
    """Remove a file if it exists."""
    if os.path.exists(filepath):
        os.remove(filepath)


def remove_dir(dirpath):
    """Remove a directory if it exists."""
    if os.path.exists(dirpath):
        shutil.rmtree(dirpath)


def run_command(command, shell=False):
    """Run a shell command."""
    try:
        subprocess.run(command, shell=shell, check=True)
        return True
    except subprocess.CalledProcessError:
        return False


# Remove CLI file if not needed
if "{{ cookiecutter.use_cli }}" != "yes":
    remove_file("src/{{ cookiecutter.project_slug }}/cli.py")

# Remove CLAUDE.md if not needed
if "{{ cookiecutter.use_claude }}" != "yes":
    remove_file("CLAUDE.md")

# Remove PyPI publishing workflow if not needed
if "{{ cookiecutter.publish_to_pypi }}" != "yes":
    remove_file(".github/workflows/release.yml")

# Check if uv is installed and create lock file
if shutil.which("uv"):
    print("\n✓ uv is installed")

    # Create uv.lock file for the project
    if run_command(["uv", "lock"]):
        print("✓ Created uv.lock file")

# Initialize git repository
if run_command(["git", "init"]):
    print("✓ Initialized git repository")

    # Create initial commit
    run_command(["git", "add", "."])
    run_command(["git", "commit", "-m", "Initial commit from cookiecutter template"])
    print("✓ Created initial commit")

# Print next steps
if shutil.which("uv"):
    print("\nNext steps:")
    print("1. cd {{ cookiecutter.project_slug }}")
    print("2. uv sync --all-extras")
    print("3. pre-commit install")
    print("4. make test")
else:
    print("\n⚠ uv is not installed")
    print("Install it with: curl -LsSf https://astral.sh/uv/install.sh | sh")

print("\n✨ Project '{{ cookiecutter.project_name }}' created successfully!")
