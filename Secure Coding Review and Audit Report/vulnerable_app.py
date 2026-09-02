import sqlite3
import os

# VULNERABILITY 1: Hardcoded Secret
API_KEY = "12345-SECRET-KEY"

def get_user_data(username):
    """Fetches user data from the database."""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # VULNERABILITY 2: SQL Injection
    # Directly concatenating user input into the SQL query
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    
    result = cursor.fetchall()
    conn.close()
    return result

def ping_server(ip_address):
    """Pings a server to check if it is alive."""
    # VULNERABILITY 3: Command Injection
    # Directly passing user input to the operating system shell
    command = "ping -c 1 " + ip_address
    os.system(command)

if __name__ == "__main__":
    print("Running vulnerable application...")
    # Simulating dangerous user input
    get_user_data("admin' OR '1'='1") 
    ping_server("8.8.8.8; ls -la")