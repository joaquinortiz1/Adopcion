document.addEventListener("DOMContentLoaded", function() {
    var enlacesMostrarOpciones = document.getElementsByClassName("mostrar-opciones");

    function mostrarOpciones(idOpciones) {
        var opciones = document.getElementById(idOpciones);
        if (opciones) {
            opciones.style.display = 'block';
        }
    }

    function ocultarOpciones(idOpciones) {
        var opciones = document.getElementById(idOpciones);
        if (opciones) {
            opciones.style.display = 'none';
        }
    }

    for (var i = 0; i < enlacesMostrarOpciones.length; i++) {
        enlacesMostrarOpciones[i].addEventListener("mouseover", function() {
            var idOpciones = this.getAttribute("data-opciones");
            mostrarOpciones(idOpciones);
        });

        enlacesMostrarOpciones[i].addEventListener("mouseout", function() {
            var idOpciones = this.getAttribute("data-opciones");
            ocultarOpciones(idOpciones);
        });
    }
});

var mostrarOpciones = function(idOpciones) {
    // Código de la función
};

var ocultarOpciones = function(idOpciones) {
    // Código de la función
};
