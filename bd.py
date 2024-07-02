import sqlite3


def create_database():
    # Подключение к базе данных (файл будет создан, если не существует)
    conn = sqlite3.connect("bd.sqlite")
    cursor = conn.cursor()

    # Создание таблицы для хранения данных пользователей
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            username TEXT,
            first_name TEXT,
            last_name TEXT
        )
    """
    )

    # Сохранение изменений и закрытие подключения
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()
