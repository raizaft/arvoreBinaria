class No:
    def __init__(self,carga:any):
        self.carga = carga
        self.esq = None
        self.dir = None

    def __str__(self):
        return str(self.carga)

class ArvoreBinariaDeBusca:        
    def __init__(self):
        self.__raiz = None

    def estaVazia(self)->bool:
        return self.__raiz == None
    
    def getRaiz(self)->any:
        return self.__raiz.carga if self.__raiz is not None else None


    def preordem(self):
        self.__preordem(self.__raiz)

    def __preordem(self, no:No):
        if no is not None:
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
    
    def desordem(self):
        return self.__desordem(self.__raiz)
    
    def __desordem(self, no):
        if no is not None:
            self.__desordem(no.dir)
            print(f'{no.carga}',end=' ')
            self.__desordem(no.esq)


    def posordem(self):
        self.__posordem(self.__raiz)

    def __posordem(self, no):
        if no is not None:
            self.__posordem(no.esq)
            self.__posordem(no.dir)
            print(f'{no.carga}',end=' ')
    
    def esvaziar(self):
        cursor = self.__raiz
        if cursor != None:
            if cursor.esq != None:
                cursor.esq = None
            elif cursor.dir != None:
                cursor.dir = None
            self.__raiz = None
        else:
            return
    
    def remove(self, chave:any)->any:
        carga = self.busca(chave)
        if carga is not None:
            self.__remove(chave, self.__raiz)
            return carga
        else:
            return None
        
    def __remove(self, key:any, no:No):
        if no is None: 
            return no
    
        if key < no.carga:
            no.esq = self.__remove(key, no.esq)

        elif(key > no.carga):
            no.dir = self.__remove(key, no.dir) 
        
        else:
            if no.esq is None : 
                temp = no.dir  
                no = None 
                return temp

            elif no.dir is None :
                temp = no.esq  
                no = None
                return temp 
        
        temp = self.__minValueNode(no.dir) 
        no.carga = temp.carga
        no.dir = self.__remove(temp.carga, no.dir )
        return no
    
    def __minValueNode(self, no:'No')->'No':
        current = no 
        while(current.esq is not None): 
            current = current.esq  
        return current
    
    def __maxValueNode(self, no:'No')->'No':
        current = no 
        while(current.dir is not None): 
            current = current.dir
        return current

    def add(self, carga:any)->bool:
        if(self.__raiz == None):
            self.__raiz = No(carga)
        else:
            self.__add(carga, self.__raiz)   

    def __add(self, carga, no):
        if (carga < no.carga):
            if(no.esq != None):
                self.__add(carga, no.esq)
            else:
                no.esq = No(carga)
        else:
            if(no.dir != None):
                self.__add(carga, no.dir)
            else:
                no.dir = No(carga)

    def __count(self, no:'No')->int:
        if no is None:
            return 0
        else:
            return 1 + self.__count(no.esq) + self.__count(no.dir)

    def __len__(self):
        return self.__count(self.__raiz)

    def busca(self, chave:any)->any:
        if(self.__raiz != None):
            no = self.__busca(chave, self.__raiz)
            return no.carga if no is not None else None
        else:
            return None
    
    def __busca(self, chave:any, no:No):
        if (chave == no.carga):
            return no
        elif (chave < no.carga and no.esq != None):
            return self.__busca(chave, no.esq)
        elif (chave > no.carga and no.dir != None):
            return self.__busca(chave, no.dir)
        else:
            return None
        
    def frequencia(self, k):
        if(self.__raiz != None):
            f = self.__frequencia(self.__raiz, k)
            return f'{k}: {f}'
        else:
            return 0
    
    def __frequencia(self, no, k):
        if k == no.carga:
            if no.esq != None:
                return 1 + self.__frequencia(no.esq, k)
            elif no.dir != None:
                return 1 + self.__frequencia(no.dir, k)
            else:
                return 1
        else:
            if k < no.carga and no.esq != None:
                return self.__frequencia(no.esq, k)
            elif k > no.carga and no.dir != None:
                return self.__frequencia(no.dir, k)
            else:
                return 0

    
if __name__ == "__main__":
    a = ArvoreBinariaDeBusca()
    a.add("raiza")
    a.add("linda")
    a.add("perfeita")
    print(a.frequencia("a"))
    