# https://pynative.com/python-database-programming-exercise-with-solution/

import sqlite3


def populate_db():
    print("populating the db")
    try:
        connection = get_connection()

        with connection:
            cursor = connection.cursor()

            cursor.execute(
                "CREATE TABLE Hospital (Hospital_Id INTEGER NOT NULL PRIMARY KEY, Hospital_Name TEXT NOT NULL,  Bed_Count INTEGER NOT NULL);"
            )

            cursor.execute(
                """
                    INSERT INTO Hospital (Hospital_Id, Hospital_Name, Bed_Count) 
                    VALUES 
                    ('1', 'Mayo Clinic', 200), 
                    ('2', 'Cleveland Clinic', 400), 
                    ('3', 'Johns Hopkins', 1000), 
                    ('4', 'UCLA Medical Center', 1500);
                """
            )

            cursor.execute(
                """
                CREATE TABLE Doctor (
                     Doctor_Id INTEGER NOT NULL PRIMARY KEY, 
                     Doctor_Name TEXT NOT NULL, 
                     Hospital_Id INTEGER NOT NULL, 
                     Joining_Date TEXT NOT NULL, 
                     Speciality TEXT NOT NULL, 
                     Salary INTEGER NOT NULL,
                     Experience INTEGER
                     );
                """
            )

            cursor.execute(
                """
                    INSERT INTO Doctor (Doctor_Id, Doctor_Name, Hospital_Id, Joining_Date, Speciality, Salary, Experience) 
                    VALUES 
                    ('101', 'David', '1', '2005-2-10', 'Pediatric', '40000', NULL), 
                    ('102', 'Michael', '1', '2018-07-23', 'Oncologist', '20000', NULL), 
                    ('103', 'Susan', '2', '2016-05-19', 'Garnacologist', '25000', NULL), 
                    ('104', 'Robert', '2', '2017-12-28', 'Pediatric ', '28000', NULL), 
                    ('105', 'Linda', '3', '2004-06-04', 'Garnacologist', '42000', NULL), 
                    ('106', 'William', '3', '2012-09-11', 'Dermatologist', '30000', NULL), 
                    ('107', 'Richard', '4', '2014-08-21', 'Garnacologist', '32000', NULL), 
                    ('108', 'Karen', '4', '2011-10-17', 'Radiologist', '30000', NULL);
                """
            )
    except (Exception, sqlite3.Error) as error:
        print("Error while getting data", error)


def get_connection():
    connection = sqlite3.connect("python_db.db")
    return connection


def close_connection(connection):
    if connection:
        connection.close()


def read_database_version():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("select sqlite_version();")
        db_version = cursor.fetchone()
        print("You are connecred to Sqlite version:", db_version)
        close_connection(connection)
    except (Exception, sqlite3.Error) as error:
        print("Error while getting data", error)


def exercise_2(doctor_id, hospital_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM Doctor WHERE Doctor_Id = {doctor_id}".format(doctor_id=doctor_id)
    )
    doctor_record = cursor.fetchall()

    cursor.execute(
        "SELECT * FROM Hospital where Hospital_Id = {hospital_id}".format(
            hospital_id=hospital_id
        )
    )
    hospital_record = cursor.fetchall()

    print("printing doctor record")
    for r in doctor_record:
        print(f"doctor id: {r[0]}")
        print(f"doctor name: {r[1]}")
        print(f"hospital id: {r[2]}")
        print(f"joining data: {r[3]}")
        print(f"specility: {r[4]}")
        print(f"salary: {r[5]}")
        print(f"experience: {r[6]}")

    print("printing hospital record")
    for r in hospital_record:
        print(f"hospital id: {r[0]}")
        print(f"hospital name: {r[1]}")
        print(f"hospital number of beds: {r[2]}")

def exercise_3(speciality: str):
    connection = get_connection()
    with connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Doctor WHERE Speciality = "{speciality}"'.format(speciality=speciality))
        data = cursor.fetchall()
        for doctor in data:
            print(doctor)

# populate_db()

# print("Question 1: print database version")
# read_database_version()


exercise_3(speciality="Garnacologist")