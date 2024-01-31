# Model (table in db)
#Considered as a table to the Flask App'''

db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(),nullable=False)
    barcode = db.Column(db.String(length=12),nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    
    #To customise how item seen when queried in shell
    def __repr__(self):
        return f'Item {self.name}'