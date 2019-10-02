from aiohttp import web
import json
from services.converte_romano import numero_para_romano
from services.validador_cpf import valida_cpf
from services.conta_zeros import conta_zeros
from services.gerador_senha import gera_senha
from services.classificador_senha import classifica_senha
from services.criptografa_senha import hash_md5
from view.app_view import *

def html_response(text):
    return web.Response(text=text, content_type='text/html')

routes = web.RouteTableDef()

@routes.get('/')
async def app_main(request):
    return html_response(app_view())

@routes.get('/romano')
async def converter_romano(request):
    numero = request.rel_url.query['roman']
    romano = numero_para_romano(numero)
   
    return html_response(roman_view(romano))

@routes.get('/valida_cpf')
async def validadar_cpf(request):
    cpf = request.rel_url.query['cpf']
    validacao = 'Válido' if valida_cpf(cpf) else 'Inválido'
    color = 'green' if validacao == 'válido' else 'red'
    return html_response(valida_cpf_view(cpf, validacao, color))

@routes.get('/dist_zeros/{string}')
async def dist_zeros(request):
    string = request.rel_url.query['distz']
    cont = conta_zeros(string)
    return html_response(dist_zeros_view(string, cont))


@routes.get('/gera_senha')
async def gerar_senha(request):
    senha = gera_senha()
    classificacao = classifica_senha(senha)
    hash_senha = hash_md5(senha)
    return html_response(gera_senha_view(senha, classificacao, hash_senha))
    
app = web.Application()
app.add_routes(routes)
web.run_app(app)