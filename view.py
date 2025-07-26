from app import app, render_template

#Definição de rotas

@app.route('/')
def inicial():
    return render_template('index.html')