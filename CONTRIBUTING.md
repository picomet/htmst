# Contributing to Htmst

We're excited to have you contribute. Before you get started, please take a moment to review this guide to understand how to contribute effectively.

## Prerequisites

Before you begin contributing to Htmst, make sure you have the following installed.

-   [Python 3.12](https://www.python.org/downloads) or later
-   [uv 0.5.4](https://docs.astral.sh/uv) or later

## Setting up the project

1. [Fork the repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#forking-a-repository)

1. [Clone the repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#cloning-your-forked-repository)

1. Navigate to the project folder

    ```bash
    cd htmst
    ```

1. Sync the project dependencies

    ```bash
    uv sync --all-groups
    ```

1. Install pre-commit hooks

    ```bash
    pre-commit install
    ```

    ```bash
    pre-commit install-hooks
    ```

## Development workflow

1. Create a branch

    ```bash
    git checkout -b feature/my-feature
    ```

1. Write code

    Write your code, following the project's coding standards.

1. Test your changes

    Run the test suite to ensure your changes are working as expected.

    ```bash
    uv run pytest
    ```

    Or run the test suite with watch mode to automatically re-run tests when you make changes.

    ```bash
    uv run ptw .
    ```

1. Commit changes

    Use meaningful commit messages. If your change fixes a specific issue, reference it in the commit message

    ```bash
    git commit -m "Your commit message"
    ```

1. Push changes

    Push your changes to your forked repository

    ```bash
    git push origin feature/my-feature
    ```

## Submitting a pull request

1. [Open a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)

    Once your changes are ready, open a pull request on the main repository. Provide a clear description of your changes and reference any related issues.

1. Review and iterate

    Collaborate with maintainers and other contributors to address any feedback on your pull request. Make necessary changes and push them to the same branch.

1. Get your pull request approved

    Once your pull request is approved, it will be merged into the main branch. Congratulations on your contribution!

Thank you for contributing! 🎉 We appreciate your help in making this project better.
