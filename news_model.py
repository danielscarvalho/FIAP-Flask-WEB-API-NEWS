import oracledb
import os

from datetime import datetime

import uuid

# CRUD

connection = None # Global variable

def get_cursor():
    
    db_user = os.environ.get('FIAP_ORA') # usuário
    db_key = os.environ.get('FIAP_KEY')  # senha
    cursor = None

    try:
        connection = oracledb.connect(
            user = db_user,
            password = db_key,
            dsn="oracle.fiap.com.br/orcl")
        
        
        cursor = connection.cursor()
        
    except Exception as err:
        print("Ops!! - Connect to DB - " + str(datetime.now()) + " - " + str(err))
        return None

    return cursor


def create(data):

    try:

        cursor = get_cursor()
        
        print("Successfully connected to Oracle Database: Create - " + str(datetime.now()))

        data["uuid"] = str(uuid.uuid4())

        SQL=f"""insert into news 
               (id,
                title, 
                description, 
                source_url, 
                image_url,
                uuid,
                published_dt,
                source,
                author) 
                values
               ({data["id"]},
                '{data["title"]}',
                '{data["description"]}',
                '{data["source_url"]}',
                '{data["image_url"]}',
                '{data["uuid"]}',
                to_date('{data["published_dt"]}','YYYY-MM-DD'),
                '{data["source"]}',
                '{data["author"]}')"""

        cursor.execute(SQL)
        cursor.execute("commit")

        if connection != None:
            connection.commit()
            connection.close()

    except Exception as err:
        print("Ops!! - Create - " + str(datetime.now()) + " - " + str(err))
        print("SQL: ", SQL)

def read(data):

    data_out = {"now": str(datetime.now())}

    try:

        cursor = get_cursor()

        print("Successfully connected to Oracle Database: Read - " + str(datetime.now()))

        SQL=f"""select *
                  from news
                 where id = {data["id"]}"""

        for registro in cursor.execute(SQL):
            data_out["id"] = registro[0]
            data_out["title"] = registro[1]
            data_out["description"] = registro[2]
            data_out["source_url"] = registro[3]
            data_out["image_url"] = registro[4]
            data_out["uuid"] = registro[5]
            data_out["published_dt"] = registro[6]
            data_out["source"] = registro[7]
            data_out["author"] = registro[8]

        if connection != None:
            connection.close()

    except Exception as err:
        print("Ops!! - Read - " + str(datetime.now()) + " - " + str(err))

    return data_out

def delete(data):

    out_message = {"now": str(datetime.now())}

    try:

        cursor = get_cursor()

        print("Successfully connected to Oracle Database: Delete - " + str(datetime.now()))

        SQL=f"""delete from news
                where id = {data["id"]}"""
       
        cursor.execute(SQL)
        cursor.execute("commit")

        if connection != None:
            connection.commit()
            connection.close()

    except Exception as err:
     
        print("Ops!! - Delete - " + str(datetime.now()) + " - " + str(err))
        print("SQL: ", SQL)
        out_message["error": str(err)]

    return out_message

def update(data):
    # Alunos implementar o UPDATE
    pass

def get_db_info():

    out_message = {"service_time":str(datetime.now())}

    try:

        cursor = get_cursor()

        print("Successfully connected to Oracle Database: DB Info - " + str(datetime.now()))
        
        SQL=f"""SELECT version, SYSDATE db_time, USER, 'ok' STATUS FROM V$INSTANCE"""  

        for registro in cursor.execute(SQL):
            out_message["db_version"] = str(registro[0])
            out_message["now"] = str(registro[1])
            out_message["status"] = registro[2]

        if connection != None:
           connection.close()

    except Exception as err:
        print("Ops!! - DB Info - " + str(datetime.now()) + " - " + str(err))
        out_message["error"] = str(err)

    return out_message

