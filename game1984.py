# Projeto: RPG com base no Livro 1984 de George Orwell
# Data Início: 08/05/2025.
# Versão 1.0.2025.05
# Autor: André Rogério Bononi e Filhos
# Contato: arbononi@gmail.com

import os
import locale
import yaml
from os import system as clear_screen
from models.scripts import Opcao, Script, Capitulo
from utils import userfunctions
from layouts.layouts import tela_principal, rosto, tela_capitulos, legenda_rosto
from config import lin_terminal, col_terminal, lin_message
from controllers.engine_texto_controller import EngineTexto

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
_app= None

def set_size_terminal(lines=30, columns=100):
    os.system(f"mode con: cols={columns} lines={lines}")
    
def iniciar():
    userfunctions.desenhar_tela(layout=tela_principal, line_loop=4, stop_loop=lin_message - 1)
    str_data_atual = userfunctions.formatar_data(userfunctions.get_data_atual(), True, True)
    userfunctions.exibir_conteudo(str_data_atual, lin=2, col=104)
    script = carregar_scripts("scripts/script_capitulo_1.yaml")
    _app = EngineTexto(script=script)
    _app.iniciar("capitulo1")
    

def carregar_scripts(path: str) -> Script:
    with open(path, 'r', encoding='utf-8') as file:
        raw_yaml = yaml.safe_load(file)

    raiz = next(iter(raw_yaml))
    dados = raw_yaml[raiz]

    script = Script()

    for capitulo_id, conteudo in dados.items():
        linhas = {}
        acoes = {}
        opcoes = []

        for chave, valor in conteudo.itens():
            if chave.startswith('lin_'):
                linhas[chave] = valor
            elif chave.startswith('opcoes'):
                for opc in valor:
                    texto = opc['texto']
                    acao = opc['acao']
                    proximo = opc['proximo']
                    opcoes.append(Opcao(texto=texto, acao=acao, proximo=proximo))
            elif isinstance(valor, str):
                acoes[chave] = valor
        
        capitulo = Capitulo(
            id=capitulo_id,
            linhas=linhas,
            acoes=acoes,
            opcoes=opcoes
        )

        script.capitulos[capitulo_id] = capitulo
    return script

if __name__ == "__main__":
    os.system("chcp 65001 > nul")
    clear_screen("cls")
    set_size_terminal(lin_terminal, col_terminal)
    iniciar()
    clear_screen("cls")
