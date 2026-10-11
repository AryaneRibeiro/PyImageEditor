from editor.editor import Editor

imagem = Editor("images/entrada/img_02.jpg")

imagem.addFiltro()
print(f'Modificações: {imagem.nModificacoes()}')

imagem.salvarImagem()

imagem.mostrarImagem()
