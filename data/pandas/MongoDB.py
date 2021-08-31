from pymongo import MongoClient
import pandas as pd

def main():
    client = MongoClient('localhost', 27017)

    my_db = client['Employee']
    my_collection = my_db['personalinfo']

    list_documents = my_collection.find()

    df = pd.DataFrame(list_documents)

    print(df)


def read_db(dbhost, dbport, collection):
    client = MongoClient(dbhost, dbport)
    my_db = client['Employee']
    my_collection = my_db[collection]
    list_documents = my_collection.find()
    df = pd.DataFrame(list_documents)
    return df


if __name__ == "__main__":
    main()
