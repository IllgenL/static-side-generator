import unittest
from htmlnode import HTMLNode, ParentNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a", "b", None, {})
        node2 = HTMLNode("a", "b", None, {})
        self.assertNotEqual(node, node2)

    def test_tag_diff(self):
        node = HTMLNode(
            "a",
            props={
                "href": "http://localhost:8888",
            },
        )
        node2 = HTMLNode("img", props={"href": "http://localhost:8888"})
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode(props={"href": "http://localhost", "target": "_blank"})
        testProps = ' href="http://localhost" target="_blank"'
        self.assertEqual(node.props_to_html(), testProps)


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, world!", {"href": "localhost:4040"})
        self.assertEqual(node.to_html(), '<a href="localhost:4040">Hello, world!</a>')


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()
