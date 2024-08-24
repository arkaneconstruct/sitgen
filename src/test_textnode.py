import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_none(self):
        node = TextNode("This is a text node","bold", None)
    
    def test_uneq_text(self):
        node = TextNode("Text A", "bold")
        node2 = TextNode("Text B", "bold")
        self.assertNotEqual(node,node2)

    def test_uneq_text_type(self):
        node = TextNode("Text A", "bold")
        node2 = TextNode("Text A", "italic")
        self.assertNotEqual(node,node2)


if __name__ == "__main__":
    unittest.main()