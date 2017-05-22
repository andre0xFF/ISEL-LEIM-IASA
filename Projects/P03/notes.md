* Python 2.7
* Pygame 32 bit

```python
import sys
import pygame
import site
import pee
import psa


print(sys.executable)
print(sys.version)
print(site.getsitepackages())
```


```python
import psa
import psa.agente from Agente
from psa.accao import Avancar


class AgenteTeste(Agente):
    def executar(self):
        self.actuador.actuar(Avancar())

psa.iniciar("env/amb1.das")
psa.executar(AgenteTeste())
```

PSA - Plataforma de Simulacao de Agentes
PEE - Procura em Estados de Espacos
ECR - Esquemas Comportamentais Reactivos
PDM - Processos de Decisao de Markov

psa.util.dirmov() - lista de angulos
psa.util.mover() - psa.util.mover(estado, ang) - estado (x, y)
psa.util.dist(estado, novoEstado) - distancia entre dois estados
psa.accao.Mover(ang, ang_abs=True) - ang_abs em relacao ao eixo horizontal
