# Contributing to [Project Name]

Thank you for considering contributing to [Project Name]! This guide outlines the process for contributing to ensure a smooth and efficient collaboration.

## Table of Contents
1. [Branching Strategy](#branching-strategy)
2. [Commit Messages](#commit-messages)
3. [Development Workflow](#development-workflow)
4. [Pull Requests](#pull-requests)
5. [Releases](#releases)
6. [Code of Conduct](#code-of-conduct)

---

## Branching Strategy

Our project follows a structured branching strategy to keep the codebase clean and organized:

- **`main`**: The production-ready branch. Contains stable release commits only.
- **`develop`**: The main development branch. All new features, fixes, and changes are merged here.
- **Feature Branches**: Created for specific tasks, using the following naming conventions:
  - `feat/feature-name` for new features.
  - `fix/bug-name` for bug fixes.
  - `chore/task-name` for maintenance or tooling updates.
  - `docs/documentation-name` for documentation updates.

---

## Commit Messages

We use [Conventional Commits](https://www.conventionalcommits.org/) to maintain a consistent and informative commit history. Here are the guidelines:

- **Format**: `<type>: <description>`
- **Types**:
  - `feat`: A new feature.
  - `fix`: A bug fix.
  - `docs`: Documentation updates.
  - `chore`: Tooling or maintenance tasks (e.g., updates to dependencies).
- **Examples**:
  - `feat: add user authentication`
  - `fix: resolve issue with data validation`
  - `docs: update API documentation`

---

## Development Workflow

### 1. **Setting Up**
- Clone the repository:
  ```bash
  git clone https://github.com/your-repo/project-name.git
  cd project-name
  ```
- Create a new branch for your task:
  ```bash
  git checkout -b feat/your-feature-name
  ```

### 2. **Developing**
- Make your changes and commit them to your branch:
  ```bash
  git add .
  git commit -m "feat: describe your change"
  ```

### 3. Syncing
- Regularly sync your branch with the latest `develop` branch:
  ```bash
  git pull origin develop
  ```

### 4. Testing
- Ensure your code is tested and passes any linting or test requirements before opening a pull request.


## Pull Requests

When your changes are ready, open a pull request (PR) to merge your branch into `develop`:

1. Base Branch: PRs should target the `develop` branch.
2. Description: Provide a clear description of the changes in your PR.
3. Checklist:
    * Code follows the style guidelines.
    * Commits follow the Conventional Commit format.
    * Tests are written/updated, and all tests pass.
4. Approval: Your PR will be reviewed and may require changes before being merged.


## Releases

* Releases are managed by merging the `develop` branch into `main` via a squash merge.
* Each release is tagged using Semantic Versioning, e.g., `v1.0.0`.
* Release commit messages follow the format:
```bash
chore(release): v1.0.0
```

## Code of Conduct

By contributing, you agree to follow our Code of Conduct to foster an open and welcoming environment.

# Questions?

If you have any questions, feel free to open an issue or contact the maintainers at @richardesp.

Thank you for contributing!