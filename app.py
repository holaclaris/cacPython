from flask import Flask, flash, render_template, request, redirect
from controller import *

app = Flask(__name__)
app.secret_key = 'Grupo17'

#Rutas
#Inicio ------
@app.route('/')
def index():
    return render_template('index.html')

#Destinos------
#Read
@app.route('/destinos')
def destinos():
    paquetes = obtener_paquetes()
    return render_template('destinos.html', paquetes=paquetes)

# Create
@app.route('/destinos/guardar_nuevo_paquete', methods=['POST'])
def guardar_nuevo_paquete_route():
    nom = request.form['nombre']
    dest = request.form['destino']
    desc = request.form['descripcion']
    imgURL = request.form['imagen']
    prec = request.form['precio']
    disp = request.form['disponible']

    filas_agregadas = guardar_nuevo_paquete(nom, dest, desc, imgURL, prec, disp)
    if filas_agregadas > 0:
        flash('El paquete se agrego exitosamente!', 'success')
    else:
        flash('El paquete no pudo ser agregado!', 'error')

    return redirect('/destinos')

# Update
@app.route('/destinos/editar_paquete/<int:id>', methods=['POST'])
def editar_paquete_route(id):
    nom = request.form['nombre']
    dest = request.form['destino']
    desc = request.form['descripcion']
    imgURL = request.form['imagen']
    prec = request.form['precio']
    disp = request.form['disponible']

    filas_modificadas = editar_paquete(id, nom, dest, desc, imgURL, prec, disp)
    if filas_modificadas > 0:
        flash('El paquete se actualizo correctamente!', 'success')
    else:
        flash('El paquete no pudo ser actualizo!', 'error')

    return redirect('/destinos')

# delete
@app.route('/destinos/eliminar_paquete/<int:id>')
def delete_paquete(id):
    filas_eliminadas = eliminar_paquete(id)
    if filas_eliminadas > 0:
        flash('El paquete se elimino correctamente!', 'success')
    else:
        flash('El paquete no pudo ser eliminado!', 'error')
    return redirect('/destinos')

#Nuestros guias ------
@app.route('/guias')
def guias():
    return render_template('guias.html')

#Contacto ----
@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__=='__main__':
    app.run(debug=True)
