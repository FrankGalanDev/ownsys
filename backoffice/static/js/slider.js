//declarando la clase 
class Slider {
	constructor(flec_izq, flec_der,fila, pelicula, indicatorActivo, numPaginas, indicator){
		this.flec_izq = flec_izq;
		this.flec_der = flec_der;
		this.fila = fila;
		this.pelicula = pelicula;
		this.indicatorActivo = indicatorActivo;
		this.numPaginas = numPaginas;
		this.indicator = indicator;


    }

	
}
//definiendo las variables que conformaran el slider

const fila = document.querySelector('.carrousel_box');
const pelicula = document.querySelectorAll('.pelicula');
const flec_izq = document.getElementById('arrow_izq');
const flec_der = document.getElementById('arrow_der');
const indicatorActivo =document.querySelector('.indicator_point .activo');
const numPaginas = '';//queremos 5 peliculas por pagina
const indicator = document.createElement('button');


// creamos un nuevo objeto slider
slider = new Slider(flec_izq, flec_der, fila, pelicula, indicatorActivo, numPaginas, indicator)


/*event listener para flecha izq, calculamos cuanto desplaza hacia un lado la flecha 
 y lo añadimos a la posicion*/
slider.flec_izq.addEventListener('click', () => {
		slider.fila.scrollLeft += slider.fila.offsetWidth;

		if(slider.indicatorActivo.nextSibling){
		slider.indicatorActivo.nextSibling.classList.add('activo');
		slider.indicatorActivo.classList.remove('activo');
	    }

	});

//event listener para flecha derecha, calculamos cuanto desplaza hacia un lado la flecha 
// y lo restamos a posicion      
slider.flec_der.addEventListener('click', () => {
		slider.fila.scrollLeft -= slider.fila.offsetWidth;

		if(slider.indicatorActivo.previousSibling){
		slider.indicatorActivo.previousSibling.classList.add('activo');
		slider.indicatorActivo.classList.remove('activo');
	    }

	});
	


//calculando paginacion
slider.numPaginas = Math.ceil(pelicula.length / 5);//queremos 5 peliculas por pagina
for(let i = 0; i < slider.numPaginas; i++){
	slider.indicator = document.createElement('button');
	if(i === 0){
		slider.indicator.classList.add('activo');
	}

	document.querySelector('.indicator_point').appendChild(slider.indicator)
	slider.indicator.addEventListener('click', (e) => {
		slider.fila.scrollLeft = i * slider.fila.offsetWidth;

	document.querySelector('.indicator_point .activo').classList.remove('activo');
		e.target.classList.add('activo')
	});

	//trabajar con el hover
	slider.pelicula.forEach((peli) => {
		peli.addEventListener('mouseenter', (e) => {
			const elemento = e.currentTarget;
			setTimeout(() =>{
				slider.pelicula.forEach(peli =>peli.classList.remove('hover'));
				elemento.classList.add('hover');
			}, 300);
		});
	});
}

slider.fila.addEventListener('mouseleave',()=> {
	slider.pelicula.forEach(peli =>slider.peli.classList.remove('hover'));
				elemento.classList.add('hover');

});