from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE = "https://cdna.artstation.com/p/assets/images/images/008/617/106/large/anakin-pagaling-asset.jpg?1513952461"


class Cupcake(db.Model):
    __tablename__ = "cupcakes"
    

    id = db.Column(db.Integer,
                       primary_key=True,
                       autoincrement=True)
    
    flavor = db.Column(db.Text,
                       nullable=False)
    
    size = db.Column(db.Text,
                       nullable=False)

    rating = db.Column(db.Float,
                       nullable=False)
     
    image = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE)
    
    
def connect_db(app):
    db.app = app
    db.init_app(app)