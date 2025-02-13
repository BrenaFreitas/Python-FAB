from flask import Flask # importa a classe Flask 
from flask_appbuilder import AppBuilder, SQLA # importa a classe AppBuilder e SQLA
from flask_migrate import Migrate # importa a classe Migrate 
from config import Config # importa a classe Config 

# cria uma instância da classe Flask e armazena na variável app
app = Flask(__name__, static_folder="static")
# configura a aplicação com as configurações da classe Config
app.config.from_object(Config)
# cria uma instância da classe SQLA e armazena na variável db
db = SQLA(app)
# cria uma instância da classe Migrate e armazena na variável migrate
migrate = Migrate(app, db)
# cria uma instância da classe AppBuilder e armazena na variável appbuilder
appbuilder = AppBuilder(app, db.session)
# importa o módulo views do pacote app 
from . import views
from . import models