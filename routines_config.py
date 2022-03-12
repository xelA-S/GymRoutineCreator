from datetime import datetime
from sql_connection import create_sql_connection

def get_all_routines(connection):
    cursor=connection.cursor()

    query="SELECT * FROM routines"

    cursor.execute()

    response=[]

    for (routine_id,routine_name,datetime) in cursor:
        response.append({
            "routine_id":routine_id,
            "routine_name":routine_name,
            "datetime":datetime
        })

    return response



def add_new_routine(connection,routine):
    cursor=connection.cursor()

    query="INSERT INTO routines(routine_name,date_created) VALUES(%s,%s)"

    data=(routine["routine_name"],datetime.now())

    cursor.execute(query,data)

    connection.commit()

    routine_id=cursor.lastrowid

    
    
    
    exercise_details_query=f"INSERT INTO exercise_details(exercise_id,reps,sets,weight,weight_unit_id,difficulty_id) VALUES(%s,%s,%s,%s,%s,%s)"

    exercise_details_data=[]

    for exercise_details_item in routine["exercise_details"]:
        exercise_details_data.append([
            int(exercise_details_item["exercise_id"]),
            int(exercise_details_item["reps"]),
            int(exercise_details_item["sets"]),
            int(exercise_details_item["weight"]),
            int(exercise_details_item["weight_unit_id"]),
            int(exercise_details_item["difficulty_id"])
            

        ])

    cursor.executemany(exercise_details_query,exercise_details_data)

    connection.commit()

    return routine_id


def delete_routine(connection,routine_id):
    cursor=connection.cursor()

    query=f"DELETE FROM exercises WHERE exercise_id={routine_id}"

    cursor.execute(query)

    connection.commit()

    return "routine deleted!"



if __name__=="__main__":
    connection=create_sql_connection()
    # print(get_all_routines(connection))
    print(add_new_routine(connection,{
        "routine_name":"first routine",
        "exercise_details":[
            {
                "exercise_id":1,
                "reps":5,
                "sets":3,
                "weight":100,
                "weight_unit_id":1,
                "difficulty_id":3
            }
        ]

    }))
        
    