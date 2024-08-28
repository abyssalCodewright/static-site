from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    node = ParentNode(
        "p", [
            LeafNode("b", "This is bold text"),
            LeafNode("i", "This is italic text")
        ]
    )
    print(repr(node))

main()