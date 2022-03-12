from sql_connection import create_sql_connection

def get_all_weight_units(connection):
    cursor=connection.cursor()

    query="SELECT * FROM weight_unit"

    cursor.execute(query)

    response=[]

    for (weight_unit_id,weight_unit) in cursor:
        response.append({
            "weight_unit_id":weight_unit_id,
            "weight_unit":weight_unit
        })

    return response




if __name__=="__main__":
    connection=create_sql_connection()
    print(get_all_weight_units(connection))

