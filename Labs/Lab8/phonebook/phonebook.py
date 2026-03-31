import csv
from connect import connect
# from csv_loader import load_from_csv


def create_table():
    sql = """
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(100) NOT NULL,
        surname VARCHAR(100) NOT NULL,
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


def insert_from_console():
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    phone = input("Enter phone: ")

    sql = "CALL insert_or_update_user(%s, %s, %s)"

    try:
        conn = connect()
        if conn is None:
            return
        cur = conn.cursor()
        cur.execute(sql, (name, surname, phone))
        conn.commit()
        cur.close()
        conn.close()
        print("Inserted or updated successfully.")
    except Exception as e:
        print("Error:", e)


def insert_many_users(names, surnames, phones):
    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "CALL insert_many_users(%s, %s, %s)",
            (names, surnames, phones)
        )

        cursor.execute("SELECT * FROM invalid_users")
        invalid_data = cursor.fetchall()

        conn.commit()

        if invalid_data:
            print(" Invalid data found:")
            for row in invalid_data:
                print(row)
        else:
            print("All users inserted successfully!")

    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()


def load_from_csv(path):
    names = []
    surnames = []
    phones = []

    with open(path, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)

        for row in reader:
            if len(row) >= 3:
                name, surname, phone = row[0], row[1], row[2]
                names.append(name)
                surnames.append(surname)
                phones.append(phone)

    insert_many_users(names, surnames, phones)


def update_name():
    phone = input("Enter phone: ")
    new_name = input("Enter new name: ")

    sql = """
    UPDATE phonebook
    SET first_name = %s
    WHERE phone = %s
    """

    try:
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
    except Exception as e:
        print("Error:", e)


def update_phone():
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    new_phone = input("Enter new phone: ")

    sql = "CALL insert_or_update_user(%s, %s, %s)"

    try:
        conn = connect()
        if conn is None:
            return
        cur = conn.cursor()
        cur.execute(sql, (name, surname, new_phone))
        conn.commit()
        print("Phone updated successfully.")
        cur.close()
        conn.close()
    except Exception as e:
        print("Error:", e)


def query_all():
    sql = "SELECT * FROM phonebook ORDER BY id"

    try:
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
    except Exception as e:
        print("Error:", e)


def query_by_name():
    pattern = input("Enter pattern: ")

    sql = "SELECT * FROM search_phonebook_pattern(%s)"

    try:
        conn = connect()
        if conn is None:
            return
        cur = conn.cursor()
        cur.execute(sql, (pattern,))

        rows = cur.fetchall()
        for row in rows:
            print(row)

        cur.close()
        conn.close()
    except Exception as e:
        print("Error:", e)


def query_by_phone():
    pattern = input("Enter phone pattern: ")

    sql = "SELECT * FROM search_phonebook_pattern(%s)"

    try:
        conn = connect()
        if conn is None:
            return
        cur = conn.cursor()
        cur.execute(sql, (pattern,))

        rows = cur.fetchall()
        for row in rows:
            print(row)

        cur.close()
        conn.close()
    except Exception as e:
        print("Error:", e)


def query_with_pagination():
    limit = int(input("Enter limit: "))
    offset = int(input("Enter offset: "))

    sql = "SELECT * FROM get_phonebook_paginated(%s, %s)"

    try:
        conn = connect()
        if conn is None:
            return
        cur = conn.cursor()
        cur.execute(sql, (limit, offset))

        rows = cur.fetchall()
        for row in rows:
            print(row)

        cur.close()
        conn.close()
    except Exception as e:
        print("Error:", e)


def delete_by_name():
    name = input("Enter name: ")

    sql = "CALL delete_user(%s)"

    try:
        conn = connect()
        if conn is None:
            return
        cur = conn.cursor()
        cur.execute(sql, (name,))
        conn.commit()

        print("Delete procedure executed.")

        cur.close()
        conn.close()
    except Exception as e:
        print("Error:", e)


def delete_by_phone():
    phone = input("Enter phone: ")

    sql = "CALL delete_user(%s)"

    try:
        conn = connect()
        if conn is None:
            return
        cur = conn.cursor()
        cur.execute(sql, (phone,))
        conn.commit()

        print("Delete procedure executed.")

        cur.close()
        conn.close()
    except Exception as e:
        print("Error:", e)


def menu():
    while True:
        print("\n--- PHONEBOOK ---")
        print("1 Create table")
        print("2 Insert console")
        print("3 Insert CSV")
        print("4 Update name")
        print("5 Update phone")
        print("6 Show all")
        print("7 Search by pattern")
        print("8 Search by phone pattern")
        print("9 Delete name")
        print("10 Delete phone")
        print("11 Show with pagination")
        print("0 Exit")

        choice = input("Choose: ")

        if choice == "1":
            create_table()
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            load_from_csv(input("CSV file: "))
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
        elif choice == "11":
            query_with_pagination()
        elif choice == "0":
            break
        else:
            print("Wrong input")


if __name__ == "__main__":
    menu()
