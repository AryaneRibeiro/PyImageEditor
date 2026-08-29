import cv2
import numpy as np

from imagemBase.imagemBase import ImagemBase

class Filtros(ImagemBase):

    def tonsCinza(self):
        mod = cv2.cvtColor(self.historico[-1], cv2.COLOR_BGR2GRAY)
        self.historico.append(mod) 

    def tamanhoImagem(self, altura, largura):
        mod = cv2.resize(self.historico[-1], (altura, largura))
        self.historico.append(mod) 

    def desfoque(self):
        mod = cv2.blur(self.historico[-1], (5,5))
        self.historico.append(mod) 
        
    def nitidez(self):
        kernel = np.array([
            [0, -1, 0],
            [-1, 5, -1],
            [0, -1, 0],
        ])
        mod = cv2.filter2D(self.historico[-1], -1, kernel)
        self.historico.append(mod) 
       
    def contraste(self, contraste= 1.0, brilho=50): # Aplha controla o contraste e o beta o brilho
        mod = cv2.convertScaleAbs(self.historico[-1], alpha=contraste, beta=brilho)
        self.historico.append(mod) 