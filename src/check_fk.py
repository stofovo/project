import sqlite3

conn = sqlite3.connect("db/shoe_store.sqlite")
conn.execute("PRAGMA foreign_keys = ON;")
cur = conn.cursor()

try:
    cur.execute("""
        INSERT INTO users (last_name, first_name, login, role_id)
        VALUES ('Тестов', 'Тест', 'test_login', 99);
    """)
    conn.commit()
    print("ОШИБКА: вставка прошла, FK не работает!")
except sqlite3.IntegrityError as e:
    print("OK: ссылочная целостность работает —", e)
finally:
    conn.close()