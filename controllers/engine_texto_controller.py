from models.scripts import Script
from views.scripts_view import ScriptView

class EngineTexto:
    _app = None

    def __init__(self, script: Script):
        self._app = ScriptView(script)

    
    def iniciar(self, capitulo_id: str):
        self._app._capitulo_atual = self._app._script.capitulos.get(capitulo_id)
        self._app._linha_atual = "lin_01"
        self._app.executar_capitulo()

    

