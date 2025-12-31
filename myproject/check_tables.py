import sqlite3
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from django.conf import settings

db_path = str(settings.DATABASES['default']['NAME'])
print(f'Checking database: {db_path}')

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Check what tables exist
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print('Tables in database:')
for table in tables:
    print(f'  - {table[0]}')

# Specifically check for auth_user
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='auth_user';")
auth_user_exists = cursor.fetchone()

print()
if auth_user_exists:
    print('✅ auth_user table EXISTS')
    # Check how many users are in it
    cursor.execute('SELECT COUNT(*) FROM auth_user;')
    user_count = cursor.fetchone()[0]
    print(f'Users in table: {user_count}')

    # Show the users
    cursor.execute('SELECT username, email, is_superuser FROM auth_user;')
    users = cursor.fetchall()
    print('Users:')
    for user in users:
        print(f'  - {user[0]} ({user[1]}) - Superuser: {user[2]}')
else:
    print('❌ auth_user table DOES NOT EXIST')

conn.close()
