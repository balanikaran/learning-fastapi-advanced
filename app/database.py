from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_USERNAME = "fastapi_course_user"
DATABASE_PASSWORD = ""
DATABASE_URL = "localhost"
DATABASE_NAME = "fastapi_course_db"

SQL_ALCHEMY_DATABASE_URL = "postgresql://{databaseUsername}:{databasePassword}@{databaseUrl}/{databaseName}".format(
    databaseUsername=DATABASE_USERNAME,
    databasePassword=DATABASE_PASSWORD,
    databaseUrl=DATABASE_URL,
    databaseName=DATABASE_NAME
)

print("SQL ALCHEMY DB URL: {}".format(SQL_ALCHEMY_DATABASE_URL))

engine = create_engine(SQL_ALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Database Dependency
def getDatabase():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()