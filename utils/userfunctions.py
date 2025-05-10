import sys
import msvcrt
from datetime import datetime, date
from config import lin_terminal, col_terminal, lin_message, col_message, size_message_lin

OCULTAR_CURSOR = '\033[?25l'
MOSTRAR_CURSOR = '\033[?25h'

def finalizar_print():
    sys.stdout.flush()

def esperar_tecla(ocultar_cursor: bool=True):
    if ocultar_cursor:
        print(OCULTAR_CURSOR, end="", flush=True)
    tecla = msvcrt.getch().decode("utf-8").upper()
    if ocultar_cursor:
        print(MOSTRAR_CURSOR, end="", flush=True)
    if tecla == "\r":
        tecla = ""
    return tecla

def posicionar_cursor(lin, col):
    sys.stdout.write(f"\033[{lin};{col}H")

def limpar_linha(lin=lin_message, col=col_message, size=size_message_lin, background=False):
    posicionar_cursor(lin, col)
    if background:
        print("_" * size, end="")
    else:
        print(" " * size, end="")
    posicionar_cursor(lin, col)
    finalizar_print()

def exibir_mensagem(mensagem: str, lin=lin_message, col=col_message, skip_line: str="", wait_key: bool=False):
    opcao = ""
    limpar_linha(lin, col, size=size_message_lin)
    posicionar_cursor(lin, col)
    print(mensagem, end=skip_line)
    finalizar_print()
    if wait_key:
        opcao = esperar_tecla()
    return opcao

def exibir_conteudo(conteudo: str, lin: int=lin_message, col: int=col_message, colorir=False):
    posicionar_cursor(lin, col)
    if colorir:
        print(f"\033[38;5;250;48;5;240m{conteudo}\033[0m", end="")
    else:
        print(conteudo, end="")
    finalizar_print()

def limpar_tela(start: int=4, stop: int=29, col: int=col_message, size: int=size_message_lin):
    for lin in range(start, stop):
        posicionar_cursor(lin, col)
        print(" " * size, end="")
    finalizar_print()

def desenhar_tela(layout, line_loop=0, stop_loop=0):
    for config in layout:
        if line_loop == config["lin"] and stop_loop > 0:
            process = True
            while process:
                posicionar_cursor(line_loop, config["col"])
                print(config["value"], end="")
                if line_loop < stop_loop:
                    line_loop += 1
                else:
                    process = False
        else:
            posicionar_cursor(config["lin"], config["col"])
            print(config["value"], end="")
    sys.stdout.flush()

def desenhar_imagem_nao_mapeada(imagem, lin, col):
    for i, linha_texto in enumerate(imagem):
        print(f"\033[{lin + i};{col}H{linha_texto}", end='', flush=True)
        
def get_data_atual():
    return datetime.now().date()

def formatar_data(data: date, exibir_dia_semana=False, antes=False):
    if exibir_dia_semana:
        if antes:
           return data.strftime("%a %d/%m/%Y").upper()
        else:
            return data.strftime("%d/%m/%Y") + " " + data.strftime("%a").upper()
        
    return data.strftime("%d/%m/%Y")

def formatar_data_hora(data: datetime):
    return data.strftime("%d/%m/%Y %H:%M:%S")
