from app import create_app,db
from app.models import Task,User
import os


app=create_app()

#Initialize DB
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render's PORT or default 5000
    app.run(host="0.0.0.0", port=port)
