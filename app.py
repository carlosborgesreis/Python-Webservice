from aiohttp import web
import json
from services.converte_romano import numero_para_romano
from services.validador_cpf import valida_cpf
from services.conta_zeros import conta_zeros
from services.gerador_senha import gera_senha
from services.classificador_senha import classifica_senha
from services.criptografa_senha import hash_md5


routes = web.RouteTableDef()

@routes.get('/romano/{numero}')
async def converter_romano(request):
    numero = request.match_info['numero']
    romano = numero_para_romano(numero)
    response = {
        "resposta": romano
    }
    return web.Response(text=json.dumps(response, ensure_ascii=False))

@routes.get('/valida_cpf/{cpf}')
async def validadar_cpf(request):
    cpf = request.match_info['cpf']
    validacao = 'válido' if valida_cpf(cpf) else 'inválido'
    response = {
        "cpf": cpf,
        "status": validacao
    }
    return web.Response(text=json.dumps(response, ensure_ascii=False))

@routes.get('/dist_zeros/{string}')
async def dist_zeros(request):
    string = request.match_info['string']
    cont = conta_zeros(string)
    response = {
        "string": string,
        "dist_zeros": cont
    }
    return web.Response(text=json.dumps(response, ensure_ascii=False))

@routes.get('/gera_senha')
async def gerar_senha(request):
    senha = gera_senha()
    classificacao = classifica_senha(senha)
    hash_senha = hash_md5(senha)
    response = {
        "senha": senha,
        "classificacao": classificacao,
        "hash": hash_senha
    }
    return web.Response(text=json.dumps(response, ensure_ascii=False))
    
app = web.Application()
app.add_routes(routes)
web.run_app(app)