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

app = FastAPI()

@app.get("/")
def root():
    # Redireciona o Usuário assim que ele abrir a URL, direto para a URL '/docs' com todas as funções
    return RedirectResponse(url="/docs")

@app.get("/exponenciar")
def exponenciar(a: float, b: float):
    return exponenciarf.exponenciar(a, b)

@app.get("/subtrair")
def subtrair(a: float, b: float):
    return subtrairf.subtrair(a, b)

@app.get("/fatorarf")
def fatorarf(a, b):
    return fatorarf.fatorarf(a, b)