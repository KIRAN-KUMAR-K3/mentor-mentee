# Mentor-Mentee Matching App

Welcome to the Mentor-Mentee Matching App, a Streamlit-based application for managing mentorship relationships and student details.

## Overview

This application allows mentors and students to interact through a centralized platform. It utilizes SQLite for data storage and provides functionalities such as:

- **User Authentication:** Secure login and signup for mentors and students.
- **Student Details Management:** Capture and store student information including test marks, certifications, projects, and academic issues.
- **Mentor Feedback:** Enable mentors to provide feedback to assigned students.
- **Dynamic UI:** Utilizes Streamlit's interactive components for seamless user interaction.

## Features

- **User Roles:** Supports roles for both mentors and students.
- **Database Integration:** Uses SQLite to store user accounts, student data, and mentor feedback.
- **Responsive Design:** Includes UI styling for a visually appealing experience.

## Installation

To run the application locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/KIRAN-KUMAR-K3/mentor-mentee
   cd mentor-mentee
   ```

2. **Install dependencies:**

   Ensure you have Python installed. Then install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**

   Execute the following command to start the Streamlit app:

   ```bash
   streamlit run app.py
   ```

4. **Access the app:**

   Open your web browser and go to `http://localhost:8501` to view the application.

## Usage

- **Login or Signup:** Choose to login as a mentor or student, or create a new account.
- **Student Details Form:** Students can input their personal details, test marks, certifications, projects, and academic issues.
- **Mentor Interaction:** Mentors can select students, view their details, provide feedback, and manage mentorship relationships.

## Screenshots

![Screenshot 1](<screenshot_url_1>)
![Screenshot 2](<screenshot_url_2>)
<!-- Add relevant screenshots to showcase your app -->

## Technologies Used

- Python
- Streamlit
- SQLite
- Pandas
- hashlib (for password hashing)
- requests (for URL image fetching)
- base64 (for encoding images)

## Contributing

Contributions are welcome! Please fork the repository and create a pull request for any suggested changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
