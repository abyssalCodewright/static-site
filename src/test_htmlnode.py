import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_repr_works(self):
        node = HTMLNode("p", "This is a paragraph.", None, {"href": "www.blizzard.com"})
        expect = "HTMLNode(p, This is a paragraph., children: None, {'href': 'www.blizzard.com'})"
        self.assertEqual(repr(node), expect)


    def test_props_to_html_works(self):
        props = HTMLNode("p", "text string", None, {"href": "www.blizzard.com"})
        expect = ' href="www.blizzard.com"'
        self.assertEqual(props.props_to_html(), expect)


    def test_props_to_html_twice(self):
        props = HTMLNode("p", "text string", None, {"href": "www.blizzard.com", "target": "_blank"})
        expect = ' href="www.blizzard.com" target="_blank"'
        self.assertEqual(props.props_to_html(), expect)


    def test_all_none(self):
        node = HTMLNode()
        expect = "HTMLNode(None, None, children: None, None)"
        self.assertEqual(repr(node), expect)


    def test_values(self):
        node = HTMLNode("div", "Eff you, I can read and write, too.")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Eff you, I can read and write, too.")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)


    def test_value_is_none(self):
        with self.assertRaises(ValueError) as context:
            LeafNode("p", None).to_html()
        self.assertEqual(str(context.exception), "All LeafNodes must have a value")


    def test_tag_is_none(self):
        node = LeafNode(None, "sentence here")
        expect = "sentence here"
        self.assertEqual(node.to_html(), expect)


    def test_link(self):
        node = LeafNode("a", "blizzard", {"website": "www.blizzard.com"})
        enode = '<a website="www.blizzard.com">blizzard</a>'
        self.assertEqual(node.to_html(), enode)


    def test_paragraph(self):
        node = LeafNode("p", "This is a paragraph")
        enode = "<p>This is a paragraph</p>"
        self.assertEqual(node.to_html(), enode)


    def test_bold(self):
        node = LeafNode("b", "This text is bold")
        enode = "<b>This text is bold</b>"
        self.assertEqual(node.to_html(), enode)



if __name__ == "__main__":
    unittest.main()