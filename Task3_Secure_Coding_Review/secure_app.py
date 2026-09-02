import sqlite3
import subprocess
import os

# REMEDIATION 1: Use Environment Variables for secrets
API_KEY = os.getenv("APP_API_KEY", "default_safe_value")

def get_user_data(username):
    """Fetches user data securely."""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # REMEDIATION 2: Parameterized Queries prevent SQL Injection
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    
    result = cursor.fetchall()
    conn.close()
    return result

def ping_server(ip_address):
    """Pings a server securely."""
    # REMEDIATION 3: Use subprocess without shell=True to prevent Command Injection
    try:
        subprocess.run(["ping", "-c", "1", ip_address], check=True)
    except subprocess.CalledProcessError:
        print("Ping failed.")

if __name__ == "__main__":
    print("Running secure application...")
    get_user_data("admin")
    ping_server("8.8.8.8")