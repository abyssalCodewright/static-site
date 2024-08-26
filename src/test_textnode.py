import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_code,
    text_type_image,
    text_type_italic,
    text_type_link,
)


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


if __name__ == "__main__":
    unittest.main()