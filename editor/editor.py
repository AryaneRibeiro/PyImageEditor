from historico.historico import Historico
from imagem.imagem import Imagem
from filtros.nitidez import Nitidez
from filtros.suavizacao import Suavizacao

import cv2

class Editor():

    def lerImagem(self, caminho):
        self.caminho = Imagem(caminho)
        self.historico.adicionarImagem(self.caminho.imagem)
        self.historico = Historico()


    def salvarImagem(self):
        salvar = cv2.imwrite("images/resultados/img_01.jpg", self.historico.obterImagemAtual())

        if salvar:
            print("Imagem salva com sucesso!")
        else:
            print("Falhar ao salvar")

    def visualizarImagem(self):
        imagem = cv2.resize(self.historico.obterImagemAtual(), (512,512))
        cv2.imshow('Edição', imagem )
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def addFiltro(self):
        filtro = int(input("Escolha um filtro para adicionar: \n (1) - Suavilização \n (2) - Nitidez \n"))

        match filtro:
            case 1:
                suavizacao = Suavizacao()
                self.historico.adicionarImagem(suavizacao.aplicar(self.historico.obterImagemAtual()))
                print("Adicionando suavilização")   
            case 2:
                print("Adicionando nitidez")
                nitidez = Nitidez()
                self.historico.adicionarImagem(nitidez.aplicar(self.historico.obterImagemAtual()))
                print("Nitidez aplicada")
            case _:
                print("Opção inválida")


    def nModificacoes(self):
        return self.historico.numeroModicacoes()
        
    