# Login Management System

## Overview
This project is a **Login Management System** built using **Python** and **MySQL**. It provides a simple way to register, log in, update information, and delete user accounts. The system also allows admin users to manage all users, including viewing, deleting, and updating user information.

## Features
- **User Registration**: Allows new users to register with a username and password.
- **User Login**: Verifies user credentials for secure login.
- **Update User Information**: Enables users to update their password.
- **Delete User**: Provides functionality to delete a user from the system.
- **Show User Information**: Displays user information like username and password.
- **Show All Users**: Admins can view all registered users in the system.
- **Admin Management**: Admins can update user information and delete users.

## Technologies Used
- **Python**: Programming language used to implement the system logic.
- **MySQL**: Database used to store user information (username and password).
- **mysql-connector-python**: Python MySQL driver used to interact with the MySQL database.

## Structure
- **Db_Helper.py**: Connects to MySQL and executes queries related to database operations.
- **Register.py**: Handles user registration by inserting new users into the database.
- **Login.py**: Manages user login by verifying the credentials against the database.
- **Update_Info.py**: Allows users to update their password and other information.
- **Show_User_Info.py**: Displays user details (e.g., username and password) for the logged-in user.
- **Delete_User.py**: Provides the functionality to delete a user from the system.
- **Show_All_Users.py**: Allows admins to view all registered users in the system.
- **User.py**: Implements user functionalities like registration, login, and updating information.
- **Admin.py**: Implements admin functionalities such as managing users (deleting and updating).
- **Main.py**: The entry point of the application to interact with the system.
- **requirements.txt**: Lists the required dependencies and libraries for the project.
- **README.md**: Documentation file providing an overview of the project, features, technologies used, and setup instructions.
