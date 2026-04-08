from fastapi import FastAPI
# Vai na caixa de ferramentas do FastAPI e pega especificamente a ferramenta de redirecionamento
from fastapi.responses import RedirectResponse

# Os Imports dos arquivos dos colaboradores afiliados
import src.somarf as somar
import src.dividirf as dividir
import src.raizf as raiz
import src.fatorarf as fatorar
import src.subtrairf as subtrair
import src.exponenciarf as exponenciar
import src.multiplicarf as multiplicar

# Teste no pull request do pipeline
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
def somar(a: float, b: float):
    return somarf.somar(a, b)

@app.get("/divisao")
def dividir(a: float, b: float):
    return dividirf.dividir(a, b)

@app.get("/raiz")
def raiz(numero: float):
    resultado = raizf.raiz(numero)
    return {"resultado": resultado}
