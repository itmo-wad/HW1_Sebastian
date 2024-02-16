from flask import Flask, render_template, redirect, url_for
from datetime import datetime 

app = Flask(__name__)

@app.route('/')
def main():
    # aqui puedo redirigir desde la ruta por defecto a /profile
    return redirect(url_for('profile'))

@app.route('/profile')
def profile():
    # Aquí puedo agregar parametros a la plantilla si quiero como el siguiente ejemplo
    return render_template('index.html', 
                           nombre="Sebastian Guevara", 
                           correo="sebastianguevara11@gmail.com",
                           fecha_actual=datetime.utcnow())


if __name__ == '__main__':
    app.run(debug=True)
