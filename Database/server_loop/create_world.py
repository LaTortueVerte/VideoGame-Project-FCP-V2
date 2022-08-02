import mariadb, math, json

# ----------------------------------------------------------
# This file transfer json data that contains all planets 
# to database in sql
# ----------------------------------------------------------

print("You're going to delete current data in the database")
verif = input("Do you really want to continue ? Y/N")

if verif == "Y":

    # Get data from json file ----------------------------------

    with open('.\Database\server_loop\data.json', 'r+') as file:
        json_data = json.load(file)

    # Send data to the database ---------------------------------------------

    def search_by_ID(id):
        for el in json_data["data"]:
            if el["id"] == id:
                return el
        return None

    conn = mariadb.connect(
        user = "root",
        password = "",
        host = "localhost",
        port = 3307,
        database = "dev-FCP-V2"
    )

    sql = "DELETE FROM planet"
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()

    except mariadb.Error as e:
        print(f"Error: {e}")

    for planet in json_data["data"]:    
        if planet["orbit_center_id"] != 0:
            orbit_center = search_by_ID(planet["orbit_center_id"])
            planet["x"] = math.cos(planet["angle"] * math.pi/180) * planet["orbit_radius"] + orbit_center["x"]
            planet["y"] = math.sin(planet["angle"] * math.pi/180) * planet["orbit_radius"] + orbit_center["y"]
        else:
            planet["x"] = math.cos(planet["angle"] * math.pi/180) * planet["orbit_radius"]
            planet["y"] = math.sin(planet["angle"] * math.pi/180) * planet["orbit_radius"]

        sql = "INSERT INTO planet (id, orbit_center_id, angle, angle_speed, orbit_radius, radius, mass, x, y, type) VALUES (" + str(planet["id"]) + "," + str(planet["orbit_center_id"]) + "," + str(planet["angle"]) + "," + str(planet["angle_speed"]) + "," + str(planet["orbit_radius"]) + "," + str(planet["radius"]) + "," + str(planet["mass"]) + "," + str(planet["x"]) + "," + str(planet["y"]) + "," + str(planet["type"]) + ");"

        try:
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()

        except mariadb.Error as e:
            print(f"Error: {e}")
