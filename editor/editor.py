from historico.historico import Historico
from imagem.RepositorioImagem import RepositorioImagem
from filtros.nitidez import Nitidez

import cv2

class Editor():
    def __init__(self, caminho):
        self.imagem = RepositorioImagem(caminho)
        self.historico = Historico()
        self.historico.addHistorico(self.imagem)

    def addFiltro(self):
        filtro = int(input("Escolha um filtro para adicionar: \n (1) - Suavilização \n (2) - Nitidez \n"))

        match filtro:
            case 1:
                print("Adicionando suavilização")   

            case 2:
                print("Adicionando nitidez")
                nitidez = Nitidez()
                self.imagem.imagem = nitidez.aplicar(self.imagem.imagem)   
                self.historico.addHistorico(self.imagem.imagem)
                print("Nitidez aplicada")
            case _:
                print("Opção inválida")

    def mostrarImagem(self):
       self.historico.imgAtual()

    def modicacoes(self):
        return self.historico.qntDeModificacao()

    def salvarImagem(self):
        RepositorioImagem.salvarImagem(self.historico.returnImgAtual())