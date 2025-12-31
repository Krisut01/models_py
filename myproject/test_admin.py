import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User

# Test admin login
client = Client()

print("Testing admin login...")

# Try to login
response = client.post('/admin/login/', {
    'username': 'admin',
    'password': 'admin123',  # You might need to change this to your actual password
    'next': '/admin/'
})

print(f"Login response status: {response.status_code}")
print(f"Response content preview: {response.content[:200]}...")

if response.status_code == 302:  # Redirect means login successful
    print("✅ Login successful!")
else:
    print("❌ Login failed")

# Test direct database access
print("\nTesting direct database access:")
try:
    user = User.objects.get(username='admin')
    print(f"✅ User found: {user.username} - Superuser: {user.is_superuser}")
except User.DoesNotExist:
    print("❌ User not found in database")
except Exception as e:
    print(f"❌ Database error: {e}")

# Test admin URL access
print("\nTesting admin URL access:")
response = client.get('/admin/')
print(f"Admin page response status: {response.status_code}")
if 'login' in str(response.content).lower():
    print("Admin page requires login (expected)")
else:
    print("Admin page accessible (unexpected)")
