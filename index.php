<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" contetn="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>🥔FatestCosmicPotato</title>
        <script src="./node_modules/pixi.js/dist/browser/pixi.min.js"></script>
        <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
        <link rel="stylesheet" href="https://unpkg.com/jquery.terminal/css/jquery.terminal.min.css"/>
        <style>
            * {
                padding : 0;
                margin: 0;
            }

            .terminal{
                position: absolute;
                bottom: 0px;
                left: 0px;
                z-index: 1;
                width: 100%;
                height: 100px;
                box-sizing: border-box;
            }

        </style>
    </head>
    <body onResize="window.location.href = window.location.href;">
        <script type="module" src="./app.js"></script>
        <iframe class = "terminal" src="terminal.html"></iframe>
    </body>
</html>
