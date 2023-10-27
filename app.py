from flask import Flask, render_template, Response, url_for
import cv2
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pedestrian_data.db'
db = SQLAlchemy(app)

# Database Model
class PedestrianData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    count = db.Column(db.Integer)

@app.route('/')
def index():
    return render_template('index.html')

def generate_frames():
    camera = cv2.VideoCapture('path_to_video.mp4')
    while True:
        success, frame = camera.read()  
        if not success:
            break
        else:
            # Convert the image frame into a jpeg format and then return it
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            
            # (You can integrate the pedestrian detection logic here and update the database accordingly.)
            
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
    camera.release()

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    db.create_all()  # This will create the pedestrian_data.db file and the PedestrianData table
    app.run(debug=True)