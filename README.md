# Pedestrian Tracker

An application to track pedestrians in video streams, developed by [Matthew Cabrera](https://github.com/sabaideematt).

## Description

This project uses computer vision to detect and track pedestrians in real-time. It also offers a web interface to visualize the tracking and provides statistics on the number of pedestrians detected.

## Installation

1. **Clone the Repository**:
   
   ```
   git clone https://github.com/sabaideematt/pedestrian-tracker.git
   cd pedestrian-tracker
   ```

2. **Set Up a Virtual Environment (Recommended)**:

   ```bash
   pip install virtualenv
   virtualenv venv
   ```

   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`

3. **Install Required Packages**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the Database**:
   
   After setting up your configurations, run the following script to initialize the SQLite database:

   ```bash
   python init_db.py
   ```

## Running the Application

1. Start the Flask application:

   ```bash
   python app.py
   ```

2. Navigate to `http://localhost:5000` in your web browser to view the tracking interface.

## Contributing

For contributions, please create a pull request. All contributions by Matthew Cabrera, [@sabaideematt](https://github.com/sabaideematt).

## License

This project is licensed under the MIT License. Refer to the `LICENSE` file for more details.