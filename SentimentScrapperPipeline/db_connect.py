import pandas as pd
from sqlalchemy import create_engine
import pymysql



def table_load():
    connection = pymysql.connect(
            host='localhost',    # Change to your MySQL server host
            user='root',         # Replace with your MySQL username
            password='12345678'  # Replace with your MySQL password
        )



    # Step 2: Create a new database
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS movie_reviews")
    print("Database `movie_reviews` created or already exists")
    connection.database = 'movie_reviews'
    create_table_query = """
    CREATE TABLE IF NOT EXISTS movie_reviews.reviews (
        id INT AUTO_INCREMENT PRIMARY KEY,
        names VARCHAR(255) NOT NULL,
        comments VARCHAR(255) NOT NULL,
        sentiment VARCHAR(100)
    )
    """
    cursor.execute(create_table_query)
    print("Table `reviews` created or already exists")
    df=pd.read_csv('/home/khalil/vs_workspace/ETL_project/data_with_sent1.csv')
    
    
    #Import the SQLCHEMY because pymsql didn't recognize table or connection while inserting data
    # IMPORT THE SQALCHEMY LIBRARY's CREATE_ENGINE METHOD
    from sqlalchemy import create_engine

    # DEFINE THE DATABASE CREDENTIALS
    user = 'root'
    password = "12345678"
    host = '127.0.0.1'
    port = 3306
    database = 'movie_reviews'
    table_name='reviews'
    # PYTHON FUNCTION TO CONNECT TO THE MYSQL DATABASE AND
    # RETURN THE SQLACHEMY ENGINE OBJECT
    def get_connection():
        return create_engine(
            url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
                user, password, host, port, database
            )
        )


    if __name__ == '__main__':

        try:
            # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
            engine = get_connection()
            print(
                f"Connection to the {host} for user {user} created successfully.")
        except Exception as ex:
            print("Connection could not be made due to the following error: \n", ex)

    try:
        df.to_sql(table_name, con=engine, if_exists='append', index=False)  # Use the SQLAlchemy engine
        print(f"Data successfully inserted into the '{table_name}' table.")
    except Exception as e:
        print(f"An error occurred: {e}")


