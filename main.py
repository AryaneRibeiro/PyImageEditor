from core.imagem import Imagem
from filtro.filtros import Filtros

# 1. Cria objeto Imagem → ele cria sozinho o Historico e o SalvarImagem
minha_img = Imagem("/home/aryane/Documentos/programacao/python/editorImagens/images/entrada/parque.jpeg")

# 2. Cria objeto de Filtros ligado à imagem
filtro = Filtros(minha_img)

# 3. Aplica filtros
filtro.tonsCinza()
filtro.desfoque()
filtro.contraste(1.2, 30)

# 4. Usa tudo

minha_img.desfazer()
