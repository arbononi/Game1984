from models.scripts import Opcao, Script, Capitulo
from utils.userfunctions import limpar_linha, limpar_tela, desenhar_tela, posicionar_cursor, esperar_tecla
from utils.userfunctions import exibir_conteudo, exibir_mensagem, lin_message
from layouts.layouts import tela_capitulos

class ScriptView():
    _script = None
    _capitulo_atual = None
    _linha_atual = None

    def __init__(self, script: Script):
        self._script = script

    def iniciar(self):
        desenhar_tela(tela_capitulos, line_loop=4, stop_loop=lin_message - 1)

    def executar_capitulo(self):
        if not self._capitulo_atual:
            exibir_mensagem("Capítulo não encontrado!", wait_key=True)
            return
        lin = 4
        col = 4
        while self._linha_atual and self._linha_atual in self._capitulo_atual.linhas:
            exibir_conteudo(self._capitulo_atual.linhas[self._linha_atual], lin=lin, col=col)
            num = int(self._linha_atual.split('_')[1]) + 1
            proxima = f'lin_{num:02d}'
            self._linha_atual = proxima if proxima in self._capitulo_atual.linhas else None
            lin += 1 if proxima else lin

        _ = esperar_tecla()
            