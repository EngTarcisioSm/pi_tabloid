from flask import Flask
from os import path
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# iniciando o banco de dados
db = SQLAlchemy()

DB_NAME = "database.db" # para o sqlite
DB_POSTGRES = "tabloid"
PASSWORD = 'jsbach'

def create_app():
    app = Flask(__name__)
 #Sqlite configuração
    app.config['SECRET_KEY'] = 'grhteyeuwhhs fgdhjajakuww'
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
 #Postgres
    # app.config['SQLALCHEMY_DATABASE_URI']=f'postgresql://postgres:{PASSWORD}@localhost/{DB_POSTGRES}'
    app.config['SQLALCHEMY_DATABASE_URI']=f'postgres://uvwafhkypqrwdr:976972ce00aeba9047cf9c53a13bca57ca465fbfa219ccc5ffbae8a3b58aa950@ec2-23-23-151-191.compute-1.amazonaws.com:5432/ddai8i1hrh524k'
    db.init_app(app)



    from .views import views
    from .auth import auth
    

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    

    from .models import User, Note, Items
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
        
    return app
def create_database(app):
    db.create_all(app=app)
    if not path.exists('website/' + DB_NAME):
       db.create_all(app=app)
       print('Created Database')

    