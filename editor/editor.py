from historico.historico import Historico
from imagem.imagem import Imagem
from filtros.nitidez import Nitidez

class Editor():
    def __init__(self, caminho):
        self.imagem = Imagem(caminho)
        self.historico = Historico()

    def salvar(self):
        self.imagem.salvarImagem()

    def mostrarImagem(self):
        self.imagem.mostrarImagem()

    def addFiltro(self):
        filtro = int(input("Escolha um filtro para adicionar: \n (1) - Suavilização \n (2) - Nitidez \n"))

        match filtro:
            case 1:
                print("Adicionando suavilização")   

            case 2:
                print("Adicionando nitidez")
                nitidez = Nitidez()
                self.imagem.imagem = nitidez.aplicarNitidez(self.imagem.imagem)
                print("Nitidez aplicada")
            case _:
                print("Opção inválida")

