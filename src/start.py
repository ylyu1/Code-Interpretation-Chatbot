from app import app, db
import os

def init_db():
    """Initialize the database if it does not already exist."""
    db_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app.db')
    if not os.path.exists(db_file_path):
        with app.app_context():
            db.create_all()

if __name__ == "__main__":
    init_db()
