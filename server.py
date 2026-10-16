from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html', titulo='Flask', mensaje='Bienvenido a la página web')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html', titulo='Servicios', mensaje='Nuestros servicios incluyen desarrollo web, diseño gráfico y marketing digital.')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html', titulo='Contacto', mensaje='Aquí puedes encontrar información sobre cómo contactarnos.')

@app.route('/productos')
def productos():
    return render_template('productos.html', titulo='Productos', mensaje='Aquí puedes encontrar información sobre nuestros productos.')

if __name__ == '__main__':
    app.run(debug=True, port=5050)