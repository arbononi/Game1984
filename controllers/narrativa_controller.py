from database.banco import Banco
from views.capitulos_view import CapitulosView
from utils.userfunctions import exibir_mensagem

class NarrativaController:
    _view = None
    def __init__(self):
        self._view = CapitulosView()
        self.capitulo_atual = "capitulo1"
        self.linha_atual = "lin_01"
        self.acoes_automatcias = {
            "desenhar_poster" : self._view.desenhar_poster
        }

    def iniciar(self):
        self._view.iniciar()
        
        while True:
            cap = Banco._model.get_capitulo(self.capitulo_atual)
            conteudo = cap.obter_linha(self.linha_atual)

            if isinstance(conteudo, dict):
                texto = conteudo.get('texto', '')
                opcoes = conteudo.get('opcoes', [])
            else:
                texto = conteudo
                opcoes = []

            self._view.exibir_narrativa(texto)
            self._view.mostrar_opcoes(opcoes)

            if not opcoes:
                proxima = self.proxima_linha(self.linha_atual, cap.linhas)
                if proxima is None:
                    exibir_mensagem("Fim do capítulo!", wait_key=True)
                    break
                self.linha_atual = proxima
                continue

            entrada = self._view.solicitar_acao()

            try:
                escolha = int(entrada) - 1
                if 0 <= escolha < len(opcoes):
                    acao = opcoes[escolha]['acao']
                    if isinstance(acao, dict):
                        auto = acao.get("auto")
                        destino = acao.get("destino")
                        proxima = acao.get('proximo', self.linha_atual)
                        if auto:
                            if destino:
                               argumentos = self.get_argumentos(destino, proxima, cap)
                            self.executar_acao_automatica(auto, argumentos)
                        if acao['tipo'] == 'pular':
                            self.linha_atual = acao.get('proximo', self.linha_atual)
                            continue
                        if destino:
                            idx = cap.listar_linhas().index(destino)
                            fim = cap.listar_linhas().index(proxima)
                            for i in range(idx, fim):
                                linha = cap.obter_linha(cap.listar_linhas()[i])
                                if isinstance(linha, dict):
                                    texto = linha.get('texto', '')
                                    opcoes = linha.get('opcoes', [])
                                else:
                                    texto = linha
                                    opcoes = []
                                self._view.exibir_narrativa(texto)
                            self.linha_atual = proxima
                    else:
                        conteudo = cap.obter_linha(acao)
                        if isinstance(conteudo, dict):
                            texto = conteudo.get('texto', '')
                            opcoes = conteudo.get('opcoes', [])
                        else:
                            texto = conteudo
                            opcoes = []
                        self.view.exibir_narrativa(texto)
                else:
                    _ = exibir_mensagem("Escolha inválida! Tente novamente!", wait_key=True)
            except ValueError:
                _ = exibir_mensagem("Entrada inválida! Escolha o número da opção", wait_key=True)

    def proxima_linha(self, atual, linhas):
        chaves = list(linhas.keys())
        try:
            idx = chaves.index(atual)
            return chaves[idx + 1] if idx + 1 < len(chaves) else None
        except ValueError:
            return None
        
    def get_argumentos(self, destino, proxima, cap):
        idx = cap.listar_linhas().index(destino)
        fim = cap.listar_linhas().index(proxima)
        args = []
        for i in range(idx, fim):
            linha = cap.obter_linha(cap.listar_linhas()[i])
            if linha:
               args.append(linha)
        return args
            
    def executar_acao_automatica(self, nome_acao, args=None):
        if isinstance(nome_acao, list):
            for nome in nome_acao:
                self.executar_acao_automatica(nome, args)
            return
        
        acao = self.acoes_automatcias.get(nome_acao)
        if callable(acao):
            acao(args)
        else:
            exibir_mensagem(f"[WARN] Ação automática desconhecida: {nome_acao}")