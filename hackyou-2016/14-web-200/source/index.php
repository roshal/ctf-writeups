<?php
ob_start();
session_start();

mysql_connect("localhost", "root", "toor");
mysql_select_db("web200");
?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Web 200</title>
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <style type="text/css">
      body { font-size: 20px; }
      input { font-size: 20px!important; }
      textarea { font-size: 20px!important; }
    </style>

    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
    <div class="container">
      <div class="jumbotron" style="margin-top: 70px; padding: 20px 50px 40px 50px;">
        <h1>hack <span style="color: #800000">you</span> Web 200</h1>
      </div>
<?php
$uid = false;
if (isset($_SESSION['uid'])) {
  $res = mysql_query("SELECT * FROM users WHERE uid = " . $_SESSION['uid']);
  if (mysql_num_rows($res) == 1) {
    $uid = $_SESSION['uid'];
    $row = mysql_fetch_assoc($res);
    $login = $row['login'];
  } else {
    unset($_SESSION['uid']);
  }
}

if ($uid === false) {
?>
      <div class="col-lg-12">
        <p>Hello! Please sign in to use our awesome service.<br/><br/></p>
      </div>
<?php
  if (isset($_POST['login'])) {
    $login = $_POST['login'];
    $password = $_POST['password'];
    $res = mysql_query("SELECT * FROM users WHERE login = '$login' AND password = '$password'");
    if (mysql_num_rows($res) == 0) {
?>
      <div class="bg-danger col-lg-12" style="margin-bottom: 30px">
        Incorrect username or password! Please check and try once again.
      </div>
<?php
    } else {
      $row = mysql_fetch_assoc($res);
      $_SESSION['uid'] = $row['uid'];
      ob_end_clean();
      header("Location: /", true, 302);
      exit;
    }
  }
?>
      <div class="col-lg-3"></div>
      <div class="col-lg-6">
        <form method="POST">
          <div class="form-group">
            <label for="login">Username</label>
            <input type="text" class="form-control" id="login" name="login" <?php if (isset($_POST['login'])) echo "value=\"" . htmlspecialchars($_POST['login']) . "\" "; ?>/>
          </div>
          <div class="form-group">
            <label for="password">Password</label>
            <input type="password" class="form-control" id="password" name="password" />
          </div>
          <input type="submit" class="btn btn-default" value="Login »" />
        </form>
      </div>
<?php
} else {
  if (isset($_GET['logout'])) {
    unset($_SESSION['uid']);
    ob_end_clean();
    header("Location: /", true, 302);
    exit;
  }
?>
      <div class="col-lg-12">
        <p>Welcome, <?php echo htmlspecialchars($login); ?>! <a href="?logout=1">Log out »</a><br/><br/></p>
      </div>
      <div class="col-lg-3"></div>
      <div class="col-lg-6">
        <form method="POST">
          <div class="form-group">
            <label for="text">Enter text to un-base64:</label>
            <textarea class="form-control" id="text" name="text" cols=40 rows=5><?php if (isset($_POST['text'])) echo htmlspecialchars(base64_decode($_POST['text']), ENT_QUOTES, "cp1252"); ?></textarea>
          </div>
          <input type="submit" class="btn btn-default" value="base64_decode »" />
        </form>
      </div>
<?php
}
?>
    </div>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
  </body>
</html>
