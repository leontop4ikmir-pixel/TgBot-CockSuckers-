import sqlite3
import datetime

def create_database():
    """Создает базу данных и таблицу"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            first_name TEXT,
            join_date TEXT
        )
    ''')
    
    conn.commit()
    conn.close()
    print("✅ База данных создана!")

def add_user(user_id, username, first_name):
    """Добавляет пользователя в БД"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT OR IGNORE INTO users 
        (user_id, username, first_name, join_date) 
        VALUES (?, ?, ?, ?)
    ''', (user_id, username, first_name, datetime.datetime.now().isoformat()))
    
    conn.commit()
    conn.close()
    return True

def get_user(user_id):
    """Находит пользователя по ID"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    user = cursor.fetchone()
    
    conn.close()
    return user

def get_all_users():
    """Получает всех пользователей"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    
    conn.close()
    return users

def get_users_count():
    """Возвращает количество пользователей"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT COUNT(*) FROM users')
    count = cursor.fetchone()[0]
    
    conn.close()
    return count

create_database()



#сделал изменения СУКА БЛЯЯЯЯТЬ
#я еблан бля