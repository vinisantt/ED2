class No:
 
    def __init__(self, valor):
        self.info = valor
        self.esq = None
        self.dir = None
        self.fb = 0

    def rotacao_dir(self,R):
        p = self
        q = p.esq
        temp = q.dir
        R.esq = q
        q.dir = p
        p.esq = temp
        p.FB()
        q.FB()

    def rotacao_esq(self,R):
        p = self
        q = p.dir
        temp = q.esq
        R.dir = q
        q.esq = p
        p.dir = temp
        p.FB()
        q.FB()

    def rotacao_dir_raiz(self,R):
        p = self
        q = p.esq
        temp = q.dir
        R.dir = q
        q.dir = p
        p.esq = temp
        p.FB()
        q.FB()

    def rotacao_esq_raiz(self,R):
        p = self
        q = p.dir
        temp = q.esq
        R.esq = q
        q.esq = p
        p.dir = temp
        p.FB()
        q.FB()

    def FB(self):
        if self.dir != None and self.esq != None:
            self.fb = self.dir.altura() - self.esq.altura()
        elif self.dir != None or self.esq != None:
            if self.esq != None:
                self.fb = -self.esq.altura()
            else:
                self.fb = self.dir.altura()
        else:
            self.fb = 0

    def insere(self, valor):
         if valor < self.info:
            if self.esq == None:
                 self.esq = No(valor)
                 self.FB()
            else:
                 self.esq.insere(valor)
                 if self.esq.fb == -2:
                     if self.esq.esq.fb == -1:
                         self.esq.rotacao_dir(self)
                     else:
                         self.esq.esq.rotacao_esq(self.esq)
                         self.esq.rotacao_dir(self)
                 elif self.esq.fb == 2:
                     if self.esq.dir.fb == 1:
                         self.esq.rotacao_esq(self)
                     else:
                         self.esq.dir.rotacao_dir_raiz(self.esq)
                         self.esq.rotacao_esq_raiz(self)
                 self.FB()
         else:
             if self.dir == None:
                 self.dir = No(valor)
                 self.FB()
             else:
                 self.dir.insere(valor)
                 if self.dir.fb == 2:
                     if self.dir.dir.fb == 1:
                         self.dir.rotacao_esq(self)
                     else:
                         self.dir.dir.rotacao_dir(self.dir)
                         self.dir.rotacao_esq(self)
                 elif self.dir.fb == -2:
                     if self.dir.esq.fb == -1:
                         self.esq.rotacao_dir(self)
                     else:
                         self.dir.esq.rotacao_esq_raiz(self.dir)
                         self.dir.rotacao_dir_raiz(self)
                 self.FB()

    def busca(self,valor):
        if valor == self.info:
            return True
        elif valor < self.info:
            if self.esq ==None:
                return False
            else:
                return  self.esq.busca(valor)
        else:
            if self.dir ==None:
                return False
            else:
                return self.dir.busca(valor)

    def preOrdem(self):
        print('('+str(self.info)+')',end='')
        print(self.fb)
        if self.esq != None:
            self.esq.preOrdem()
        if self.dir != None:
            self.dir.preOrdem()

    def inOrdem(self):
        if self.esq != None:
            self.esq.inOrdem()
        print(self.info,end='')
        if self.dir != None:
            self.dir.inOrdem()

    def posOrdem(self):
        if self.esq != None:
            self.esq.posOrdem()
        if self.dir != None:
            self.dir.posOrdem()
        print(self.info,end='')

    def soma(self):
        total=self.info
        if self.esq != None:
            total+=self.esq.soma()
        if self.dir != None:
            total+=self.dir.soma()
        return total

    def somaFolhas(self):
        total=0
        if self.esq==None and self.dir==None:
            total=self.info
        if self.esq != None:
            total+=self.esq.somaFolhas()
        if self.dir != None:
            total+=self.dir.somaFolhas()
        return total

    def printFolhas(self):
        if self.esq != None:
            self.esq.printFolhas()
        if self.esq==None and self.dir==None:
            print(self.info,end='')
        if self.dir != None:
            self.dir.printFolhas()

    def printFolhasRevers(self):
        if self.dir != None:
            self.dir.printFolhas()
        if self.esq==None and self.dir==None:
            print(self.info,end='')
        if self.esq != None:
            self.esq.printFolhas()


    def nivelNo(self,valor):
        nivel=1
        if valor < self.info:
            nivel+=self.esq.nivelNo(valor)
        elif valor > self.info:
            nivel+=self.dir.nivelNo(valor)
        return nivel

    def altura(self):
        alturaesq=1
        alturadir=1
        if self.esq != None:
            alturaesq += self.esq.altura()
        if self.dir != None:
            alturadir += self.dir.altura()
        return max(alturaesq,alturadir)

    def alturaNo(self,valor):
        if valor==self.info:
            alturaesq=1
            alturadir=1
            if self.esq != None:
                alturaesq += self.esq.alturaNo(self.esq.info)
            if self.dir != None:
                alturadir += self.dir.alturaNo(self.dir.info)
            return max(alturaesq,alturadir)
        elif valor > self.info and self.dir != None:
            return self.dir.alturaNo(valor)
        elif valor < self.info :
            return self.esq.alturaNo(valor)


    def maisDireita(self):
        if self.dir != None:
            return self.dir.maisDireita()
        else:
            return self.info

    def maisEsquerda(self):
        if self.esq != None:
            return self.esq.maisEsquerda()
        else:
            return self.info

class Tree:

    def __init__(self):
        self.raiz = None

    def insere(self, valor):
        if self.raiz == None:
            self.raiz = No(valor)
        else:
            self.raiz.insere(valor)
            self.raiz.FB()
            if self.raiz.fb == -2:
                if self.raiz.esq.fb == -1:
                    self.rotacao_dir_raiz()
                else:
                    self.raiz.esq.rotacao_esq_raiz(self.raiz)
                    self.rotacao_dir_raiz()
            elif self.raiz.fb == 2:
                if self.raiz.dir.fb == 1:
                    self.rotacao_esq_raiz()
                else:
                    self.raiz.dir.rotacao_dir_raiz(self.raiz)
                    self.rotacao_esq_raiz()
            self.raiz.FB()

    def rotacao_dir_raiz(self):
        p = self.raiz
        q = p.esq
        temp = q.dir
        self.raiz = q
        q.dir = p
        p.esq = temp
        p.FB()
        q.FB()

    def rotacao_esq_raiz(self):
        p = self.raiz
        q = p.dir
        temp = q.esq
        self.raiz = q
        q.esq = p
        p.dir = temp
        p.FB()
        q.FB()

    def busca(self,valor):
        if self.raiz==None:
            return False
        else:
            return self.raiz.busca(valor)

    def preOrdem(self):
        if self.raiz !=None:
            self.raiz.preOrdem()

    def inOrdem(self):
        if self.raiz != None:
            self.raiz.inOrdem()

    def posOrdem(self):
        if self.raiz !=None:
            self.raiz.posOrdem()

    def soma(self):
        if self.raiz != None:
            return self.raiz.soma()

    def somaFolhas(self):
        if self.raiz != None:
            return self.raiz.somaFolhas()

    def printFolhas(self):
        if self.raiz != None:
            self.raiz.printFolhas()

    def nivelNo(self,valor):
        if self.raiz != None:
            return self.raiz.nivelNo(valor)

    def altura(self):
        if self.raiz != None:
            return self.raiz.altura()

    def maisDireita(self):
        if self.raiz !=None:
            return self.raiz.maisDireita()

    def maisEsquerda(self):
        if self.raiz != None:
            return self.raiz.maisEsquerda()

    def alturaNo(self,valor):
        if self.raiz != None:
            return self.raiz.alturaNo(valor)