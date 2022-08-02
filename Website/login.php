<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" contetn="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🥔FatestCosmicPotato</title>
</head>
<body>
    <?php
        require('./conn/CRUD.php');
        session_start();

        if (isset($_POST['username']))
        {
            $username = stripslashes($_REQUEST['username']);

            $password = stripslashes($_REQUEST['password']);

            $list = find("users",array("username"=>$username, "password"=>hash('sha256', $password)));
            if ($list != null && sizeof($list) == 1)
            {
                $row = $list[0];

                $_SESSION['username'] = $username;
                $_SESSION['id'] = $row["id"];

                // Go to menu

                header("Location: index.php");
            }
            else
            {
                $message = "username or / and password incorrect.";
            }
        }
    ?>

    <form action="" method="post" name="login">

        <h1>Sign in</h1>

        <input type="text" name="username">
        <input type="password" name="password" minlength="8" autocomplete=off>

        <input type="submit" value="🔌" name="submit">

        <a href="register.php">sign out</a>

        <?php if (! empty($message)) { ?>
            <p class="errorMessage"><?php echo $message; ?></p>
        <?php } ?>

    </form>

<body>
</html>