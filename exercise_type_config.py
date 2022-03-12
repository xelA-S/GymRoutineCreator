from sql_connection import create_sql_connection

def get_all_exercise_types(connection):
    cursor=connection.cursor()

    query="SELECT * FROM exercise_type"

    cursor.execute(query)

    response=[]

    for (type_id,type) in cursor:
        response.append({
            "type_id":type_id,
            "type":type
        })

    return response


def add_type(connnection,value):
    cursor=connection.cursor()

    query=f"INSERT INTO exercise_type(type) VALUES({value})"

    cursor.execute(query)

    connection.commit()

    return cursor.lastrowid


if __name__=="__main__":
    connection=create_sql_connection()
    print(get_all_exercise_types(connection))

