import mariadb, math

import mariadb, math, json

# --------------------------------------------------------------------
# This file update database that contains all planets and players data
# --------------------------------------------------------------------

conn = mariadb.connect(
    user = "root",
    password = "",
    host = "localhost",
    port = 3307,
    database = "dev-FCP-V2"
)

# Get data from database ------------------------------------------------

sql = "SELECT * FROM planet"
try:
    cur = conn.cursor(dictionary=True)
    cur.execute(sql)
    result_1 = cur.fetchall()

except mariadb.Error as e:
    print(f"Error: {e}")

# Process data in database ----------------------------------------------
result_2 = []
for planet in result_1:
    new_planet = {}

    new_planet["id"] = planet[0]
    new_planet["orbit_center_id"] = planet[1]
    new_planet["angle"] = planet[2]
    new_planet["angle_speed"] = planet[3]
    new_planet["orbit_radius"] = planet[4]
    new_planet["radius"] = planet[5]
    new_planet["mass"] = planet[6]
    new_planet["x"] = planet[7]
    new_planet["y"] = planet[8]
    new_planet["type"] = planet[9]

    result_2.append(new_planet)

def search_by_ID(id):
    for planet in result_2:
        if planet["id"] == id:
            return planet
    return None
    
for planet in result_2:

    planet["angle"] += planet["angle_speed"]
    if planet["orbit_center_id"] != 0:
        orbit_center = search_by_ID(planet["orbit_center_id"])
        
        planet["x"] = math.cos(planet["angle"] * math.pi/180) * planet["orbit_radius"] + orbit_center["x"]
        planet["y"] = math.sin(planet["angle"] * math.pi/180) * planet["orbit_radius"] + orbit_center["y"]
    else:
        planet["x"] = math.cos(planet["angle"] * math.pi/180) * planet["orbit_radius"]
        planet["y"] = math.sin(planet["angle"] * math.pi/180) * planet["orbit_radius"]

    '''
    for el in result_1:
        print(el)
    for el in result_2: 
        print(el)
    '''

    # Send data to the database ---------------------------------------------

    sql = "UPDATE planet SET angle = " + str(planet["angle"]) + ", x = " + str(planet["x"]) + ", y = " + str(planet["y"]) + " WHERE id = " + str(planet["id"]) + ";"
     
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()

    except mariadb.Error as e:
        print(f"Error: {e}")
