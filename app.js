
//-----------------------------------------------------------------------------------------------------
// INIT game screen
//-----------------------------------------------------------------------------------------------------

const Application = PIXI.Application;
const Graphics = PIXI.Graphics;

const app = new Application({
    transparent: false,
    antialias: true,
    resizeTo: window
});

PIXI.settings.SCALE_MODE = PIXI.SCALE_MODES.NEAREST;

app.renderer.backgroundColor = 0x001E4D; //2B2B54 - 23395D
app.renderer.resize(window.innerWidth, window.innerHeight);
app.renderer.view.style.position = 'absolute';
document.body.appendChild(app.view);

window.onresize = function(){ 
window.location.href = "./index.php"; // redirect to itself = reload page
}

//-----------------------------------------------------------------------------------------------------
// OBJECTS
//-----------------------------------------------------------------------------------------------------

// Global ---------------------------------------------------------------------------------------------

const pixel_size = Math.floor(window.innerWidth/400);

// Planet ---------------------------------------------------------------------------------------------

class Pixelated_Circle {
    constructor(Graphics, pixel_size, parent, x, y, r, color){
        this.x = x;
        this.y = y;
        this.r = Math.floor(r + r%2); // convert to even number
        this.parent = parent;

        // DRAW CIRCLE -----------------------------------------

        // Init

        this.circle_container = new PIXI.Container();

        function distance(x1, y1, x2, y2){
            return Math.sqrt(Math.pow((x2-x1), 2) + Math.pow((y2-y1), 2)); 
        }

        var list = new Array();

        var drawY = r;
        var drawX = 0;
        while (drawY != 0){
            while (distance(0, 0, drawX, drawY-1) < r){
                drawX++;
            }
            if ((distance(0, 0, drawX, drawY-1) >= r) && (drawY > 0)){
                list.push([drawX, drawY]);
            }
            while ((distance(0, 0, drawX, drawY-1) >= r) && (drawY > 0)){
                drawY--;
            }
        }

        for (var i = 0 ; i < list.length ; i++){
            const rect = new Graphics();
            rect.beginFill(color);
            rect.drawRect((r - list[i][0]) * pixel_size, (r - list[i][1]) * pixel_size, list[i][0] * 2 * pixel_size, list[i][1] * 2 * pixel_size);
            rect.endFill();

            /*
            const rect = new Graphics();
            rect.beginFill(color);
            rect.drawRect(x-list[i][0], y-list[i][1], list[i][0] * 2 * pixel_size, list[i][1] * 2 * pixel_size);
            rect.endFill();*/

            this.circle_container.addChild(rect);
        }

        this.circle_container.pivot.set(this.circle_container.width / 2, this.circle_container.height / 2);
        this.circle_container.position.set(x, y);
        //this.circle_container.scale.set(pixel_size, pixel_size);
        this.parent.addChild(this.circle_container);
    }
}

// Spaceship

class Spaceship {
    constructor(pixel_size, parent, x, y ){
        this.sprite = PIXI.Sprite.from('./images/spaceship/spaceship.png');
        this.sprite.anchor.set(0.5, 0.5);
        this.sprite.position.set(x, y);
        this.sprite.scale.set(pixel_size, pixel_size);

        this.parent = parent;
        this.parent.addChild(this.sprite);
    }
}

//-----------------------------------------------------------------------------------------------------
// LOOP
//-----------------------------------------------------------------------------------------------------


var sp = new Spaceship(pixel_size, app.stage, window.innerWidth/2, window.innerHeight/2);