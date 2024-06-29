import streamlit as st
import pandas as pd
import sqlite3

def get_mentors(interests):
    conn = sqlite3.connect('users.db')
    query = f"SELECT * FROM mentors WHERE expertise IN ({','.join(['?' for _ in interests])})"
    mentors = pd.read_sql_query(query, conn, params=interests)
    conn.close()
    return mentors

def get_notifications(student_name):
    conn = sqlite3.connect('users.db')
    query = "SELECT * FROM notifications WHERE student = ?"
    notifications = pd.read_sql_query(query, conn, params=(student_name,))
    conn.close()
    return notifications

def show():
    st.title("Student Dashboard")
    
    interests = st.multiselect("Select your interests", ["Math", "Physics", "Chemistry", "Biology", "Computer Science"])
    
    if interests:
        st.subheader("Available Mentors")
        mentors = get_mentors(interests)
        for index, row in mentors.iterrows():
            st.write(f"**{row['name']}** - Expertise: {row['expertise']}")
            st.button(f"Request meeting with {row['name']}")
    
    st.subheader("Progress and Goals (Placeholder)")
    st.write("Progress tracking and goal setting functionalities to be implemented.")
    
    st.subheader("Notifications")
    student_name = st.session_state['username']
    notifications = get_notifications(student_name)
    if not notifications.empty:
        for index, row in notifications.iterrows():
            st.write(f"Notification: {row['message']}")
    else:
        st.write("No notifications")
