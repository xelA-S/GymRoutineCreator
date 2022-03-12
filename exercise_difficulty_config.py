from sql_connection import create_sql_connection

def get_all_difficulties(connection):
    cursor=connection.cursor()

    query="SELECT * FROM exercise_difficulty"

    cursor.execute(query)

    response=[]

    for (difficulty_id,difficulty) in cursor:
        response.append({
            "difficulty_id":difficulty_id,
            "difficulty":difficulty
        })

    return response


def add_difficulty(connection,difficulty):
    cursor=connection.cursor()

    query=f"INSERT INTO exercise_difficulty(difficulty) VALUES ('{difficulty}')"

    cursor.execute(query)

    connection.commit()

    return cursor.lastrowid


def delete_difficulty(connection,difficulty_id):
    cursor=connection.cursor()

    query=f"DELETE FROM exercise_difficulty WHERE difficulty_id={difficulty_id}"

    cursor.execute(query)

    connection.commit()

    return "diffculty deleted!"    



if __name__=="__main__":
    connection=create_sql_connection()
    # print(get_all_difficulties(connection))
    # print(add_difficulty(connection,"extreme"))
    print(delete_difficulty(connection,4))