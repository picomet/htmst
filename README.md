# htmst

![PyPI - Python Versions](https://img.shields.io/pypi/pyversions/htmst)

htmst is a python library for parsing html into AST.

## Installation

```bash
pip install htmst
```

## Usage

```python
from htmst import HtmlAst

html = """<span foo="bar">hi</span>"""
ast = HtmlAst(html)

print(ast.root.children[0].tag) # span

print(ast.root.children[0].attrs[0].name) # foo

print(ast.root.children[0].attrs[0].value) # bar
```

## Development

### Setup

```bash
git clone https://github.com/mahdibm/htmst.git
cd htmst
uv sync
```

### Testing

```bash
uv run ptw .
```

### Linting

```bash
uv run ruff .
```

### Formatting

```bash
uv run black .
```
