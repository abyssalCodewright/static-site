from mkdn_into_txtnode import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link
from textnode import (
    text_type_bold,
    text_type_code,
    text_type_italic,
    text_type_text,
    text_type_image,
    text_type_link,
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


    def test_extract_images(self):
        words = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(extract_markdown_images(words), [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')])


    def test_extract_images_with_less_punc(self):
        words = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(extract_markdown_images(words), [('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')])


    def test_extract_links(self):
        words = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown_links(words), [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])


    def test_extract_links_with_punc(self):
        words = "This is text with a link ![to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown_links(words), [("to youtube", "https://www.youtube.com/@bootdotdev")])


    def test_split_image_single(self):
            node = TextNode("This is text with a image ![to boot dev](https://www.boot.dev)", text_type_text)
            self.assertListEqual(
                [
                    TextNode("This is text with a image ", text_type_text),
                    TextNode("to boot dev", text_type_image, "https://www.boot.dev")
                ],
                split_nodes_image([node])
            )


    def test_split_image_just_image(self):
        node = TextNode("![to boot dev](https://www.boot.dev)", text_type_text)
        self.assertListEqual(
            [
                TextNode("to boot dev", text_type_image, "https://www.boot.dev")
            ],
            split_nodes_image([node])
        )


    def test_split_image_multiple(self):
        node = TextNode("This is text with a image ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)", text_type_text)
        self.assertListEqual(
            [
                TextNode("This is text with a image ", text_type_text),
                TextNode("to boot dev", text_type_image, "https://www.boot.dev"),
                TextNode(" and ", text_type_text),
                TextNode("to youtube", text_type_image, "https://www.youtube.com/@bootdotdev")
            ],
            split_nodes_image([node])
        )


    def test_split_link(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", text_type_text)
        self.assertListEqual(
            [
                TextNode("This is text with a link ", text_type_text),
                TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
                TextNode(" and ", text_type_text),
                TextNode("to youtube", text_type_link, "https://www.youtube.com/@bootdotdev")
            ],
            split_nodes_link([node])
        )