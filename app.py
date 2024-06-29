import streamlit as st
import sqlite3
import pandas as pd
from student import student_dashboard
from mentor import mentor_dashboard

# Initialize the database
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        username TEXT PRIMARY KEY,
                        email TEXT,
                        password TEXT,
                        user_type TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS mentors (
                        name TEXT PRIMARY KEY,
                        expertise TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        name TEXT PRIMARY KEY,
                        interests TEXT,
                        mentor TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS notifications (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        student TEXT,
                        message TEXT,
                        mentor TEXT,
                        FOREIGN KEY (student) REFERENCES students (name))''')
    cursor.execute('''INSERT OR IGNORE INTO users (username, email, password, user_type)
                      VALUES ('mentor', 'mentor@example.com', 'mentor@123', 'mentor')''')
    cursor.execute('''INSERT OR IGNORE INTO mentors (name, expertise)
                      VALUES ('Mentor A', 'Math,Physics'),
                             ('Mentor B', 'Chemistry,Biology'),
                             ('Mentor C', 'Computer Science,Math')''')
    cursor.execute('''INSERT OR IGNORE INTO students (name, interests, mentor)
                      VALUES ('Student A', 'Math,Physics', 'Mentor A'),
                             ('Student B', 'Chemistry,Biology', 'Mentor B')''')
    conn.commit()
    conn.close()

def register_student():
    st.title("Student Registration")
    email = st.text_input("Email")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    register_button = st.button("Register")

    if register_button:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO users (username, email, password, user_type) VALUES (?, ?, ?, "student")', (username, email, password))
            conn.commit()
            st.success("Registration successful! Please log in.")
        except sqlite3.IntegrityError:
            st.error("Username already exists. Please choose a different username.")
        conn.close()

def login_student():
    st.title("Student Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login as Student")

    if login_button:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ? AND user_type = "student"', (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            st.session_state['username'] = username
            st.session_state['type'] = "student"
            st.success("Logged in successfully!")
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")

def login_mentor():
    st.title("Mentor Login")
    username = st.text_input("Username", value="mentor")
    password = st.text_input("Password", value="mentor@123", type="password")
    login_button = st.button("Login as Mentor")

    if login_button:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ? AND user_type = "mentor"', (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            st.session_state['username'] = username
            st.session_state['type'] = "mentor"
            st.success("Logged in successfully!")
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")

if 'username' not in st.session_state:
    init_db()
    st.sidebar.title("Login")
    user_type = st.sidebar.selectbox("User Type", ["Student", "Mentor"])

    if user_type == "Student":
        login_option = st.sidebar.radio("Login or Register", ["Login", "Register"])
        if login_option == "Login":
            login_student()
        else:
            register_student()
    else:
        login_mentor()
else:
    if st.session_state['type'] == "student":
        student_dashboard.show()
    elif st.session_state['type'] == "mentor":
        mentor_dashboard.show()
    else:
        st.error("Unknown user type")

# Logout button
if st.sidebar.button("Logout"):
    del st.session_state['username']
    del st.session_state['type']
    st.experimental_rerun()
