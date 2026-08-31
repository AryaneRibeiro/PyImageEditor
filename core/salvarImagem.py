import os 
import cv2

class SalvarImagem:
    def salvarImagem(self, imagem, nomePasta):
        pasta = "images/resultados"
        os.makedirs(pasta, exist_ok=True)
        caminho = os.path.join(pasta, nomePasta + ".png")
        salvo = cv2.imwrite(caminho, imagem)
        if salvo is True:
            print(f"Imagem salva em: {caminho}")
        else:
            print(f"Erro ao salvar imagem em:{caminho}")