from flask import Flask, Response
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask import url_for
import os

root = os.path.dirname(__file__)

flask_app = Flask(__name__)

flask_app.config.from_object('config')
db = SQLAlchemy(flask_app)

migrate = Migrate(flask_app,db)

manager = Manager(flask_app)

manager.add_command('db',MigrateCommand)

resp = Response("")
# resp.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
# resp.headers["Pragma"] = "no-cache"
# resp.headers["Expires"] = "0"

from app.controllers.pageTranslate import PageTranslator
from app.controllers import default
import app.models.tables


trans = PageTranslator( os.path.join(root,'static\\pages\\'),
                        os.path.join(root,'templates\\'))

trans.translate()
