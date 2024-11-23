from htmst import HtmlAst
from htmst.structures import (
    CommentNode,
    DoctypeNode,
    DoubleNode,
    Pos,
    SingleNode,
    TextNode,
)


def test_text():
    html = """hi"""
    ast = HtmlAst(html)
    node = ast.root.children[0]
    assert isinstance(node, TextNode)
    assert node.text == "hi"


def test_double():
    html = """<div>hi</div>"""
    ast = HtmlAst(html)
    node = ast.root.children[0]
    assert isinstance(node, DoubleNode)
    assert node.tag == "div"
    assert hasattr(node, "children")
    assert node.start == Pos(0, 0)
    assert node.end == Pos(0, len(html))


def test_single():
    html = """<input type="text" />"""
    ast = HtmlAst(html)
    node = ast.root.children[0]
    assert isinstance(node, SingleNode)
    assert node.tag == "input"
    assert not hasattr(node, "children")
    assert node.start == Pos(0, 0)
    assert node.end == Pos(0, len(html))


def test_attrs():
    html = """<div class="foo" id="bar" @click="alert()">hi</div>"""
    ast = HtmlAst(html)
    node = ast.root.children[0]
    assert isinstance(node, DoubleNode)
    assert node.tag == "div"
    assert node.attrs[0].name == "class"
    assert node.attrs[0].value == "foo"
    assert node.attrs[1].name == "id"
    assert node.attrs[1].value == "bar"
    assert node.attrs[2].name == "@click"
    assert node.attrs[2].value == "alert()"
    assert node.start == Pos(0, 0)
    assert node.end == Pos(0, len(html))


def test_double_quote():
    html = """<div class="foo \\" bar">hi</div>"""
    ast = HtmlAst(html)
    node = ast.root.children[0]
    assert isinstance(node, DoubleNode)
    assert node.tag == "div"
    assert node.attrs[0].value == 'foo \\" bar'
    assert node.start == Pos(0, 0)
    assert node.end == Pos(0, len(html))


def test_single_quote():
    html = """<div class='foo \\' bar'>hi</div>"""
    ast = HtmlAst(html)
    node = ast.root.children[0]
    assert isinstance(node, DoubleNode)
    assert node.tag == "div"
    assert node.attrs[0].value == "foo \\' bar"
    assert node.start == Pos(0, 0)
    assert node.end == Pos(0, len(html))


def test_comment():
    html = """<!-- comment -->"""
    ast = HtmlAst(html)
    node = ast.root.children[0]
    assert isinstance(node, CommentNode)
    assert node.text == " comment "
    assert node.start == Pos(0, 0)
    assert node.end == Pos(0, len(html))


def test_doctype():
    html = """<!DOCTYPE html>"""
    ast = HtmlAst(html)
    node = ast.root.children[0]
    assert isinstance(node, DoctypeNode)
    assert node.text == "html"
    assert node.start == Pos(0, 0)
    assert node.end == Pos(0, len(html))


class TestSource:
    def test_first_bracket(self):
        html = """<script>foo(</script>)</script>"""
        ast = HtmlAst(html)
        node = ast.root.children[0]
        assert isinstance(node, DoubleNode)
        assert node.tag == "script"
        assert node.start == Pos(0, 0)
        assert node.end == Pos(0, len(html))

    def test_second_bracket(self):
        html = """<script>function foo(){ </script>; }</script>"""
        ast = HtmlAst(html)
        node = ast.root.children[0]
        assert isinstance(node, DoubleNode)
        assert node.tag == "script"
        assert node.start == Pos(0, 0)
        assert node.end == Pos(0, len(html))

    def test_third_bracket(self):
        html = """<script>function foo(){ bar[</script>]; }</script>"""
        ast = HtmlAst(html)
        node = ast.root.children[0]
        assert isinstance(node, DoubleNode)
        assert node.tag == "script"
        assert node.start == Pos(0, 0)
        assert node.end == Pos(0, len(html))

    def test_signle_quote(self):
        html = """<script>function foo(){ bar['</script>']; }</script>"""
        ast = HtmlAst(html)
        node = ast.root.children[0]
        assert isinstance(node, DoubleNode)
        assert node.tag == "script"
        assert node.start == Pos(0, 0)
        assert node.end == Pos(0, len(html))

    def test_double_quote(self):
        html = """<script>function foo(){ bar["</script>"]; }</script>"""
        ast = HtmlAst(html)
        node = ast.root.children[0]
        assert isinstance(node, DoubleNode)
        assert node.tag == "script"
        assert node.start == Pos(0, 0)
        assert node.end == Pos(0, len(html))
