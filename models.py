from app import db


class State(db.Model):
    __tablename__ = 'states'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tp = db.Column(db.Float(), default=0.0)
    tc = db.Column(db.Float(), default=0.0)
    T = db.Column(db.Float(), default=0.0)
    b = db.Column(db.Float(), default=0.0)
    h = db.Column(db.Float(), default=0.0)
    timestamp = db.Column(db.BigInteger, default=0)

    def __init__(self, tp, tc, T, b, h, timestamp):
        self.tp = tp
        self.tc = tc
        self.T = T
        self.b = b
        self.h = h
        self.timestamp = timestamp

    def __repr__(self):
        return '<id {}>'.format(self.id)
 
    def serialize(self):
        return {
            'id': self.id,
            'tp': self.tp,
            'tc': self.tc,
            'T': self.T,
            'b': self.b,
            'h': self.h,
            'timestamp': self.timestamp
        }


