from app.database.database import engine, Base
from app.models import user, item

# Import all models here so they are registered with SQLAlchemy
# before calling Base.metadata.create_all()

def init_db():
    # Create all tables
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()