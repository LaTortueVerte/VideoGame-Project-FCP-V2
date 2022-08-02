import math, json, time
from tkinter import *

zoom = 20

with open('.\Database\server_loop\data.json', 'r+') as file:
    json_data = json.load(file)

fenetre = Tk()
canvas = Canvas(fenetre, width=1000, height=1000, background='white')
canvas.pack(fill="both", expand=True)

def create_circle(x, y, r, color):
    if color != None:
        return canvas.create_oval(x-r, y-r, x+r, y+r, fill=color)
    else:
        return canvas.create_oval(x-r, y-r, x+r, y+r)

def search_by_ID(id):
    for el in json_data["data"]:
        if el["id"] == id:
            return el
    return None



for planet in json_data["data"]:    
    if planet["orbit_center_id"] != 0:
        orbit_center = search_by_ID(planet["orbit_center_id"])
        planet["orbit"] = create_circle(orbit_center["x"]/zoom + 500, orbit_center["y"]/zoom + 500, planet["orbit_radius"]/zoom, None)
        planet["x"] = math.cos(planet["angle"] * math.pi/180) * planet["orbit_radius"] + orbit_center["x"]
        planet["y"] = math.sin(planet["angle"] * math.pi/180) * planet["orbit_radius"] + orbit_center["y"]
    else:
        planet["x"] = math.cos(planet["angle"] * math.pi/180) * planet["orbit_radius"]
        planet["y"] = math.sin(planet["angle"] * math.pi/180) * planet["orbit_radius"]

    #print(planet)
    planet["ref"] = create_circle(planet["x"]/zoom + 500, planet["y"]/zoom + 500, planet["radius"]/zoom, 'black')

while True:
    for planet in json_data["data"]:    
        planet["angle"] += planet["angle_speed"] * 50
        if planet["orbit_center_id"] != 0:
            orbit_center = search_by_ID(planet["orbit_center_id"])
            
            canvas.moveto(planet["orbit"], orbit_center["x"]/zoom + 500 - planet["orbit_radius"]/zoom, orbit_center["y"]/zoom + 500 - planet["orbit_radius"]/zoom)
            planet["x"] = math.cos(planet["angle"] * math.pi/180) * planet["orbit_radius"] + orbit_center["x"]
            planet["y"] = math.sin(planet["angle"] * math.pi/180) * planet["orbit_radius"] + orbit_center["y"]
        else:
            planet["x"] = math.cos(planet["angle"] * math.pi/180) * planet["orbit_radius"]
            planet["y"] = math.sin(planet["angle"] * math.pi/180) * planet["orbit_radius"]

        canvas.moveto(planet["ref"], planet["x"]/zoom + 500 - planet["radius"]/zoom, planet["y"]/zoom + 500 - planet["radius"]/zoom)
        #print(planet["id"], " angle = ", format(planet["angle"], ".3f"), " x = ", format(planet["x"], ".3f"), " y = ", format(planet["y"], ".3f"))

    fenetre.update()
    time.sleep(0.001)