from flask import render_template, flash, request, redirect
from app import app
import json

# Usually the searchs occurs in databases, for this simple example we're using search in this array
BRAZIL_STATES = [u"Acre - Rio Branco",
u"Alagoas - Maceió",
u"Amapá - Macapá",
u"Amazonas - Manaus",
u"Bahia - Salvador",
u"Ceara - Fortaleza",
u"Distrito Federal - Brasília",
u"Espírito Santo - Vitória",
u"Goiás - Goiânia",
u"Maranhão - São Luiz",
u"Mato Grosso - Cuiabá",
u"Mato Grosso do Sul - Campo Grande",
u"Minas Gerais - Belo Horizonte",
u"Pará - Belém",
u"Paraíba - João Pessoa",
u"Paraná - Curitiba",
u"Pernambuco - Recife",
u"Piauí - Terezina",
u"Rio de Janeiro - Rio de Janeiro",
u"Rio Grande do Norte - Natal",
u"Rio Grande do Sul - Porto Alegre",
u"Rondônia - Porto Velho",
u"Roraima - Boa Vista",
u"Santa Catarina - Florianópolis",
u"São Paulo - São Paulo",
u"Sergipe - Aracajú",
u"Tocantins - Palmas"]

@app.route("/")
@app.route('/index')
def index():
    return render_template("index.html") # render the page

@app.route("/search")
def search():
  text = request.args['searchText'] # get the text to search for
  # create an array with the elements of BRAZIL_STATES that contains the string
  # the case is ignored
  result = [c for c in BRAZIL_STATES if text.lower() in c.lower()]
  # return as JSON
  return json.dumps({"results":result}) 


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         flash('Login requested for OpenID="%s", remember_me=%s' %
#               (form.openid.data, str(form.remember_me.data)))
#         return redirect('/index')
#     return render_template('login.html', 
#                            title='Sign In',
#                            form=form,
#                            providers=app.config['OPENID_PROVIDERS'])