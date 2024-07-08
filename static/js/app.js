//Codigo para que al clickear el menu hamburguesa se vea el menu (barraOcultar)

const hamburguesa= document.getElementById('hamburguesa');
const cruz = document.getElementById('cruz');
const navBar = document.getElementById('navBar');
const barraOcultar = document.getElementById('barraOcultar');
const contenedorTitulo= document.getElementById('contenedorTitulo');

const clickHamburguesa=(e)=>{
    hamburguesa.style.display="none";
    cruz.style.display = "flex";
    navBar.style.top = "0vh";
    barraOcultar.style.display = "flex";
    barraOcultar.style.padding = "0px 20px";
    contenedorTitulo.style.left ="42%";
    contenedorTitulo.style.top="0";
    contenedorTitulo.style.scale="0.6";
}

//Y al clickear la cruz se cierre el menu desplegable

const clickCruz=(e)=>{
    hamburguesa.style.display="";
    cruz.style.display = "none";
    navBar.style.top = "1vh";
    barraOcultar.style.display = "";
    contenedorTitulo.style.left = "";
    contenedorTitulo.style.top= "";
    contenedorTitulo.style.scale= "";
}


hamburguesa.addEventListener('click', clickHamburguesa);
cruz.addEventListener('click', clickCruz);


// Formulario CRUD
var modal = document.getElementById("myModal");
var paquetesForm = document.getElementById("paquetesForm");
var span = document.getElementsByClassName("close")[0];

// Cierra la ventana emergente con:
// click en la x
span.onclick = function () {
    modal.style.display = "none";
}
// clic fuera de la ventana 
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

// Abre la ventana emergente y cargar datos en el formulario
function openModal(action, id, nombre, destino, descripcion, imagen, precio, disponible) {
    paquetesForm.action = action;
    document.getElementById('id').value = id;
    document.getElementById('nombre').value = nombre;
    document.getElementById('destino').value = destino;
    document.getElementById('descripcion').value = descripcion;
    document.getElementById('imagen').value = imagen;
    document.getElementById('precio').value = precio;
    document.getElementById('disponible').value = disponible;
    modal.style.display = "block";
}
