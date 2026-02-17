#!/usr/bin/env python3
"""
Debug script to check what API key Django is reading
"""

import os
from decouple import config

print("🔍 Debugging API Key Reading...")
print("=" * 50)

# Check if .env file exists
if os.path.exists('.env'):
    print("✅ .env file exists")
    
    # Read the .env file directly
    with open('.env', 'r') as f:
        env_content = f.read()
        print(f"📄 .env file content:")
        print(env_content)
        print("-" * 30)
else:
    print("❌ .env file not found")

# Try to read with python-decouple
try:
    api_key = config('OPENWEATHER_API_KEY', default='NOT_FOUND')
    print(f"🔑 API Key from config(): {api_key}")
    print(f"📏 API Key length: {len(api_key)}")
    
    if api_key == 'NOT_FOUND':
        print("❌ API key not found by python-decouple")
    elif len(api_key) < 20:
        print("⚠️ API key seems too short")
    else:
        print("✅ API key looks valid")
        
except Exception as e:
    print(f"❌ Error reading API key: {e}")

print("=" * 50)
