function toggleGaleria() {
    // Obtiene las fotos de la mascota específica
    var fotosMascota = obtenerFotosMascota(mascotaId);

    // Muestra u oculta la galería
    var galeria = document.getElementById('galeria');
    galeria.style.display = (galeria.style.display === 'none') ? 'flex' : 'none';

    // Muestra la primera foto de la mascota en la galería
    document.getElementById('imagen-galeria').src = fotosMascota[0].url_foto;
}

function cerrarGaleria() {
    document.getElementById('galeria').style.display = 'none';
}

// Define una función para obtener las fotos de la mascota
function obtenerFotosMascota(mascotaId) {
    // Realiza una solicitud AJAX para obtener las fotos de la mascota desde el servidor
    // En este ejemplo, asumimos que estás usando jQuery para simplificar la solicitud AJAX
    $.ajax({
        url: '/ruta/para/obtener/fotos/mascota/' + mascotaId,
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            // data contendrá las fotos de la mascota
            mostrarFotosEnGaleria(data);
        },
        error: function(error) {
            console.error('Error al obtener las fotos de la mascota:', error);
        }
    });
}

// Define una función para mostrar las fotos en la galería
function mostrarFotosEnGaleria(fotosMascota) {
    // Resto de tu código para mostrar las fotos en la galería
    // Recorre el array de fotos y realiza las acciones necesarias
    var carrusel = document.getElementById('carrusel');
    carrusel.innerHTML = ''; // Limpiar el carrusel antes de agregar nuevas fotos

    // Agregar las fotos al carrusel
    fotosMascota.forEach(function(foto) {
        var imagen = document.createElement('img');
        imagen.src = foto.url_foto;
        carrusel.appendChild(imagen);
    });
}