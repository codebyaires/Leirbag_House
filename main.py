from fastapi import FastAPI
# Vai na caixa de ferramentas do FastAPI e pega especificamente a ferramenta de redirecionamento
from fastapi.responses import RedirectResponse

# Os Imports dos arquivos dos colaboradores afiliados
import somar
import divisao
import raiz
import fatorarf
import subtrairf
import exponenciarf
import multiplicarf
import math

app = FastAPI()

@app.get("/")
def root():
    # Redireciona o Usuário assim que ele abrir a URL, direto para a URL '/docs' com todas as funções
    return RedirectResponse(url="/docs")

@app.get("/exponenciar")
def exponenciar(a: float, b: float):
    resultado = exponenciarf.exponenciar(a, b)
    return {"resultado": resultado}

@app.get("/subtrair")
def subtrair(a: float, b: float):
    resultado = subtrairf.subtrair(a, b)
    return {"resultado": resultado}

@app.get("/fatorar")
def fatorar(a, b):
    resultado = fatorarf.fatorar(a, b)
    return {"resultado": resultado}

@app.get("/multiplicar")
def multiplicar(a: float, b: float):
    resultado = multiplicarf.multiplicar(a, b)
    return {"resultado": resultado}

@app.get("/somar")
def funsomar(a: float, b: float):
    return somar.somar(a, b)

@app.get("/divisao")
def fundivisao(a: float, b: float):
    return divisao.dividir(a, b)

@app.get("/raiz")
def funraiz(numero: float):
    return math.sqrt(numero)
    


