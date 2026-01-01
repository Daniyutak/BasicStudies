# t -> grau
# 2t -1 -> maximo de chaves
# t-1 -> minimo de chaves (exceto raiz)
# 2t -> maximo de filhos
# t -> minimo de filhos (exceto raiz)

class node:
    def __init__(self):
        self.keys = []
        self.children = []
        self.leaf = False


class tree:
    def __init__(self, t):
        self.t = t
        self.root = node()
        self.root.leaf = True
    
    def insert(self, key, current=None):
        if current is None: current = self.root
        
        if current.keys[0] == None:
            self.current.keys.append(key)
            return
        
        else:
            for i in self.root.keys:
                if key < i:
                    self.insert(key, current.children[i])
        
        

            

            

     

