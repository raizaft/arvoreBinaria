class No:
    def __init__(self,carga:any):
        self.carga = carga
        self.esq = None
        self.dir = None

    def __str__(self):
        return str(self.carga)
    
class ArvoreBinaria:        
    def __init__(self, carga_da_raiz:any = None):
        if carga_da_raiz is None:
            self.__raiz = carga_da_raiz
        else:
            self.__raiz = No(carga_da_raiz)
        self.__cursor = self.__raiz
        self.__tamanho = 0

    def estaVazia(self)->bool:
        return self.__raiz == None
    
    def criaRaiz(self, carga:any):
        if self.__raiz is None:
            self.__raiz = No(carga)
            self.__cursor = self.__raiz
            self.__tamanho += 1
    
    def getRaiz(self)->any:
        if self.__raiz != None:
            return self.__raiz.carga
        else:
            return None

    def getCursor(self)->any:
        if self.__cursor != None:
            return self.__cursor.carga
        else:
            return None
    
    def preordem(self):
        self.__preordem(self.__raiz)

    def __preordem(self, no:No):
        if no != None:
            print(f'{no.carga}',end=' ')
            self.__preordem(no.esq)
            self.__preordem(no.dir)

    def emordem(self):
        self.__emordem(self.__raiz)

    def __emordem(self, no):
        if no is not None:
            self.__emordem(no.esq)
            print(f'{no.carga}',end=' ')
            self.__emordem(no.dir)
    
    def posordem(self):
        self.__posordem(self.__raiz)

    def __posordem(self, no):
        if no is not None:
            self.__posordem(no.esq)
            self.__posordem(no.dir)
            print(f'{no.carga}',end=' ')
    
    def descerEsquerda(self):
        if self.__cursor is not None and self.__cursor.esq is not None:
            self.__cursor = self.__cursor.esq

    def descerDireita(self):
        if self.__cursor is not None and self.__cursor.dir is not None:
            self.__cursor = self.__cursor.dir
    
    def resetCursor(self):
        self.__cursor = self.__raiz

    def __ehFolha(self, no:'No'):
        return no.esq == None and no.dir == None

    def removeEsq(self)->any:
        if self.__cursor is not None and self.__cursor.esq is not None and self.__ehFolha(self.__cursor.esq):
            carga = self.__cursor.esq.carga
            self.__cursor.esq = None
            self.__tamanho -= 1
            return carga
        else:
            return None

    def removeDir(self)->any:
        if self.__cursor is not None and self.__cursor.dir is not None and self.__ehFolha(self.__cursor.dir):
            carga = self.__cursor.dir.carga
            self.__cursor.dir = None
            self.__tamanho -= 1
            return carga
        else:
            return None

    def addEsq(self, carga:any)->bool:
        if self.__cursor is not None and self.__cursor.esq is None:
            self.__cursor.esq = No(carga)
            self.__tamanho += 1
            return True
        else:
            return False
    
    def addDir(self, carga)->bool:
        if self.__cursor is not None and self.__cursor.dir is None:
            self.__cursor.dir = No(carga)
            self.__tamanho += 1
            return True
        else:
            return False

    def __len__(self):
        return self.__tamanho
    
    def altura(self):
        return self.__altura(self.__raiz) - 1

    def __altura(self, no):
        if no is None:
            return 0
        return 1 + max(self.__altura(no.esq), self.__altura(no.dir))

    def leafs(self):
        return self.__leafs(self.__raiz)
    
    def __leafs(self, no):
        if no is None:
            return 0
        if no.esq is None and no.dir is None:
            return 1
        return self.__leafs(no.esq) + self.__leafs(no.dir)
    
    def count(self):
        return self.__count(self.__raiz)
    
    def __count(self, no):
        if no is None:
            return 0
        return 1 + self.__count(no.esq) + self.__count(no.dir)
    
    def busca(self, chave:any)->bool:
        return self.__busca(chave, self.__raiz)
    
    def __busca(self, chave:any, no:No):
        if no is None:
            return False
        if chave == no.carga:
            return True
        if self.__busca(chave,no.esq):
            return True
        else:
            return self.__busca(chave,no.dir)
        
    def go(self, chave:any )->any: # retorna a carga
        no = self.__go(chave,self.__raiz)
        if no is not None:
            return no.carga
        else:
            return None
    
    def __go(self, chave:int, no:No)->No:
        if no is None:
            return None
        if chave == no.carga:
            return no       
        recuperado = self.__go(chave,no.esq)
        if recuperado is not None:
            return recuperado
        else:
            return self.__go(chave,no.dir)

if __name__ == "__main__":
    a = ArvoreBinaria()
    a.criaRaiz(1)
    a.addEsq(2)
    a.addDir(3)
    a.descerEsquerda()
    a.addDir(4)
    a.resetCursor()
    a.descerDireita()
    a.addEsq(5)
    a.addDir(6)
    a.descerDireita()
    a.addEsq(7)

    print('Pré-ordem:')
    a.preordem()
    print('')
    print('Altura:')
    print(a.altura())
    print('Quantidade de nós:')
    print(a.count())
    print('Quantidade de folhas:')
    print(a.leafs())
    # print('')
    # print('Em ordem:')
    # a.emordem()
    # print('')
    # print('Pós-ordem:')
    # a.posordem()