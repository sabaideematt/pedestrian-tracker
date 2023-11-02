from flask import Flask, render_template, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
import cv2
from models import db, PedestrianData, TotalPedestrians

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pedestrian_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

api = Api(app)

# Load pre-trained model for pedestrian detection
pedestrian_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

@app.route('/')
def index():
    return render_template('index.html')

def detect_pedestrians(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    pedestrians = pedestrian_cascade.detectMultiScale(gray, 1.1, 3)
    for (x, y, w, h) in pedestrians:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return frame, len(pedestrians)

def generate_frames():
    camera = cv2.VideoCapture('video_path_here.mp4')
    while True:
        success, frame = camera.read()
        if not success:
            break
        frame, pedestrian_count = detect_pedestrians(frame)
        
        # Update database with pedestrian count
        new_data = PedestrianData(count=pedestrian_count)
        db.session.add(new_data)
        
        total_record = TotalPedestrians.query.first()
        if not total_record:
            db.session.add(TotalPedestrians(total_count=pedestrian_count))
        else:
            total_record.total_count += pedestrian_count
        
        db.session.commit()

        ret, jpeg = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# RESTful API Resource for Pedestrian Stats
class PedestrianStatsResource(Resource):
    def get(self):
        total_pedestrians = TotalPedestrians.query.first()
        total_count = total_pedestrians.total_count if total_pedestrians else 0
        return jsonify({"total_pedestrians_counted": total_count})

api.add_resource(PedestrianStatsResource, '/api/pedestrian-stats')

if __name__ == '__main__':
    app.run(debug=True)
