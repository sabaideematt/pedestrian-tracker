from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Model to store the count of pedestrians detected in each frame
class PedestrianData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())
    count = db.Column(db.Integer)

# Model to store the cumulative count of pedestrians detected
class TotalPedestrians(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total_count = db.Column(db.Integer, default=0)
