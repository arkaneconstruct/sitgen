from textnode import TextNode

class HTMLNode():
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = [] if children is None else children
        self.props = {} if props is None else props
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        x = ""
        for key,value in self.props.items():
            x += f' {key}="{value}"'
        return x
    
    def __repr__(self):
        x = f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
        return x


class LeafNode(HTMLNode):
    def __init__(self,tag=None, value=None, props=None):
        super().__init__(self,tag,value,props)
        self.tag = tag
        self.value = value
        self.props = props if props is not None else {}

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value.")
        
        if self.tag is None:
            return str(self.value)

        x = super().props_to_html()
        return f"<{self.tag}{x}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(self,tag,children,props)
        self.tag=tag
        self.children=children
        self.props = props if props is not None else {}

    def to_html(self):
        if self.tag is None:
            raise ValueError("All parent nodes must have a tag.")
        if self.children is None:
            raise ValueError("All parent nodes must have children.")
        html_content = ''
        for child in self.children:
            html_content += child.to_html()
        return f"<{self.tag}>{html_content}</{self.tag}>"
    
def text_node_to_html_node(text_node):
    accepted_types = ["text","bold","italic","code","link","image"]
    if text_node.text_type not in accepted_types:
        raise Exception("Not a valid type.")
    if text_node.text_type == "text":
        new_node = LeafNode(value=text_node.text)
    if text_node.text_type == "bold":
        new_node = LeafNode(tag="b", value=text_node.text)
    if text_node.text_type == "italic":
        new_node = LeafNode(tag="i", value=text_node.text)
    if text_node.text_type == "code":
        new_node = LeafNode(tag="code", value=text_node.text)
    if text_node.text_type == "link":
        new_node = LeafNode(tag="a", value=text_node.text,props={"href":text_node.url})
    if text_node.text_type =="image":
        new_node = LeafNode(tag="img", value="",props={"src":text_node.url,"alt":text_node.text})
    return new_node