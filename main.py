from editor.editor import Editor


imagem = Editor("/home/aryane/Documentos/programacao/python/editorImagens/images/entrada/parque.jpeg")

imagem.addFiltro()
imagem.mostrarImagem()
print(f'Modificações: {imagem.modicacoes()}')