import config
from time import sleep
from layouts.layouts import tela_capitulos, rosto
from utils.userfunctions import limpar_linha, limpar_tela, desenhar_tela, exibir_conteudo, exibir_mensagem, esperar_tecla
from utils.userfunctions import posicionar_cursor, desenhar_imagem_nao_mapeada

class CapitulosView:
    def __init__(self):
        pass

    def iniciar(self):
        limpar_tela()
        desenhar_tela(layout=tela_capitulos, line_loop=4, stop_loop=config.lin_message - 1)
        self.linha_atual_textos = 4
        self.col_atual_textos = 4
        self.linha_atual_acoes = 4
        self.col_atual_acoes = 82

    def exibir_narrativa(self, texto):
        self.col_atual_textos = 4
        for letra in texto:
            exibir_conteudo(letra, self.linha_atual_textos, self.col_atual_textos)
            self.col_atual_textos += 1
            sleep(0.01)
        self.linha_atual_textos += 1
        self.col_atual_textos = 4
        if self.linha_atual_textos == config.lin_message - 1:
            _ = exibir_mensagem("Pressione qualquer tecla para continuar...", wait_key=True)
            self.linha_atual_textos = 4
            limpar_tela(start=4, stop=config.lin_message - 1, col=self.col_atual_textos, size=75)

    def mostrar_opcoes(self, opcoes):
        if not opcoes:
            return
        limpar_tela(start=4, stop=config.lin_message - 1, col=self.col_atual_acoes - 1, size=config.col_terminal - self.col_atual_acoes)
        self.linha_atual_acoes = 4
        self.col_atual_acoes = 82
        for i, opcao in enumerate(opcoes):
            exibir_conteudo(f"{i + 1}. {opcao['texto']}", self.linha_atual_acoes, self.col_atual_acoes)
            self.linha_atual_acoes += 1

    def solicitar_acao(self):
        return exibir_mensagem("O que deseja fazer?", wait_key=True)

    def desenhar_poster(self, args=None):
        self.col_atual_acoes = 82
        limpar_tela(start=4, stop=config.lin_message - 1, col=self.col_atual_acoes - 1, size=config.col_terminal - self.col_atual_acoes)
        desenhar_imagem_nao_mapeada(rosto, 4, 82)
        self.linha_atual_acoes += len(rosto)
        if not args:
            return
        for linha in args:
            if isinstance(linha, dict):
                texto = linha.get('texto', '')
            else:
                texto = linha
            for letra in texto:
                exibir_conteudo(letra, self.linha_atual_acoes, self.col_atual_acoes)
                self.col_atual_acoes += 1
                sleep(0.06)
            self.linha_atual_acoes += 1
            self.col_atual_acoes = 82
        _ = exibir_mensagem("Pressione qualquer tecla pra continuar...", wait_key=True)
        self.col_atual_acoes = 82
        limpar_tela(start=4, stop=config.lin_message - 1, col=self.col_atual_acoes - 1, size=config.col_terminal - self.col_atual_acoes)

        
