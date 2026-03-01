from Sub import * 
class Skill:
    def __init__(self, name, sub, description, parent=None, child=None):
        self.name = name
        self.description = description
        self.parent = parent
        self.child = child
        self.sub = sub
        vars = [self.name, self.description, self.parent, self.child, self.sub]
    def details(self):
        
        return[f"DETAILS of [{self.name}] ({self})",
        f"[SUB]: {self.sub.name} ({self.sub})",
        f"[DESCRIPTION]: {self.description}",
        f"[PARENT]: {None if self.parent == None else self.parent.name} ({self.parent})",
        f"[CHILD]: {self.child}\n----------"]