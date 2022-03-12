from sql_connection import create_sql_connection


def get_all_exercises(connection):
    cursor=connection.cursor()

    query="SELECT exercises.exercise_id,exercises.exercise_name,exercises.muscle,exercises.type_id, exercise_type.type FROM exercises inner join exercise_type on exercises.type_id=exercise_type.type_id"

    cursor.execute(query)

    response=[]

    for (exercise_id,exercise_name,muscle,type_id,type) in cursor:
        response.append({
            "exercise_id":exercise_id,
            "exercise_name":exercise_name,
            "muscle":muscle,
            "type_id":type_id,
            "type":type
            })

    return response



def insert_exercise(connection,exercise):
    cursor=connection.cursor()

    query=f"INSERT INTO exercises(exercise_name,muscle,type_id) VALUES(%s,%s,%s)"

    data=(exercise["exercise_name"],exercise["muscle"],exercise["type_id"])

    cursor.execute(query,data)

    connection.commit()

    return cursor.lastrowid


def edit_exercise(connection,column,value,exercise_id):
    cursor=connection.cursor()

    if type(value)==str:
        query=f"UPDATE exercises SET {column}='{value}' WHERE exercise_id={exercise_id}"
    elif type(value)==int:
        query=f"UPDATE exercises SET {column}={value} WHERE exercise_id={exercise_id}"

    cursor.execute(query)

    connection.commit()

    new_query=f"SELECT * FROM exercises where exercise_id={exercise_id}"
    
    cursor.executemany(new_query)

    response=[]

    for (exercise_id,exercise_name,muscle,type_id) in cursor:
        response.append({
            "exercise_id":exercise_id,
            "exercise_name":exercise_name,
            "muscle":muscle,
            "type_id":type_id
            })

    return response





def delete_exercise(connection,exercise_id):

    cursor=connection.cursor()

    query=f"DELETE FROM exercises WHERE exercise_id={exercise_id}"

    cursor.execute(query)

    connection.commit()

    return "exercise deleted!"


if __name__=="__main__":
    connection=create_sql_connection()
    print(get_all_exercises(connection))
    # print(insert_exercise(connection,{
    #     "exercise_name":"squats",
    #     "muscle":"quads",
    #     "type_id":2
    # }))
    print(delete_exercise(connection,8))
    # print(edit_exercise(connection,"exercise_name","bench press",7))


    