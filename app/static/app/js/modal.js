// Obtener el modal
var modal = document.getElementById("productModal");

// Obtener el <span> que cierra el modal
var span = document.getElementsByClassName("close")[0];

// Cuando el usuario haga clic en <span> (x), cerrar el modal
span.onclick = function() {
    modal.style.display = "none";
}


// Función para abrir el modal y mostrar los detalles del producto
function openModal(productId) {
    var servicio = document.querySelector(`[data-id='${productId}']`);
    var title = servicio.querySelector('.card-title').innerText;
    var imageSrc = servicio.querySelector('img').src;
    var price = servicio.querySelector('.precio').innerText;
    
    document.getElementById('modalTitulo').innerText = title;
    document.getElementById('modalImg').src = imageSrc;
    document.getElementById('modalPrecio').innerText = price;

    modal.style.display = "block";
}

