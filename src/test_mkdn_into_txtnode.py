from mkdn_into_txtnode import split_nodes_delimiter
from textnode import (
    text_type_bold,
    text_type_code,
    text_type_italic,
    text_type_text,
    TextNode
)
import unittest

class TestInlineMarkdown(unittest.TestCase):
    def test_error_raised(self):
        node = TextNode("Still *wakes the deep", text_type_text)
        with self.assertRaises(ValueError) as context:
            split_nodes_delimiter([node], "*", text_type_italic)
        self.assertEqual(str(context.exception), "Invalid markdown, formatted section not closed")


    def test_regular_case(self):
        node = TextNode("Still *wakes* the deep", text_type_text)
        fordel = split_nodes_delimiter([node], "*", text_type_italic)
        enode = [TextNode("Still ", text_type_text), TextNode("wakes", text_type_italic), TextNode(" the deep", text_type_text)]
        self.assertEqual(fordel, enode)


    def test_multiple_cases(self):
        node = TextNode("Where *dips* the *rocky* highland", text_type_text)
        fordel = split_nodes_delimiter([node], "*", text_type_italic)
        enode = [TextNode("Where ", text_type_text), TextNode("dips", text_type_italic), TextNode(" the ", text_type_text), TextNode("rocky", text_type_italic), TextNode(" highland", text_type_text)]
        self.assertEqual(fordel, enode)


    def test_diff_delim(self):
        node = TextNode("*Come away* o human child, to the **waters and the wild**", text_type_text)
        fordel = split_nodes_delimiter([node], "**", text_type_bold)
        fordel = split_nodes_delimiter(fordel, "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("Come away", text_type_italic),
                TextNode(" o human child, to the ", text_type_text),
                TextNode("waters and the wild", text_type_bold)
            ],
            fordel
        )


    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("bold", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("italic", text_type_italic),
            ],
            new_nodes,
        )
