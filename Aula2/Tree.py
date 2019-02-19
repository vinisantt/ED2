class Tree:
      def __init__(self):
            self.raiz = None

      def inOrdem(self):
            if self.raiz != None:
                  return self.raiz.inOrdem()

      def nivel(self, valor):
            if self.raiz != None:
                  return self.raiz.nivel(valor)

      def insere(self, valor):
            if self.raiz == None:
                  self.raiz = No(valor)
            else:
                  self.raiz.insere(valor)
                      
      def balanceia_dir(self):
            if self.raiz != None:
                  return self.raiz.balanceia_dir()

      def balanceia_esq(self):
            if self.raiz != None:
                  return self.raiz.balanceia_esq()
        
      def altura(self):
            if self.raiz != None:
                  return self.raiz.altura()

      def calcfb(self):
            if self.raiz != None:
                  return self.raiz.calcfb()

      def achafb(self,valor):
            if self.raiz !=None:
                  return self.raiz.achafb(valor)
          
class No:
      def __init__(self, valor):
            self.info = valor
            self.esq = None
            self.dir = None
            self.fb = 0

      def insere(self, valor):
            
            if valor <= self.info:
                  if self.esq == None:
                        self.esq = No(valor)
                        self.fb = self.calcfb()
                        
                        

                  else:
                        self.esq.insere(valor)
                        self.fb = self.calcfb()

            else:
                  if self.dir == None:
                        self.dir = No(valor)
                        self.fb = self.calcfb()
                        

                  else:
                        self.dir.insere(valor)
                        self.fb = self.calcfb()
                  
            
              

      def achafb(self,valor):
            if valor == self.info:
                  print("FB de",valor,"é:",self.fb)
                  
            else:
                  print("entrou aqui")
                  if valor < self.info:
                        print("entrou aqui esquerda")
                        self.esq.achafb(valor)
                  else:
                        print("entrou aqui direita")
                        self.dir.achafb(valor)
      
      def calcfb(self):
            if self.dir != None and self.esq != None:
                  return 0
            else:
                  if self.dir == None and self.esq != None:
                        return - self.esq.altura()
                  elif self.dir != None and self.esq == None:
                        return self.dir.altura() 
                  else:
                        return self.dir.altura() - self.esq.altura()


      def altura(self):
            hesq=hdir=0
            if self.esq!=None:
                  hesq=self.esq.altura()
            if self.dir!=None:
                  hdir=self.dir.altura()
            return 1 + max(hesq,hdir)


      def inOrdem(self):
            if self.esq != None:
                  self.esq.inOrdem()
            print(self.info)
            if self.dir != None:
                  self.dir.inOrdem()


      def nivel(self, valor):
            ct = 1
            if self.info > valor:
                  if self.info == valor:
                        return ct
                  elif self.esq != None:
                        ct += self.esq.nivel(valor) 
                  elif self.info < valor:
                        if self.info == valor:
                              return ct
                  elif self.dir != None:
                        ct += self.dir.nivel(valor)
            return ct

      #def balanceia_dir(self):
        #METE O CÓDIGO AE
        
      #def balanceia_esq(self):
        #METE O CÓDIGO AE

              

