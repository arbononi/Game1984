class Capitulo:
    def __init__(self, nome, linhas):
        self.nome = nome
        self.linhas = linhas

    def obter_linha(self, chave):
        return self.linhas.get(chave, '')
    
    def listar_linhas(self):
        return list(self.linhas.keys())
    
    def obter_opcoes(self, chave):
        """Retorna as opções de uma linha específica"""
        linha = self.obter_linha(chave)
        return linha.get('opcoes', []) if isinstance(linha, dict) else []
    
class NarrativaModel:
    def __init__(self):
        self.capitulos = {}

    def adicionar_capitulo(self, capitulo):
        self.capitulos[capitulo.nome] = capitulo
    
    def get_capitulo(self, nome):
        """Retorna o capítulo pelo nome"""
        return self.capitulos.get(nome)

    def get_proxima_linha(self, capitulo, linha_atual):
        """Retorna a próxima linha de acordo com o fluxo do capítulo"""
        return capitulo.obter_linha(linha_atual)        
