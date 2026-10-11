import cv2

class VisualizarImagem():
    def exibirImagemAtual(self, imagemSemAlteracao, imagemFinal):
            imagemSemAlteracao = cv2.resize(imagemSemAlteracao, (512, 512))
            imagemFinal = cv2.resize(imagemFinal, (512, 512))
            
            imagemEditada = cv2.hconcat([imagemSemAlteracao, imagemFinal])
            cv2.imshow("Resultado final", imagemEditada)
            cv2.waitKey(0)
            cv2.destroyAllWindows()