from historico.historico import Historico
from imagem.RepositorioImagem import RepositorioImagem
from filtros.nitidez import Nitidez
from imagem.visualizadorImagem import VisualizarImagem

class Editor():
    def __init__(self, caminho):
        self.caminho = RepositorioImagem(caminho)
        self.historico = Historico()
        self.historico.adicionarImagem(self.caminho.imagem)

    def addFiltro(self):
        filtro = int(input("Escolha um filtro para adicionar: \n (1) - Suavilização \n (2) - Nitidez \n"))

        match filtro:
            case 1:
                print("Adicionando suavilização")   
            case 2:
                print("Adicionando nitidez")
                nitidez = Nitidez()
                self.historico.adicionarImagem(nitidez.aplicar(self.historico.obterImagemAtual()))
                print("Nitidez aplicada")
            case _:
                print("Opção inválida")

    def mostrarImagem(self):
       visualizar = VisualizarImagem()
       visualizar.exibirImagemAtual(self.caminho.imagem, self.historico.obterImagemAtual())

    def nModificacoes(self):
        return self.historico.numeroModicacoes()

    def salvarImagem(self):
        RepositorioImagem.salvarImagem(self.historico.obterImagemAtual())