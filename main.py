from fastapi import FastAPI
# Vai na caixa de ferramentas do FastAPI e pega especificamente a ferramenta de redirecionamento
from fastapi.responses import RedirectResponse

# Os Imports dos arquivos dos colaboradores afiliados
import somar
import divisao
import raiz
import fatorarf
import subtrairf

app = FastAPI()

@app.get("/")
def root():
    # Redireciona o Usuário assim que ele abrir a URL, direto para a URL '/docs' com todas as funções
    return RedirectResponse(url="/docs")

print ("Hello Word")

import exponenciarf 

@app.get("/exponenciar")
def rota_exponenciar(num1: float, num2: float):
    resultado = exponenciarf.exponenciar(a, b)
    return {"resultado": resultado}
