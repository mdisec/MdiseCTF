<?php
/**
 * Created by PhpStorm.
 * User: trincem
 * Date: 10/22/15
 * Time: 11:56 AM
 */

require("flag.php");

class Authentication{
    const KEY = "0e86982004367237686113517103584116354523";
    var $cred = "";
    function __construct($cred){
        echo self::KEY;
        $this->cred = md5($cred);
    }

    public function check(){
        if($this->cred == self::KEY)
            return TRUE;
        return False;
    }
}
if(isset($_GET['auth'])) {
    $authenticator = new Authentication($_GET['auth']);
    $result = $authenticator->check();
    if($result){header("Flag : ".get_flag());}
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
    <script src="https://code.jquery.com/jquery-2.1.4.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
    <meta charset="UTF-8">
    <title>Picus Security Authentication</title>
    <style>
        .form-signin{max-width:330px;padding:15px;margin:0 auto}.form-signin .form-signin-heading,.form-signin .checkbox{margin-bottom:10px}.form-signin .checkbox{font-weight:400}.form-signin .form-control{position:relative;font-size:16px;height:auto;padding:10px;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box}.form-signin .form-control:focus{z-index:2}.form-signin input[type="text"]{margin-bottom:-1px;border-bottom-left-radius:0;border-bottom-right-radius:0}.form-signin input[type="password"]{margin-bottom:10px;border-top-left-radius:0;border-top-right-radius:0}.account-wall{margin-top:20px;padding:40px 0 20px;background-color:#f7f7f7;-moz-box-shadow:0 2px 2px rgba(0,0,0,0.3);-webkit-box-shadow:0 2px 2px rgba(0,0,0,0.3);box-shadow:0 2px 2px rgba(0,0,0,0.3)}.login-title{color:#555;font-size:18px;font-weight:400;display:block}.profile-img{width:96px;height:96px;margin:0 auto 10px;display:block;-moz-border-radius:50%;-webkit-border-radius:50%;border-radius:50%}.need-help{margin-top:10px}.new-account{display:block;margin-top:10px}
    </style>
</head>
<body>
<div class="container">
    <div class="row">
        <div class="col-sm-6 col-md-4 col-md-offset-4">
            <h1 class="text-center login-title">Sign in to continue to Picus Security Panel</h1>
            <div class="account-wall">
                <a href="http://picussecurity.com" target="_blank" "><img class="profile-img" src="https://avatars0.githubusercontent.com/u/8177886?v=3&s=200"
                     alt=""></a>
                <form class="form-signin" method="GET">
                    <input type="password" name="auth" class="form-control" placeholder="Password">
                    <button class="btn btn-lg btn-primary btn-block" type="submit" id="submit">
                        Sign in</button>
                    <?php
                    if(isset($result) && $result === FALSE){
                    ?>
                    <label class="text-center text-warning" id="message">
                        Auth code is wrong. Please use correct code!
                    </label>
                    <?php } else if(isset($result) && $result === TRUE){?>
                    <label class="text-center text-success" id="message">
                        Gratz..! I've already shared my flag with you;)
                    </label>
                    <?php } ?>
                </form>
            </div>
        </div>
    </div>
</div>
</body>
</html>