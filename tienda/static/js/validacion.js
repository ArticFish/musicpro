$(document).ready(function(){
    $("#form1").on('submit', function(e){
    let mensajesMostrar = "";
    let entrar = false;

var usuario =$("#usuario").val();
var contra =$("#contra").val();
var conficontra =$("#conficontra").val();
    if(usuario.trim().length<4 || usuario.trim().length >15){
        mensajesMostrar +="El nombre de usuario debe tener entre 4 y 15 caracteres <br>";
        entrar = true;
    }
    if(contra.length<8 || contra.length >15 ){
        mensajesMostrar +="La contraseña debe tener entre 8 y 15 caracteres <br>";
        entrar = true;
    }
    if(conficontra!=contra){
        mensajesMostrar +="Las contraseñas no son iguales <br>"
        entrar = true;
    }
    let letra=contra.charAt(0);
    let letraMayus=letra.toUpperCase();

    if(letra!=letraMayus){
        mensajesMostrar +="La primera letra de la contraseña debe ser mayuscula"
        entrar=true
    }
    if(entrar){
        $("#mensajes").html(mensajesMostrar);
        e.preventDefault();
    }
    else{
        mensajesMostrar +=""
        $("#mensajes").html(mensajesMostrar);
    }
});
    $("#form2").on('submit', function(e){
    let mensajesMostrar = "";
    let entrar = false;

    var iniciousuario =$("#iniciousuario").val();
    var iniciocontra =$("#iniciocontra").val();
    if(iniciousuario.length<4 || iniciousuario.length >15){
        mensajesMostrar +="El nombre de usuario debe tener entre 4 y 15 caracteres <br>";
        entrar = true;
    }
    if(iniciocontra.length<8 || iniciocontra.length >15 ){
        mensajesMostrar +="La contraseña debe tener entre 8 y 15 caracteres <br>";
        entrar = true;
    }
    if(entrar){
        $("#mensajes").html(mensajesMostrar);
        e.preventDefault();
    }
    else{
        mensajesMostrar +=""
        $("#mensajes").html(mensajesMostrar);
    }
    });
});
