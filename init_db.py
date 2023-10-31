# init_db.py

from models import db

def init_db():
    """Initialize the database."""
    db.create_all()

if __name__ == '__main__':
    init_db()
    print("Database initialized!")
