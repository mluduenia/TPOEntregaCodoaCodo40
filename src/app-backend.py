from flask import Flask, render_template, request, redirect, url_for
import os
import database as db
template_dir=os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir=os.path.join(template_dir, 'src', 'templates', 'public', 'administrador')

app=Flask(__name__, template_folder = template_dir)

#Rutas de la app

@app.route('/')
def home():
    cursor=db.database.cursor()#es el database de database.py
    cursor.execute("SELECT * FROM consultas")
    miResultado=cursor.fetchall()
    #convertir los datos en diccionarios
    insertarObjeto=[]
    NombreColumna=[column[0] for column in cursor.description]
    for record in miResultado:
        insertarObjeto.append(dict(zip(NombreColumna, record)))
    cursor.close()
    return render_template('index.html',data=insertarObjeto)

#Guardar Usuarios en base
@app.route('/consultas',methods=['POST'])
def agregarUsuario():
    nombre=request.form['nombre']
    apellido=request.form['apellido']
    correo=request.form['correo']
    consulta=request.form['consulta']
    if nombre and apellido and correo and consulta:
        cursor=db.database.cursor()
        sql = "INSERT INTO consultas (nombre, apellido, correo, consulta) VALUES (%s, %s, %s, %s)"
        data = (nombre, apellido, correo, consulta)    #tupla
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

@app.route('/delete/<string:id>')
def delete(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM consultas WHERE id = %s"
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('home'))


@app.route('/edit/<string:id>', methods=['POST'])
def edit():
    nombre=request.form['nombre']
    apellido=request.form['apellido']
    correo=request.form['correo']
    consulta=request.form['consulta']
    if nombre and apellido and correo and consulta:
            cursor=db.database.cursor()
            sql = "UPDATE INTO consultas SET (nombre, apellido, correo, consultas) VALUES (%s, %s, %s, %s)"
            data = (nombre, apellido, correo, consulta)    #tupla
            cursor.execute(sql, data)
            db.database.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True, port=3501)