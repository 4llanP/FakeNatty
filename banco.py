from fakeNatty import database, app
from fakeNatty.models import Usuario, Post

with app.app_context():
    database.create_all()
