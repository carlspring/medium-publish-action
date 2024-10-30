# Publish Markdown to Medium GitHub Action

This GitHub Action publishes Markdown files to Medium as stories or drafts.

## Usage

Add the following workflow to your repository to use this action.

### Example Workflow

```yaml
name: Publish Markdown to Medium
on:
  push:
    paths:
      - "content/*.md"

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Publish Markdown to Medium
        uses: carlspring/medium-publisher-action@v1
        with:
          medium_token: ${{ secrets.MEDIUM_TOKEN }}
          file_path: "content/your-article.md"
          publish_status: "draft" # Use 'public' to publish immediately
```

## Inputs

* `medium_token` (Required): Your Medium integration token.
* `file_path` (Required): Path to the Markdown file to publish.
* `publish_status`: (Optional): Set to draft (default) or public.

## Medium Integration Token

* Go to Medium `Settings`.
* Generate an integration token.
* Add this token as a secret in your GitHub repository under `Settings` > `Secrets and variables` > `Actions` (e.g., `MEDIUM_TOKEN`).
