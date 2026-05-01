from app import create_app, db
from app.models import User,Task
from sqlalchemy import inspect

app = create_app()

with app.app_context():
    db.create_all()
    print("all created")

    inspector = inspect(db.engine)
    print("tables in db",inspector.get_table_names())

if __name__ == "__main__":
    app.run(debug=True)