#importamos nuestro framework 
from flask import Flask, render_template

#Llamamos a flask, pero debemos decirle que este es nuestro archivo principal
app = Flask(__name__)

#Creamos una ruta para la pagina principal y mediante una funcion manejamos que hara el usuario en ella
@app.route('/')

def home():
    return render_template('home.html')

@app.route('/about')

def about():
    return render_template('about.html')

if __name__ == '__main__':
    #Mientras se mantenga en true el debug seguira avanzando
    app.run(debug=True)
