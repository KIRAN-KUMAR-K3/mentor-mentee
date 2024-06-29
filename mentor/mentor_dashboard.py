import streamlit as st
import pandas as pd
import sqlite3

def get_students():
    conn = sqlite3.connect('users.db')
    query = "SELECT * FROM students"
    students = pd.read_sql_query(query, conn)
    conn.close()
    return students

def add_notification(student_name, message, mentor_name):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notifications (student, message, mentor) VALUES (?, ?, ?)", (student_name, message, mentor_name))
    conn.commit()
    conn.close()

def show():
    st.title("Mentor Dashboard")
    
    st.subheader("All Students")
    students = get_students()
    for index, row in students.iterrows():
        st.write(f"**{row['name']}** - Interests: {row['interests']} - Mentor: {row['mentor']}")
    
    st.subheader("Assign Projects/Assignments")
    student_name = st.selectbox("Select Student", students['name'])
    message = st.text_area("Project/Assignment Details")
    if st.button("Assign"):
        mentor_name = st.session_state['username']
        add_notification(student_name, message, mentor_name)
        st.success("Project/Assignment assigned successfully!")
    
    st.subheader("Upcoming Meetings (Placeholder)")
    st.write("Functionality to view upcoming meetings to be implemented.")
    
    st.subheader("Provide Feedback (Placeholder)")
    st.write("Functionality to provide feedback to students to be implemented.")
