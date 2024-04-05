# Objective:
# The aim of this assignment is to reinforce your understanding of Python's interaction with SQL databases, focusing on CRUD (Create, Read, Update, Delete) operations in the context of a gym's membership and workout session management system. You will work with two tables: 'Members' and 'WorkoutSessions'.

# Problem Statement:
# You are tasked with developing a Python application to manage a gym's database. The database consists of 'Members' and 'WorkoutSessions' tables. Your role is to implement various functions to add, retrieve, update, and delete records in these tables, ensuring data integrity and efficient data handling.

# Task 1: Add a Member

#     Write a Python function to add a new member to the 'Members' table in the gym's database.

#     # Example code structure
#     def add_member(id, name, age, trainer_id):
#         # SQL query to add a new member
#         # Error handling for duplicate IDs or other constraints

#     Expected Outcome:
#     A Python function that successfully adds a new member to the 'Members' table in the gym's database. The function should handle errors gracefully, such as duplicate member IDs or violations of other constraints.

from connect_database import connect_database
import mysql.connector
from mysql.connector import Error

def add_member(id, name, age, trainer_id):
    
    conn = connect_database()

    if conn is not None:
        try:
            cursor = conn.cursor()
            
            new_member = [id, name, age, trainer_id]

            query = "INSERT INTO Members (id, name, age, trainer_id) VALUES (%s, %s, %s, %s)"

            cursor.execute(query, new_member)
            conn.commit()
            print("New member added succesfully")

        except Error as e:
            print(f"Error: {e}")

        finally:
            print("Closing cursor and connection...")
            cursor.close()
            conn.close()

add_member(5, "Vitorio Storraro", 72, 3)



# Task 2: Add a Workout Session

#     Develop a Python function to add a new workout session to the 'WorkoutSessions' table for a specific member.

#     # Example code structure
#     def add_workout_session(member_id, date, duration_minutes, calories_burned):
#         # SQL query to add a new workout session
#         # Error handling for invalid member ID or other constraints

#     Expected Outcome:
#     A Python function that adds a new workout session to the 'WorkoutSessions' table in the gym's database for a specific member. The function should handle errors gracefully, such as invalid member IDs or violations of other constraints.



def add_workout_session(session_id, member_id, date, time, activity):
    
    conn = connect_database()

    if conn is not None:
        try:
            cursor = conn.cursor()
            
            new_session = [session_id, member_id, date, time, activity]

            query = "INSERT INTO WorkoutSessions (session_id, member_id, session_date, session_time, activity) VALUES (%s, %s, %s, %s, %s)"

            cursor.execute(query, new_session)
            conn.commit()
            print("New member added succesfully")

        except Error as e:
            print(f"Error: {e}")

        finally:
            print("Closing cursor and connection...")
            cursor.close()
            conn.close()

add_workout_session(5, 5, "2024-04-06", "11:30AM", "jump rope")

# Task 3: Updating Member Information

#     Implement a function to update the age of a member. Ensure that your function checks if the member exists before attempting the update.

#     # Example code structure
#     def update_member_age(member_id, new_age):
#         # SQL query to update age
#         # Check if member exists
#         # Error handling

#     Expected Outcome:
#     A Python function that updates the age of a member and handles cases where the member does not exist.

def update_member_age(member_id, new_age):
    
    conn = connect_database()

    if conn is not None:
        try:
            cursor = conn.cursor()
            
            member_update = [new_age, member_id]

            query = "UPDATE Members SET age = %s WHERE id = %s"

            cursor.execute(query, member_update)
            conn.commit()
            print("Member updated succesfully")

        except Error as e:
            print(f"Error: {e}")

        finally:
            print("Closing cursor and connection...")
            cursor.close()
            conn.close()

update_member_age(1, 22)

# Task 4: Delete a Workout Session

#     Create a Python function to delete a workout session based on its session ID. Include error handling for cases where the session ID does not exist.

#     # Example code structure
#     def delete_workout_session(session_id):
#         # SQL query to delete a session
#         # Error handling for non-existent session ID

#     Expected Outcome:
#     A Python function that can delete a workout session using its session ID, with proper error handling for invalid IDs.

def delete_workout_session(session_id):
    
    conn = connect_database()

    if conn is not None:
        try:
            cursor = conn.cursor()
            
            session_del = [session_id]

            query = "DELETE FROM WorkoutSessions WHERE session_id = %s"

            cursor.execute(query, session_del)
            conn.commit()
            print("Session deleted succesfully")

        except Error as e:
            print(f"Error: {e}")

        finally:
            print("Closing cursor and connection...")
            cursor.close()
            conn.close()

delete_workout_session(5)

# Submission Guidelines:

#     Submit a Python script (.py file) containing all the functions for the tasks.
#     Include comments in your code to explain your logic and SQL queries.
#     Ensure your script handles errors gracefully and provides meaningful output.
