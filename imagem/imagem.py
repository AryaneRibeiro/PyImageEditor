import cv2

class Imagem:

    def __init__(self, caminho):
        self.imagem = cv2.imread(caminho)

        if self.imagem is None:
            raise ValueError("Erro ao enviar imagem")

        print("Imagem carregada com sucesso!")

    def salvarImagem(self):
        cv2.imwrite("imagemModificada.png", self.imagem)
        print("Salva com sucesso!")


    def mostrarImagem(self):
        cv2.imshow("imagem",self.imagem)
        cv2.waitKey(0)
        cv2.destroyAllWindows()