# Projeto: RPG com base no Livro 1984 de George Orwell
# Data Início: 08/05/2025.
# Versão 1.0.2025.05
# Autor: André Rogério Bononi e Filhos
# Contato: arbononi@gmail.com

import os
import locale
from os import system as clear_screen
from utils import userfunctions
from layouts.layouts import tela_principal, rosto, tela_capitulos, legenda_rosto
from config import lin_terminal, col_terminal, lin_message
from controllers.narrativa_controller import NarrativaController

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def set_size_terminal(lines=30, columns=100):
    os.system(f"mode con: cols={columns} lines={lines}")
    
def iniciar():
    userfunctions.desenhar_tela(layout=tela_principal, line_loop=4, stop_loop=lin_message - 1)
    str_data_atual = userfunctions.formatar_data(userfunctions.get_data_atual(), True, True)
    userfunctions.exibir_conteudo(str_data_atual, lin=2, col=104)
    _ = userfunctions.exibir_mensagem("Aguarde... Carregando Roteiros...")
    userfunctions.limpar_linha()
    _app = NarrativaController()
    _app.iniciar()

if __name__ == "__main__":
    os.system("chcp 65001 > nul")
    clear_screen("cls")
    set_size_terminal(lin_terminal, col_terminal)
    iniciar()
    clear_screen("cls")
