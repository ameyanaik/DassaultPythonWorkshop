import mysql.connector as connection
import pandas as pd

def main():

    my_db = connection.connect(host='localhost', database='testdata', user='ameya', passwd='ameya123')
    df = pd.read_sql("Select * from employee", my_db)
    print(df)
    my_db.close()


def read_db(dbhost, dbname, username, password, table):
    df = None
    my_db = None
    try:
        my_db = connection.connect(host=dbhost, database=dbname, user=username, passwd=password)
        df = pd.read_sql(f"Select * from {table}", my_db)
        print(df)
    except Exception as e:
        print(e)
    finally:
        my_db.close()
        return df



if __name__=="__main__":
    main()