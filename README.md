## Student Performance Management System

## Project Overview

The Student Performance Management System (SPMS) is a software application designed to help educational institutions track and analyze student academic performance. 
This system allows administrators and teachers to manage student records, analyze performance trends, and generate insightful reports.
With Tkinter for the GUI, MySQL for the database, and Pandas/NumPy for data analysis, this system provides an efficient and user-friendly solution to monitor student progress.

![istockphoto-1488294044-612x612](https://github.com/user-attachments/assets/948c644c-282b-4e93-998a-377d4a74eb0e)



## Objectives

The primary aim of this project is to:

  Provide a user-friendly interface to add, update, and delete student records.
  Analyze student performance trends using statistical computations.
  Display performance results visually using tables and graphs.
  Store and retrieve student data efficiently using MySQL.
  Enable exporting reports to CSV for further analysis.

## System Requirements


1. Functional Requirements

The system must support the following functions:

  User Authentication: Secure login and signup.
  Student Management: Add, update, delete, and view student records.

## Performance Analysis:

  Calculate average marks, highest/lowest scores.
  Detect trends in student performance across semesters.
  Reporting: Export performance data to CSV. 
  Visualization: Represent student data using tables and graphs.

2. Non-Functional Requirements

    Scalability: The system should efficiently handle large datasets.
    Code Modularity: Implement Object-Oriented Programming (OOP) principles for better code organization.
    Efficient Querying: Optimize MySQL queries for fast data retrieval.

## System Modules

# 1. User Authentication

![Screenshot 2025-04-01 020547](https://github.com/user-attachments/assets/23ac25f7-4eea-4e56-a596-64f004d25b8b)


 Users (administrators or teachers) must log in using a username and password.
 New users can sign up, and credentials are stored securely in MySQL.
 Password encryption and validation will be implemented.

# 2. Student Management

  sers can add, edit, delete, and view student records.
  Each student record includes details like Name, Roll Number, Course, Semester, and Marks.

# 3. Performance Analysis

  The system computes:
  Average marks of students.
  Highest and lowest scores in each subject.
  Pass percentage of students.
  Performance trends over multiple semesters using Pandas/NumPy.

# 4. Reporting

  Users can export student performance data in CSV format for further review.
  Reports will include student details, scores, and statistical insights.

# 5. Visualization

  Performance data will be displayed as:

  Tables (showing raw data).
  Graphs (bar charts, line graphs, etc.) for better insights.

## Workflow of the System

## User Login

![Screenshot 2025-04-01 020547](https://github.com/user-attachments/assets/ffecb5c8-0776-48b6-85f2-27432e79d965)


  The user enters login credentials.
  The system verifies credentials from the MySQL database.

## Dashboard

![Screenshot 2025-04-01 020339](https://github.com/user-attachments/assets/eed155b8-02a1-42e9-b716-1e03dddc04ab)


  Upon login, users see options to manage students, analyze performance, and generate reports.
  Student Actions
  Users can add new students, update details, or delete records.

## Performance Analysis

![Screenshot 2025-04-01 020351](https://github.com/user-attachments/assets/21eb7401-66af-4d1f-ba06-d0bdb86cb04d)


  The system calculates average marks, pass percentage, and trends.       
  Graphical representation of student performance.

## Reports

![Screenshot 2025-04-01 020507](https://github.com/user-attachments/assets/37c5902e-7cef-4d08-8933-7ec84392cb38)


  Users can export reports as CSV files for record-keeping.

## Technologies Used

   Frontend (GUI): Tkinter (Python GUI Library)
   Backend (Database): MySQL
   Data Processing & Analysis: Pandas, NumPy
   Visualization: Matplotlib, Tkinter Tables

## Conclusion

 This Student Performance Management System is a powerful tool for educational institutions to store, manage, analyze, and visualize student performance data. 
 By leveraging Python’s data analysis capabilities and MySQL’s  robust data storage, this system provides an efficient, user-friendly, and insightful solution for academic performance tracking.
