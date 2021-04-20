from flask import Flask
app = Flask(__name__) #nuevo objeto

@app.route('/')#Wrap o deorador. indica la ruta donde el usuario podra tener acceso
def hello_world():
    return 'Hello, World!'#regresar un string

app.run() # se encarga de ejecutr el servidor 5000
