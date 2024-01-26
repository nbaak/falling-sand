

class Pixel:
    
    def __init__(self, pos, color=None):
        self.pos = pos
        self.color = color
        self.final = False
        
    def __eq__(self, other):
        if isinstance(other, tuple):
            return self.pos == other
            
        elif isinstance(other, Pixel):
            return self.pos == other.pos
            
    def __repr__(self):
        return f"{self.pos=} {self.color=}"