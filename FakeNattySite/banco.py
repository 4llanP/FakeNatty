from shared import database, app
from shared.models import Usuario, Post

with app.app_context():
    database.create_all()
