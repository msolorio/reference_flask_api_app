from . import db, ma

class Automobile(db.Model):
    __tablename__ = 'automobiles'

    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(50))
    year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Auto {self.make} {self.model}>'



class AutomobileSchema(ma.Schema):
    class Meta:
        fields = ('id', 'make', 'model', 'color', 'year')
        model = Automobile


auto_schema = AutomobileSchema()
autos_schema = AutomobileSchema(many=True)
