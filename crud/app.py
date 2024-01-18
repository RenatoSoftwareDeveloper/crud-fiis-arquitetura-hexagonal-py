# crud/app.py
from flask import Flask
#from crud.web.routes.fundo_imobiliario_routes import fundo_imobiliario_blueprint
from web.routes.fundo_imobiliario_routes import fundo_imobiliario_blueprint
app = Flask(__name__)
app.register_blueprint(fundo_imobiliario_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
