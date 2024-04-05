# Objective:
# The goal of this assignment is to advance your SQL querying skills within Python, focusing on specific SQL 
# functions and clauses like DISTINCT, COUNT, and BETWEEN. You will be working with the same gym database as in 
# the previous assignment, comprising the Members and WorkoutSessions tables.

# Problem Statement:
# As a part of the gym's management team, you need to conduct an in-depth analysis of the membership data. 
# Your task is to develop Python functions that execute advanced SQL queries for distinct department identification, 
# employee count in each department, and age-based employee filtering.

# Task 1: SQL DISTINCT Usage

#     Problem Statement:

#     Identify the distinct trainers working with gym members.

#     Expected Outcome:

#     A list of unique trainer IDs from the Members table.

#     Example Code Structure:

#     def list_distinct_trainers():
#         # SQL query using DISTINCT
#         # Execute and fetch results

from connect_database import connect_database
import mysql.connector
from mysql.connector import Error

# def list_distinct_trainers():

#     conn = connect_database()

#     if conn is not None:
#         try:
#             cursor = conn.cursor()
            
#             #new_member = [id, name, age, trainer_id]

#             query = "SELECT DISTINCT trainer_id FROM Members"

#             cursor.execute(query)
#             for trainer in cursor.fetchall():
#                 print(trainer)

#         except Error as e:
#             print(f"Error: {e}")

#         finally:
#             print("Closing cursor and connection...")
#             cursor.close()
#             conn.close()

# list_distinct_trainers()

# Task 2: SQL COUNT Functionality

#     Problem Statement:

#     Count the total number of members assigned to each trainer. Focus on understanding the GROUP BY clause.

#     Expected Outcome:

#     A count of members grouped by their trainer IDs.

#     Example Code Structure:

#     def count_members_per_trainer():
#         # SQL query using COUNT and GROUP BY
#         # Execute and fetch results

def count_members_per_trainer():

    conn = connect_database()

    if conn is not None:
        try:
            cursor = conn.cursor()
            
            #new_member = [id, name, age, trainer_id]

            query = "SELECT COUNT(id), trainer_id FROM Members GROUP BY trainer_id"

            cursor.execute(query)
            for members in cursor.fetchall():
                print(members)

        except Error as e:
            print(f"Error: {e}")

        finally:
            print("Closing cursor and connection...")
            cursor.close()
            conn.close()

count_members_per_trainer()

# Task 3: SQL BETWEEN Usage

#     Problem Statement:

#     Retrieve the details of members whose ages fall between 25 and 30.

#     Expected Outcome:

#     A list of members (including their names, ages, and trainer IDs) who are between the ages of 25 and 30.

#     Example Code Structure:

#     def get_members_in_age_range(start_age, end_age):
#         # SQL query using BETWEEN
#         # Execute and fetch results

# Note: The database structure used for this assignment is the same as the previous one, consisting of 
# the Members and WorkoutSessions tables.

def get_members_in_age_range(start_age, end_age):

    conn = connect_database()

    if conn is not None:
        try:
            cursor = conn.cursor()
            
            age_group = [start_age, end_age]

            query = "SELECT * FROM Members WHERE age BETWEEN %s AND %s"

            cursor.execute(query, age_group)
            for members in cursor.fetchall():
                print(members)

        except Error as e:
            print(f"Error: {e}")

        finally:
            print("Closing cursor and connection...")
            cursor.close()
            conn.close()

#get_members_in_age_range(25, 30)
#No members in this age range so using this other range
get_members_in_age_range(22, 72)

# Submission Guidelines:

#     Submit a Python script (.py file) containing the functions for the specified tasks.
#     Ensure your code is well-commented to explain the logic and SQL queries used.
#     Make sure your script includes error handling and provides clear output for each task.
