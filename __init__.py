import os
from dotenv import load_dotenv
from app.server import app

load_dotenv()
 
if __name__ == "__main__":
        app.run(host=os.getenv("HOST_NAME"), port=os.getenv("PORT"))