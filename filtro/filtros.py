import cv2
import numpy as np

class Filtros:

    def __init__(self, objImagem ):
        self.imagem = objImagem

    def tonsCinza(self):
        mod = cv2.cvtColor(self.imagem.imgAtual, cv2.COLOR_BGR2GRAY)
        self.imagem.aplicarAlteracoes(mod)

    def tamanhoImagem(self, altura, largura):
        mod = cv2.resize(self.imagem.imgAtual, (largura, altura))
        self.imagem.aplicarAlteracoes(mod) 

    def desfoque(self):
        mod = cv2.blur(self.imagem.imgAtual, (5,5))
        self.imagem.aplicarAlteracoes(mod) 
        
    def nitidez(self):
        kernel = np.array([
            [0, -1, 0],
            [-1, 5, -1],
            [0, -1, 0],
        ])
        mod = cv2.filter2D(self.imagem.imgAtual, -1, kernel)
        self.imagem.aplicarAlteracoes(mod) 
       
    def contraste(self, contraste= 1.0, brilho=50): # Aplha controla o contraste e o beta o brilho
        mod = cv2.convertScaleAbs(self.imagem.imgAtual, alpha=contraste, beta=brilho)
        self.imagem.aplicarAlteracoes(mod) 