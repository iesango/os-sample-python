from flask import Flask

application = Flask(__name__)

@application.route("/")
def home():
    return """
    <h1>¡Hola desde OpenShift Iván!</h1>
    <p>Esta es mi primera aplicación web desplegada en la nube.</p>
    <a href='/about'>Ir a Acerca de</a>
    """

@application.route("/about")
def about():
    return """
    <h1>Acerca de esta app</h1>
    <p>Esta aplicación fue creada usando Python y Flask, y desplegada en OpenShift.</p>
    <p>Autor: Iván</p>
    <a href='/'>Volver al inicio</a>
    """

if __name__ == "__main__":
    application.run()
