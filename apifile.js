function comenzar(){
	zonadatos=document.getElementById("zonadatos");
	var boton=document.getElementById("boton");
	boton.addEventListener("click", escribir_archivo, false);

	navigator.webkitPersistentStorage.requestQuota(5*1024*1024, acceso);

}

function acceso(){
	window.webkitRequestFileSystem(PERSISTENT,10*1024*1024,creasis,errores);
}

function creasis(sistema){
	espacio=sistema.root
}

function escribir_archivo(){
    var nombre=document.getElementById("archivo_origen").value;

    espacio.getFile(nombre,{create:true, exclusive:false}, function(entrada){
         entrada.createWriter(escribir_contenido, errores);
    }, errores);

}

function escribir_contenido(fileWriter){
    var texto=document.getElementById("texto").value;
    fileWriter.onwriteend=exito();

    var blob=new Blob([texto],{type:"text/html"});
    fileWriter.write(blob); 
}

function exito(){
    document.getElementById("archivo_origen".value="");
    document.getElementById("texto".value="");
    zonadatos.innerHTML="archivo creado con exito";
}

function errores(e){
	alert("hay un error" + e.code);
}

window.addEventListener("load",comenzar,false);