/*
Ejercicio:
Crear un programa donde el usuario debe ingresar un password en tu aplicación.
Si el password tiene menos de 6 caracteres, se debe mostrar el aviso:
'El password es demasiado corto'
*/

let password = prompt("Ingrese su contraseña")

if (password.length < 6) {
    alert("El password es demasiado corto");
} else {
    alert("El password se ingresó exitosamente");
}