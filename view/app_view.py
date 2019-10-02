def app_view():
    return """
    <h2>Serviços:</h2>
    <form action="/romano" method="get" accept-charset="utf-8"
      enctype="application/x-www-form-urlencoded">

        <label for="roman">Numero para Romano</label>
        <input id="roman" name="roman" type="text" value="" autofocus/>

        <input type="submit""/>
    </form>
    <form action="/valida_cpf" method="get" accept-charset="utf-8"
      enctype="application/x-www-form-urlencoded">

        <label for="cpf">Validar CPF</label>
        <input id="cpf" name="cpf" type="text" value="" autofocus/>

        <input type="submit""/>
    </form>
    <form action="/dist_zeros" method="get" accept-charset="utf-8"
      enctype="application/x-www-form-urlencoded">

        <label for="distz">Distancia de zeros</label>
        <input id="distz" name="distz" type="text" value="" autofocus/>

        <input type="submit""/>
    </form>
    <form action="/gera_senha" method="get" accept-charset="utf-8"
      enctype="application/x-www-form-urlencoded">

        <label>Gerador de senha</label>

        <input type="submit""/>
    </form>
    """

def roman_view(value):
    return f"""
    <h3 style="color: red;font-size: 34">Romano: {value}</h3>
    <form action="http://0.0.0.0:8080/">
        <input type="submit" value="Voltar" />
    </form>

    """

def valida_cpf_view(cpf, is_valid, color):
    return f"""
    <h2 style="color: {color}">CPF: {cpf}</h2>
    <h1 style="color: {color}">{is_valid}</h1>
    <form action="http://0.0.0.0:8080/">
        <input type="submit" value="Voltar" />
    </form>

    """

def dist_zeros_view(string, dist):
    return f"""
    <h5 style="color: yellow">String: {string}</h5>
    <h6 style="color: yellow">Maior distância de zeros: {dist}</h6>
    <form action="http://0.0.0.0:8080/">
        <input type="submit" value="Voltar" />
    </form>

    """

def gera_senha_view(senha, classificacao, hash):
    return f"""
    <h5 style="color: blue">Senha: {senha}</h5>
    <h5 style="color: black">Classificação: {classificacao}</h5>
    <h5 style="color: red">Hash: {hash}</h5>
    <form action="http://0.0.0.0:8080/">
        <input type="submit" value="Voltar" />
    </form>

    """