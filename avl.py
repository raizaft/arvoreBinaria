class No: 
    def __init__(self, carga): 
        self.carga = carga 
        self.esq = None
        self.dir = None
        self.altura = 1

    def __str__(self):
        return f'|{self.carga}:h={self.altura}|'

class AVL: 
    def __init__(self, carga = None):
        if carga is None:
            self.__raiz = None
        else:
            self.__raiz = self.add(carga)

    def estaVazia(self)->bool:
        return self.__raiz == None

    def insert(self, novo):
        if(self.__raiz == None):
            self.__raiz = No(novo)
        else:
            self.__raiz = self.__insert(self.__raiz, novo)
  
    def __insert(self, no, novo):
        # Step 1 - Performs a BST recursion to add the node
        if not no: 
            return No(novo) 
        elif novo < no.carga: 
            no.esq = self.__insert(no.esq, novo) 
        else: 
            no.dir = self.__insert(no.dir, novo) 
  
        # Step 2 - Update the Altura of ancestor node
        no.altura = 1 + max(self.getAltura(no.esq), 
                              self.getAltura(no.dir)) 
  
        # Step 3 - Computes the balance factor 
        balance = self.getBalance(no) 
  
        # Step 4 - Checks if the node is unbalanced
        # Then, one of the following actions will be performed:

        # CASE 1 - dir rotation
        if balance > 1 and novo < no.esq.carga: 
            return self.__rotacaoDir(no) 
  
        # CASE 2 - esq rotation
        if balance < -1 and novo > no.dir.carga: 
            return self.__rotacaoEsq(no) 
  
        # CASE 3 - Double rotation: esq dir 
        if balance > 1 and novo > no.esq.carga: 
            no.esq = self.__rotacaoEsq(no.esq) 
            return self.__rotacaoDir(no) 
  
        # CASE 4 - Double rotation: dir esq 
        if balance < -1 and novo < no.dir.carga: 
            no.dir = self.__rotacaoDir(no.dir) 
            return self.__rotacaoEsq(no) 
        return no
  
    def __rotacaoEsq(self, p)->No: 
        u = p.dir 
        T2 = u.esq 
  
        u.esq = p 
        p.dir = T2 

        p.altura = 1 + max(self.getAltura(p.esq), 
                         self.getAltura(p.dir)) 
        u.altura = 1 + max(self.getAltura(u.esq), 
                         self.getAltura(u.right)) 
        return u 
  
    def __rotacaoDir(self, p)->No: 
        u = p.esq 
        T2 = u.dir 

        u.dir = p 
        p.esq = T2 

        p.altura = 1 + max(self.getAltura(p.esq), 
                        self.getAltura(p.dir)) 
        u.altura = 1 + max(self.getAltura(u.esq), 
                        self.getAltura(u.dir)) 
        return u 
  
    def getAltura(self, no)->int: 
        if no is None: 
            return 0
        return no.altura 
  
    def getBalance(self, no)->int: 
        if not no: 
            return 0
  
        return self.getAltura(no.esq) - self.getAltura(no.dir) 
  
    def preOrder(self):
        self.__preOrder(self.__raiz)

    def __preOrder(self, no): 
        if not no: 
            return
  
        print("{0} ".format(no.carga), end="") 
        self.__preOrder(no.esq) 
        self.__preOrder(no.dir) 

    def delete(self, chave):
        if(self.__raiz is not None):
            self.__raiz = self.__delete(self.__raiz, chave)
        
    def __delete(self, no, chave)->No: 
        if not no: 
            return no 
        elif chave < no.carga: 
            no.esq = self.__delete(no.esq, chave)   
        elif chave > no.carga: 
            no.dir = self.__delete(no.dir, chave)   
        else: 
            if no.esq is None: 
                temp = no.dir 
                no = None
                return temp 
  
            elif no.dir is None: 
                temp = no.esq 
                no = None
                return temp 
  
            temp = self.getMincargaNode(no.dir) 
            no.carga = temp.carga 
            no.dir = self.__delete(no.dir, temp.carga) 

        if no is None: 
            return no 

        no.altura = 1 + max(self.getAltura(no.esq), 
                            self.getAltura(no.dir)) 
  
        balance = self.getBalance(no) 
  
        if balance > 1 and self.getBalance(no.esq) >= 0: 
            return self.__rotacaoDir(no) 
  
        # Case 2 - Right Right 
        if balance < -1 and self.getBalance(no.dir) <= 0: 
            return self.__rotacaoEsq(no) 
  
        # Case 3 - esq dir 
        if balance > 1 and self.getBalance(no.esq) < 0: 
            no.esq = self.__rotacaoEsq(no.esq) 
            return self.__rotacaoDir(no) 
  
        # Case 4 - dir esq 
        if balance < -1 and self.getBalance(no.dir) > 0: 
            no.dir = self.__rotacaoDir(no.dir) 
            return self.__rotacaoEsq(no) 
        return no  

    def getNo(self)->No :
        return self.__no
    
    def getMincargaNode(self, no)->No:
        if no is None or no.esq is None:
            return no
        return self.getMincargaNode(no.esq)

if __name__ == '__main__':
    a = AVL()
    a.insert(42)
    a.insert(15)
    a.insert(88)
    a.insert(6)
    a.insert(27)
    a.insert(4)
    a.preOrder()
    print('')
    a.delete(15)
    a.preOrder()