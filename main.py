from flask import Flask, render_template, jsonify, request, session, redirect, url_for
import sqlite3
app = Flask(__name__)
app.secret_key = 'clave-secreta'

#--------------------- Iniciar sesión ---------------------#
@app.route('/')
def index():
    return render_template('login.html')
  
@app.route('/confirmarUsuario', methods=['GET', "POST"])
def login():
  if request.method=="POST":
    usuario=request.form["nombre"]
    contraseña=request.form["contraseña"]
    print(usuario, contraseña)
    conn = sqlite3.connect('memotest.db')
    cur = conn.cursor()
    cur.execute(f"""SELECT *
                      FROM Jugadores
                      WHERE nombre = '{usuario}' 
                      AND contraseña='{contraseña}';
                  """)
    existe = cur.fetchall()
    conn.commit()
    conn.close()
    if existe != []:
      session['nombre']= usuario
      session['contraseña']= contraseña
      return redirect(url_for('inicio'))
    else:
      return redirect(url_for('index'))
# ---------------------------------------------------------------#

#-------------------------- Registrarse --------------------------#
@app.route('/registrarse')
def registro():
  return render_template('registro.html')
  
@app.route('/crearUsuario',methods=['GET', "POST"] )
def crearUsuario():
  if request.method=="POST":
    usuario=request.form["nombre"]
    contraseña=request.form["contraseña"]
    print(usuario, contraseña)
    conn = sqlite3.connect('memotest.db')
    cur = conn.cursor()
    cur.execute(f"""INSERT INTO Jugadores(nombre, contraseña)
      VALUES('{usuario}','{contraseña}');""")
    conn.commit()
    conn.close()
    session['nombre']= request.form['nombre']
    session['contraseña']=request.form['contraseña']
    print(session["nombre"])
    return redirect(url_for('inicio'))
  else:
    return redirect(url_for('index'))
# ---------------------------------------------------------------#

# ------------------------ Tableros ----------------------------#   
@app.route('/inicio')
def inicio():
  
  if session['nombre'] != "":
    return render_template('index.html')
  else:
    return redirect(url_for('index'))
  
@app.route('/tablero/<n>')
def tablero(n):
  tab = int(n)-1
  
  conn = sqlite3.connect('memotest.db')
  conn.row_factory = sqlite3.Row
  cur = conn.cursor()
  cur.execute(f""" SELECT *
  FROM Tableros
  WHERE idTablero={tab}
  ORDER BY numeroColumna, numeroFila; """)  
  va = cur.fetchall()
  lista=[]
  for i in va:
      li = {
           "id": i[0],
          "idTablero": i[1],
          "numeroColumna": i[2],
          "numeroFila": i[3],
          "valor": i[4]
      }
      lista.append(li)
  print(lista)
  cur.execute(f"""SELECT COUNT(DISTINCT numeroColumna)
  FROM Tableros
  WHERE idTablero={tab}""")
  col = cur.fetchone()
  cantColum = col[0]
  print(cantColum)
  cur.execute(f""" SELECT COUNT(DISTINCT numeroFila)
  FROM Tableros
  WHERE idTablero={tab}""")
  fil = cur.fetchone()
  cantFilas = fil[0]
  print(cantFilas)

  return render_template("tableros.html", tab=tab,lista=lista, cantFilas=cantFilas, cantColum=cantColum)
  

@app.route("/test")
def test():
#  id = int
  conn = sqlite3.connect('memotest.db')
  cur = conn.cursor()
  q= """ SELECT COUNT(DISTINCT numeroColumna)
  FROM Tableros
  WHERE idTablero=0
"""
  cur.execute(q)
  fil = cur.fetchall()
  print(fil)
#  cantco = fil[0]
  return f"hola {fil}"
# ---------------------------------------------------------------#
app.run(host='0.0.0.0', port=81)
