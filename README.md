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

print(ast.root.children[0].start.row) # 0
print(ast.root.children[0].start.col) # 0

print(ast.root.children[0].end.row) # 0
print(ast.root.children[0].end.col) # 25

print(ast.root.children[0].attrs[0].name) # foo
print(ast.root.children[0].attrs[0].value) # bar

print(ast.root.children[0].attrs[0].start.row) # 0
print(ast.root.children[0].attrs[0].start.col) # 6

print(ast.root.children[0].attrs[0].end.row) # 0
print(ast.root.children[0].attrs[0].end.col) # 15
```

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) for more information.

## License

This project is licensed under the [MIT License](LICENSE).
