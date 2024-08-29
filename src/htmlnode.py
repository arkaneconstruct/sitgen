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