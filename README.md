# Pedestrian Tracker

A computer vision project leveraging OpenCV to detect and track pedestrians in video footage. Integrated with Flask to provide a user-friendly web interface, and SQLite to keep a record of the pedestrian counts.

## Features

- Real-time pedestrian detection from video footage.
- Live web feed displaying the detected pedestrians.
- Database integration to store and retrieve pedestrian count data.
- A stylish and responsive web interface.

## Setup & Installation

1. **Clone the Repository**: 

    ```bash
    git clone https://github.com/sabaideematt/pedestrian-tracker.git
    cd pedestrian-tracker
    ```

2. **Install Dependencies**:

   Ensure you have Python installed. Then, using pip, install the required packages:

   ```bash
   pip install flask flask_sqlalchemy opencv-python
   ```

3. **Set Up the Database**:

   Before running the application for the first time, ensure the database is initialized. You can do this by running:

   ```python
   from app import db
   with app.app_context():
       db.create_all()
   ```

   Once the tables are created, you won't need to run these lines again.

4. **Run the Application**:

   ```bash
   python app.py
   ```

   This will start a local development server. Open a web browser and navigate to `http://127.0.0.1:5000/` to see the application in action.

## Project Structure

- `/static`: Contains static files such as CSS and JavaScript.
- `/templates`: Contains the HTML templates.
- `app.py`: Main application file with Flask routes and video processing logic.
- `models.py`: Contains the database models for SQLAlchemy.

## Future Enhancements

- Integration with a more robust database like PostgreSQL for scalability.
- Additional analytics views to show insights from the pedestrian count data.
- Improved tracking algorithms for better accuracy and detection in diverse scenarios.

## Credits

Project developed by Matthew Cabrera.

OpenCV for computer vision functionalities.
Flask for the web application framework.
SQLite for lightweight database functionalities.