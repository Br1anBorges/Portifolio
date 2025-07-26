from flask import Flask, render_template

#Inicialização do app
app = Flask(__name__)

#Importando as rotas
from view import *

#Executando arquivo diretamente dessa aba
if __name__ == '__main__':
    
    app.run(debug=True)
