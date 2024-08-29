import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_code,
    text_type_image,
    text_type_italic,
    text_type_link,
    text_node_to_html_node
)
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertEqual(node, node2)

    def test_text_inequal(self):
        node = TextNode("This text is equal", text_type_text)
        node2 = TextNode("This text is not equal", text_type_text)
        self.assertNotEqual(node, node2)

    def test_text_type_inequal(self):
        node = TextNode("This text type is inequal", text_type_text)
        node2 = TextNode("This text type is inequal", text_type_bold)
        self.assertNotEqual(node, node2)

    def test_url_eq(self):
        node = TextNode("text string", text_type_bold, "website.com")
        node2 = TextNode("text string", text_type_bold, "website.com")
        self.assertEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode("text string", text_type_bold, "website.com")
        node2 = TextNode("text string", text_type_bold)
        self.assertNotEqual(node, node2)

    def test_empty_text(self):
        node = TextNode("", text_type_text)
        expected = "TextNode(, text, None)"
        self.assertEqual(repr(node), expected)

    def test_empty_text_type(self):
        node = TextNode("text string", "")
        expected = "TextNode(text string, , None)"
        self.assertEqual(repr(node), expected)

    def test_base_repr(self):
        node = TextNode("This is text", text_type_bold, "website.com")
        expected = "TextNode(This is text, bold, website.com)"
        self.assertEqual(repr(node), expected)




class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_to_html_text(self):
        tnode = TextNode("hello", text_type_text)
        lnode = text_node_to_html_node(tnode)
        self.assertEqual(lnode.value, "hello")
        self.assertEqual(lnode.tag, None)


    def test_text_to_html_italic(self):
        tnode = TextNode("hello", text_type_italic)
        lnode = text_node_to_html_node(tnode)
        self.assertEqual(lnode.tag, "i")
        self.assertEqual(lnode.value, "hello")


    def test_text_to_html_link(self):
        tnode = TextNode("blizzard", text_type_link, "www.blizzard.com")
        lnode = text_node_to_html_node(tnode)
        self.assertEqual(lnode.tag, "a")
        self.assertEqual(lnode.value, "blizzard")
        self.assertEqual(lnode.props, {"href": "www.blizzard.com"})


if __name__ == "__main__":
    unittest.main()