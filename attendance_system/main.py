from app import create_app
from app.database import init_db
import os

app = create_app()
init_db(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))
