from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the SQLite database (adjust path to your database file)
DATABASE_URL = "sqlite:///database-lab7.db"

# Create engine and session
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Base class for ORM models
Base = declarative_base()

# Define tables based on the provided schema
class DescriptionOfTransactions(Base):
    __tablename__ = 'Description_of_transactions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    additional_information = Column(Integer)

class IncomeCategories(Base):
    __tablename__ = 'Income_categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    passive_income = Column(Integer)
    active_income = Column(Integer)

class Users(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(Text)
    email = Column(Text)

class Date(Base):
    __tablename__ = 'date'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date_of_transactions = Column(Integer)

class Expenses(Base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    expense_name = Column(Text)
    expence_amount = Column(Integer)

class SourcesOfIncome(Base):
    __tablename__ = 'sources_of_income'
    id = Column(Integer, primary_key=True, autoincrement=True)
    salary = Column(Integer)
    sales = Column(Integer)
    investments = Column(Integer)

class Summ(Base):
    __tablename__ = 'summ'
    id = Column(Integer, primary_key=True, autoincrement=True)
    transactions_sum = Column(Integer)

# Create tables in the database
Base.metadata.create_all(engine)

# CRUD Operations
def add_user(username, email):
    new_user = Users(username=username, email=email)
    session.add(new_user)
    session.commit()
    print(f"User {username} added.")

def get_users():
    users = session.query(Users).all()
    for user in users:
        print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}")

def update_user(user_id, new_email):
    user = session.query(Users).filter_by(id=user_id).first()
    if user:
        user.email = new_email
        session.commit()
        print(f"User {user.username}'s email updated to {new_email}.")
    else:
        print("User not found.")

def delete_user(user_id):
    user = session.query(Users).filter_by(id=user_id).first()
    if user:
        session.delete(user)
        session.commit()
        print(f"User {user.username} deleted.")
    else:
        print("User not found.")

# Example usage
if __name__ == "__main__":
    add_user("Yaroslav Shavula", "shayaros@example.com")
    get_users()
    update_user(1, "shayaros@icloud.com")
    delete_user(1)
