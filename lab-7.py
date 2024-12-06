from sqlalchemy import create_engine, Column, Integer, String, func
from sqlalchemy.orm import declarative_base, Session

# Підключення до бази даних
engine = create_engine('sqlite:///database-lab7.db', echo=False)
Base = declarative_base()

# Оголошення класів моделей
class IncomeCategories(Base):
    __tablename__ = 'income_categories'
    id = Column(Integer, primary_key=True)
    passive_income = Column(Integer)
    active_income = Column(Integer)


class SourcesOfIncome(Base):
    __tablename__ = 'sources_of_income'
    id = Column(Integer, primary_key=True)
    salary = Column(Integer)
    sales = Column(Integer)
    investments = Column(Integer)


class Expenses(Base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True)
    expense_name = Column(String)
    expense_amount = Column(Integer)


# Створення таблиць
Base.metadata.create_all(engine)

# Створення сесії
def create_session():
    return Session(engine)


# Функції CRUD
def add_income_category(session, passive, active):
    """Додати категорію доходу"""
    new_category = IncomeCategories(passive_income=passive, active_income=active)
    session.add(new_category)
    session.commit()
    print("Категорія доходу додана.")


def add_source_of_income(session, salary, sales, investments):
    """Додати джерело доходу"""
    new_source = SourcesOfIncome(salary=salary, sales=sales, investments=investments)
    session.add(new_source)
    session.commit()
    print("Джерело доходу додано.")


def add_expense(session, name, amount):
    """Додати витрату"""
    new_expense = Expenses(expense_name=name, expense_amount=amount)
    session.add(new_expense)
    session.commit()
    print("Витрата додана.")


def update_expense(session, expense_id, new_name, new_amount):
    """Оновити витрату"""
    expense = session.query(Expenses).filter_by(id=expense_id).first()
    if expense:
        expense.expense_name = new_name
        expense.expense_amount = new_amount
        session.commit()
        print("Витрата оновлена.")
    else:
        print("Витрата не знайдена.")


def delete_expense(session, expense_id):
    """Видалити витрату"""
    expense = session.query(Expenses).filter_by(id=expense_id).first()
    if expense:
        session.delete(expense)
        session.commit()
        print("Витрата видалена.")
    else:
        print("Витрата не знайдена.")


def search_expenses(session, name=None):
    """Пошук витрат за назвою"""
    query = session.query(Expenses)
    if name:
        query = query.filter(Expenses.expense_name.like(f"%{name}%"))
    results = query.all()
    if results:
        for expense in results:
            print(f"ID: {expense.id}, Назва: {expense.expense_name}, Сума: {expense.expense_amount}")
    else:
        print("Витрати не знайдено.")


# Головна функція для роботи з користувачем
def main():
    session = create_session()
    while True:
        print("\nОберіть дію:")
        print("1. Додати категорію доходу")
        print("2. Додати джерело доходу")
        print("3. Додати витрату")
        print("4. Оновити витрату")
        print("5. Видалити витрату")
        print("6. Пошук витрат")
        print("7. Вийти")
        choice = input("Ваш вибір: ")

        if choice == "1":
            passive = int(input("Введіть суму пасивного доходу: "))
            active = int(input("Введіть суму активного доходу: "))
            add_income_category(session, passive, active)
        elif choice == "2":
            salary = int(input("Введіть зарплату: "))
            sales = int(input("Введіть дохід від продажів: "))
            investments = int(input("Введіть дохід від інвестицій: "))
            add_source_of_income(session, salary, sales, investments)
        elif choice == "3":
            name = input("Введіть назву витрати: ")
            amount = int(input("Введіть суму витрати: "))
            add_expense(session, name, amount)
        elif choice == "4":
            expense_id = int(input("Введіть ID витрати для оновлення: "))
            new_name = input("Введіть нову назву витрати: ")
            new_amount = int(input("Введіть нову суму витрати: "))
            update_expense(session, expense_id, new_name, new_amount)
        elif choice == "5":
            expense_id = int(input("Введіть ID витрати для видалення: "))
            delete_expense(session, expense_id)
        elif choice == "6":
            name = input("Введіть частину назви витрати для пошуку (або залиште порожнім): ")
            search_expenses(session, name)
        elif choice == "7":
            print("Вихід.")
            session.close()
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
