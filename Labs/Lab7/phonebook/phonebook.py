import csv
from connect import connect

def create_table():
    sql = """
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(100) NOT NULL,
        phone VARCHAR(30) NOT NULL UNIQUE
    )
    """

    try:
        conn = connect()
        if conn is None:
          return
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
        print("Table created successfully.")
    except Exception as e:
        print("Error:", e)
import csv
from connect import connect


def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    sql = """
    INSERT INTO phonebook(first_name, phone)
    VALUES(%s, %s)
    """

    try:
        conn = connect()
        if conn is None:
          return
        cur = conn.cursor()
        cur.execute(sql, (name, phone))
        conn.commit()
        cur.close()
        conn.close()
        print("Inserted successfully.")
    except Exception as e:
        print("Error:", e)

def insert_from_csv(filename):
    sql = """
    INSERT INTO phonebook(first_name, phone)
    VALUES(%s, %s)
    """

    try:
        conn = connect()
        if conn is None:
          return
        cur = conn.cursor()

        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cur.execute(sql, (row['first_name'], row['phone']))

        conn.commit()
        cur.close()
        conn.close()
        print("CSV data inserted.")
    except Exception as e:
        print("Error:", e)


def update_name():
    phone = input("Enter phone: ")
    new_name = input("Enter new name: ")

    sql = """
    UPDATE phonebook
    SET first_name = %s
    WHERE phone = %s
    """

    conn = connect()
    if conn is None:
          return
    cur = conn.cursor()
    cur.execute(sql, (new_name, phone))
    conn.commit()

    if cur.rowcount > 0:
        print("Updated successfully.")
    else:
        print("No record found.")

    cur.close()
    conn.close()


def update_phone():
    name = input("Enter name: ")
    new_phone = input("Enter new phone: ")

    sql = """
    UPDATE phonebook
    SET phone = %s
    WHERE first_name = %s
    """

    conn = connect()
    if conn is None:
          return
    cur = conn.cursor()
    cur.execute(sql, (new_phone, name))
    conn.commit()

    if cur.rowcount > 0:
        print("Updated successfully.")
    else:
        print("No record found.")

    cur.close()
    conn.close()


def query_all():
    sql = "SELECT * FROM phonebook ORDER BY id"

    conn = connect()
    if conn is None:
          return
    cur = conn.cursor()
    cur.execute(sql)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()


def query_by_name():
    name = input("Enter name: ")

    sql = """
    SELECT * FROM phonebook
    WHERE first_name ILIKE %s
    """

    conn = connect()
    if conn is None:
          return
    cur = conn.cursor()
    cur.execute(sql, (f"%{name}%",))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()

def query_by_phone():
    phone = input("Enter phone: ")

    sql = """
    SELECT * FROM phonebook
    WHERE phone LIKE %s
    """

    conn = connect()
    cur = conn.cursor()
    cur.execute(sql, (f"%{phone}%",))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()


def delete_by_name():
    name = input("Enter name: ")

    sql = "DELETE FROM phonebook WHERE first_name = %s"

    conn = connect()
    if conn is None:
          return
    cur = conn.cursor()
    cur.execute(sql, (name,))
    conn.commit()

    print(f"Deleted: {cur.rowcount}")

    cur.close()
    conn.close()


def delete_by_phone():
    phone = input("Enter phone: ")

    sql = "DELETE FROM phonebook WHERE phone = %s"

    conn = connect()
    if conn is None:
          return
    cur = conn.cursor()
    cur.execute(sql, (phone,))
    conn.commit()

    print(f"Deleted: {cur.rowcount}")

    cur.close()
    conn.close()


def menu():
    while True:
        print("\n--- PHONEBOOK ---")
        print("1 Create table")
        print("2 Insert console")
        print("3 Insert CSV")
        print("4 Update name")
        print("5 Update phone")
        print("6 Show all")
        print("7 Search by name")
        print("8 Search by phone")
        print("9 Delete name")
        print("10 Delete phone")
        print("0 Exit")

        choice = input("Choose: ")

        if choice == "1":
            create_table()
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            insert_from_csv(input("CSV file: "))
        elif choice == "4":
            update_name()
        elif choice == "5":
            update_phone()
        elif choice == "6":
            query_all()
        elif choice == "7":
            query_by_name()
        elif choice == "8":
            query_by_phone()
        elif choice == "9":
            delete_by_name()
        elif choice == "10":
            delete_by_phone()
        elif choice == "0":
            break
        else:
            print("Wrong input")


if __name__ == "__main__":
    menu()
