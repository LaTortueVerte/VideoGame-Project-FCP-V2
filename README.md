INSTALLATION STEP :

1 - install pixi js :
    Run the following command in the folder
    "npm install pixi.js"

2 - install database 

    use dev-FCP-V2;

    CREATE TABLE Spaceship(
        id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
        rotation INT,
        motor_power INT,
        health INT,
        fuel INT,
        x INT,
        y INT,
        speed INT
    );

    CREATE TABLE Planet(
        id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
        orbit_center_id INT,
        angle_speed INT,
        radius INT,
        mass INT,
        x INT,
        y INT
    );

    CREATE TABLE Player(
        id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
        username VARCHAR(100),
        password VARCHAR(100),
        x INT,
        y INT,
        landing_planet_id INT
    );

3 - install mariadb

    pip install mariadb

TECHNO USED : 

    terminal : https://itnext.io/how-to-create-interactive-terminal-like-website-888bb0972288