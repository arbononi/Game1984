from dataclasses import dataclass, field
from typing import List, Dict, Optional, Union
import yaml

@dataclass
class Opcao:
    texto: str
    acao: Union[str, Dict[str, str]]
    proximo: Optional[str] = None

@dataclass
class Capitulo:
    id: str
    linhas: Dict[str, str] = field(default_factory=dict)
    acoes: Dict[str, str] = field(default_factory=dict)
    opcoes: List[Opcao] = field(default_factory=list)

@dataclass
class Script:
    capitulos: Dict[str, Capitulo] = field(default_factory=dict)
