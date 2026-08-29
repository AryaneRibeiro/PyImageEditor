import cv2
import numpy as np
import os 

class ImagemBase:
    def __init__(self, imagem):
        self.imagem = cv2.imread(imagem)
        if self.imagem is None:
            raise ValueError(f"Erro ao tentar encontrar imagem no caminho: {imagem}")
        else:
            self.historico = []
            self.historico.append(self.imagem.copy())
              
    def exibirImagem(self):
        cv2.imshow("Imagem original x Imagem modificada", self.historico[-1])
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def salvarImagem(self, nomePasta):
        __pasta = "images/resultados"
        os.makedirs(__pasta, exist_ok=True)
        caminho = os.path.join(__pasta, nomePasta + ".png")
        salvo = cv2.imwrite(caminho, self.historico[-1])
        if salvo is True:
            print(f"Imagem salva em: {caminho}")
        else:
            print(f"Erro ao salvar imagem em:{caminho}")

    def modificaoesFeitas(self):
        print(f'Total de modficações feitas: {len(self.historico) - 1}')

    def desfazer(self):
        if len(self.historico) > 1:
            self.historico.pop()
        else:
            print("Não há modificações para realizar")
        

    def informacoesImagens(self):
        x,y = self.historico[-1].shape
        print(f'Altura: {x}\nLargura: {y}')