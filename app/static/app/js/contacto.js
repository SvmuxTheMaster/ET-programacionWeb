document.getElementById('formLogin').addEventListener('submit', function(event) {
    event.preventDefault();

    //se obtienen valore del form
    const correo = document.getElementById('correo').value.trim();
    const nombre = document.getElementById('nombre').value.trim();
    const mensaje = document.getElementById('mensaje').value.trim(); 

    const error = document.getElementById('error');

    //VALIDACION CORREO
    if (!correo || !validarCorreo( correo )){
        alert(error.textContent = 'Introduzca un correo valido')
        return;
    }

    //VALIDACION NOMBRE
    if (!nombre || nombre.length < 2){
        alert(error.textContent = 'Introduzca un nombre valido')
        return;
    }

    if (!mensaje || mensaje.length < 10){
        alert(error.textContent = 'Introduzca un mensaje valido')
        return;
    }

    alert('¡Mensaje enviado con éxito!');
    window.location.href = '/';
    
});

function validarCorreo( email ){
    const validar = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return validar.test( email );
}