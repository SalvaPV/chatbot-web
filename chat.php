<?php
if(isset($_POST['mensaje'])){
    $mensaje = $_POST['mensaje'];
    //detecta si es windows o mac
    $so = substr(PHP_OS, 0, 3);
    if($so == 'WIN'){
        $respuesta = shell_exec("python chatbot.py \"$mensaje\"");
    } else {
        $respuesta = shell_exec("python3 chatbot.py \"$mensaje\"");
    }
    echo $respuesta;
}
?>
