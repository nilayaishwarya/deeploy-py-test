# Developer Guide

## Documentation

For generating documentation, we use [pydoc-markdown](https://pydoc-markdown.readthedocs.io/en/latest/) and [mkdocs-material](https://squidfunk.github.io/mkdocs-material/).

### Generate

1. Generate the markdown from python code

    ```bash
    pydoc-markdown --render-toc -v
    ```

2. Generate HTML from the markdown

    ```bash
    mkdocs build -f docs/mkdocs.yml
    ```