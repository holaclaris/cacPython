from flask import Flask, render_template, request, redirect
from controller import *

app = Flask(__name__)

#Rutas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/destinos')
def destinos():
    paquetes = obtener_paquetes()
    return render_template('destinos.html', paquetes=paquetes)

@app.route('/guias')
def guias():
    return render_template('guias.html')


# delete

@app.route('/destinos/eliminar_paquete/<int:id>')
def delete_paquete(id):
    eliminar_paquete(id)
    return redirect("/destinos")

#Lo siguiente es el codigo del profe para implementar el crud

# # insert
# # 1) cargar el form
# @app.route("/tienda/cargar_producto")
# def insertTienda():
#     title = "Nuevo Producto"
#     return render_template("form_nuevo_producto.html", title=title)
# # 2) enviar los datos del form, por POST

# @app.route("/tienda/guardar_nuevo_producto", methods = ['POST'] )
# def newProd_Tienda():
#     # print(request.form['nombre'])
#     nombre_prod = request.form['nombre']
#     desc_prod = request.form['descripcion']
#     precio_prod = request.form['precio']
#     cargar_nuevo_producto(nombre_prod, desc_prod, precio_prod)
#     return redirect("/tienda")
    
# # update
# @app.route("/tienda/editar_producto/<int:id>")
# def editar_prod(id):
#     title = "Editar Producto"
#     prod_por_id = obtener_prod_por_id(id)
#     # print(prod_por_id)
#     return render_template("form_editar_producto.html", title=title, producto=prod_por_id)

# @app.route("/tienda/update_producto", methods=['POST'])
# def update_prod():
#     id_edit = request.form['id']
#     nombre_edit = request.form['nombre']
#     desc_edit = request.form['descripcion']
#     precio_edit = request.form['precio']
#     resp = actualizar_prod(nombre_edit,desc_edit,precio_edit,id_edit)
#     return redirect("/tienda")
#     # return render_template("tienda.html", resp=resp)




if __name__=='__main__':
    app.run(debug=True)
