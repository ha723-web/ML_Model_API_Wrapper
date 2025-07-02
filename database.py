from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://harshiniakunuri@localhost:5432/pricebook_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
