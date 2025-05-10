import os
import yaml
from models.narrativa import NarrativaModel, Capitulo

class Banco:
    _model = None
    
    def __init__(self):
        pass

    def carregar_arquivo(self, nome_arquivo):
        pasta_scripts = 'scripts'
        
        if not os.path.exists(pasta_scripts):
            raise FileNotFoundError(f"A pasta {pasta_scripts} não foi encontrada no projeto")
        
        # Construa o caminho completo para o arquivo YAML
        caminho_completo = os.path.join(pasta_scripts, nome_arquivo)

        # Verifica se o arquivo existe
        if not os.path.isfile(caminho_completo):
            raise FileNotFoundError(f"O arquivo '{nome_arquivo}' não foi encontrado na pasta '{pasta_scripts}'.")

        with open(caminho_completo, encoding='utf-8') as f:
            dados = yaml.safe_load(f)

        Banco._model = NarrativaModel()
        for cap_nome, conteudo in dados.get("inicio", {}).items():
            linhas = {}
            for k, v in conteudo.items():
                if k.startswith("lin_") or not k.startswith("capitulo"):
                    if isinstance(v, dict) and 'opcoes' in v:
                        # Se tiver opções, vamos tratar cada opção corretamente
                        opcoes = []
                        for opcao in v['opcoes']:
                            acao = opcao.get('acao', {})
                            if isinstance(acao, dict):
                                tipo_acao = acao.get('tipo')
                                if tipo_acao == 'ler':
                                    destino = acao.get('destino')
                                    proximo = acao.get('proximo')
                                    acao['tipo'] = 'ler'
                                    acao['destino'] = destino
                                    acao['proximo'] = proximo
                                elif tipo_acao == 'pular':
                                    proximo = acao.get('proximo')
                                    acao['tipo'] = 'pular'
                                    acao['proximo'] = proximo
                            opcoes.append(opcao)
                        v['opcoes'] = opcoes
                    linhas[k] = v
            cap = Capitulo(cap_nome, linhas)
            Banco._model.adicionar_capitulo(cap)
