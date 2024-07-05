from flask import Flask, render_template, request, redirect

app = Flask(__name__)

#Rutas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/destinos')
def destinos():
    return render_template('destinos.html')

@app.route('/guias')
def guias():
    return render_template('guias.html')


if __name__=='__main__':
    app.run(debug=True)
