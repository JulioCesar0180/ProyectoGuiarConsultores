//home.js
var explosivos = 0;
var electricidad = 0;
var sustancias = 0;
var altura =0;

function displayExplosivos(){
    if(explosivos < 1){
        var num = document.getElementById('exp').innerHTML;
        explosivos++;
        $('<div id="explosivosNext"><b>P'+num+'-1.</b> Indique todas las actividades que realiza la empresa para disminuir los riesgos con respecto a la manipulación de explosivos<div><br></div>'+
        '<div class="input-radio"><input type="checkbox" id="inscripcion" name="explosivos[]" value="inscripcion">'+
        '<label for="inscripcion" class="unselectable">Cuenta con inscripción vigente en el Registro Nacional de Explosivos y Productos Químicos (DGMN)</label></div>'+
        '<div class="input-radio"><input type="checkbox" id="certificado" name="explosivos[]" value="certificado">'+
        '<label for="certificado" class="unselectable">Cuenta con certificado del Cuerpo de Bomberos, de la instalación donde se almacenará el producto</label></div>'+
        '<div class="input-radio"><input type="checkbox" id="personal" name="explosivos[]" value="personal">'+
        '<label for="personal" class="unselectable">Cuenta con personal con Licencia de Programador Calculista y/o Manipulador de Explosivos</label></div>'+
        '<div class="input-radio"><input type="checkbox" id="polvorin" name="explosivos[]" value="polvorin">'+
        '<label for="polvorin" class="unselectable">Cuenta con Polvorín, plantas de explosivos y/o cambios de fabrica autorizados</label></div>'+
        '<div class="input-radio"><input type="checkbox" id="procedimientos" name="explosivos[]" value="procedimientos">'+
        '<label for="procedimientos" class="unselectable">Cuenta con "Procedimientos seguros de trabajo", según el Artículo N 16, Decreto Supremo 72, Ministerio de Minería</label></div>'+
        '<div class="input-radio"><input type="checkbox" id="dispositivos" name="explosivos[]" value="dispositivos">'+
        '<label for="dispositivos" class="unselectable">Cuenta con "dispositivos de seguridad" otorgados por el mandante, según Artículo N 18, Decreto Supremo 72, Ministerio de Minería</label></div>'+
        '<div><br></div><div><hr></div></div>').appendTo("#explosivos");
    }
}

function occultExplosivos(){
    if(explosivos == 1){
        explosivos--;
        var parent = document.getElementById("explosivos");
        var child = document.getElementById("explosivosNext");
        parent.removeChild(child);
    }
}

function displayElectricidad(){
    if(electricidad < 1){
        var num = document.getElementById('ele').innerHTML;
        electricidad++;
        $('<div id="electricidadNext"><b>P'+num+'-1.</b> Indique todas las actividades que realiza la empresa para disminuir los riesgos con respecto a la MANIPULACIÓN DE ELECTRICIDAD<div><br></div>'+
        '<div class="input-radio"><input type="checkbox" id="apertura" name="electricidad[]" value="apertura">'+
        '<label for="apertura" class="unselectable">Cumple con la apertura con corte visible de las fuentes de tensión</label></div>'+
        '<div class="input-radio"><input type="checkbox" id="encaramiento" name="electricidad[]" value="encaramiento">'+
        '<label for="encaramiento" class="unselectable">Realiza encaramiento o bloqueo de los aparatos de corte</label></div>'+
        '<div class="input-radio"><input type="checkbox" id="ausencia" name="electricidad[]" value="ausencia">'+
        '<label for="ausencia" class="unselectable">Reconocimiento de ausencia de la ausencia de tensión</label></div>'+
        '<div class="input-radio"><input type="checkbox" id="tierra" name="electricidad[]" value="tierra">'+
        '<label for="tierra" class="unselectable">Puesta a tierra y en cortocircuito de todos los conductores</label></div>'+
        '<div class="input-radio"><input type="checkbox" id="delimitacion" name="electricidad[]" value="delimitacion">'+
        '<label for="delimitacion" class="unselectable">Delimitación de la zona de trabajo</label></div>'+
        '<div><br></div><div><hr></div></div>').appendTo("#electricidad");
    }
}

function occultElectricidad(){
    if(electricidad == 1){
        electricidad--;
        var parent = document.getElementById("electricidad");
        var child = document.getElementById("electricidadNext");
        parent.removeChild(child);
    }
}

function displaySustancias(){
    if(sustancias < 1){
        var num = document.getElementById('sus').innerHTML;
        sustancias++;
        $('<div id="sustanciasNext"><b>P'+num+'-1.</b> Indique todas las actividades que realiza la empresa para disminuir los riesgos con respecto al TRANSPORTE DE SUSTANCIAS PELIGROSAS<div><br></div>'+
        '<div class="input-radio"><input type="checkbox" id="distintivos" name="sustancias_peligrosas[]" value="distintivos">'+
        '<label for="distintivos" class="unselectable">Cuenta con distintivos y rótulos a que se refiere la Norma Chilena Noh. 2190-Of93</label></div>'+
        '<div class="input-radio"><input type="checkbox" id="tacografo" name="sustancias_peligrosas[]" value="tacografo">'+
        '<label for="tacografo" class="unselectable">Sus vehículos cuentan con tacógrafo, control electrónico de velocidad y distancia recorrida</label></div>'+
        '<div class="input-radio"><input type="checkbox" id="antiguedad" name="sustancias_peligrosas[]" value="antiguedad">'+
        '<label for="antiguedad" class="unselectable">Tiene vehículos con una antigüedad máxima de 15 años</label></div>'+
        '<div class="input-radio"><input type="checkbox" id="transporte" name="sustancias_peligrosas[]" value="transporte">'+
        '<label for="transporte" class="unselectable">Realiza transporte de sustancias peligrosas a granel, según normativa 2136.Of1989</label></div>'+
        '<div class="input-radio"><input type="checkbox" id="embalaje" name="sustancias_peligrosas[]" value="embalaje">'+
        '<label for="embalaje" class="unselectable">Cuenta con embalaje autorizado según Decreto 298 y sus modificaciones</label></div>'+
        '<div class="input-radio"><input type="checkbox" id="carga" name="sustancias_peligrosas[]" value="carga">'+
        '<label for="carga" class="unselectable">Cuenta con procedimientos según Normativa NCh 382. NCh 2120/1 a 2120/9 de carga y descarga de sustancias peligrosas</label></div>'+
        '<div><br></div><div><hr></div></div>'+
        '<div id="sustanciasNext"><b>P'+num+'-2.</b> Indique todos los tipos de plataforma que tiene para el TRANSPORTE DE SUSTANCIAS PELIGROSAS<div><br></div>'+
        '<div class="input-radio"><input type="checkbox" id="tipoA" name="tipoA" value="tipoA">'+
        '<label for="tipoA" class="unselectable">A</label></div>'+
        '<div class="input-radio"><input type="checkbox" id="tipoB" name="tipoB" value="tipoB">'+
        '<label for="tipoB" class="unselectable">B</label></div>'+
        '<div class="input-radio"><input type="checkbox" id="tipoC" name="tipoC" value="tipoC">'+
        '<label for="tipoC" class="unselectable">C</label></div>'+
        '<div><br></div><div><hr></div></div>').appendTo("#sustancias");
    }
}

function occultSustancias(){
    if(sustancias == 1){
        sustancias--;
        var parent = document.getElementById("sustancias");
        var child = document.getElementById("sustanciasNext");
        while(child){
            parent.removeChild(child);
            var child = document.getElementById("sustanciasNext");
        }
    }
}

function displayAltura(){
    if(altura < 1){
        var num = document.getElementById('alt').innerHTML;
        altura++;
        $('<div id="alturaNext"><b>P'+num+'-1.</b> Indique todas las actividades que realiza la empresa para disminuir los riesgos con respecto a los TRABAJOS EN ALTURA<div><br></div>'+
        '<div class="input-radio"><input type="checkbox" id="norma" name="altura[]" value="norma">'+
        '<label for="norma" class="unselectable">Cuenta con procedimientos según norma NCh. 998.Of1999. / NCh.1258-1</label></div>'+
        '<div class="input-radio"><input type="checkbox" id="supervisor" name="altura[]" value="supervisor">'+
        '<label for="supervisor" class="unselectable">Cuenta con supervisor que apruebe y revise trabajos en altura (secuencia lógica)</label></div>'+
        '<div class="input-radio"><input type="checkbox" id="proteccion" name="altura[]" value="proteccion">'+
        '<label for="proteccion" class="unselectable">Cuenta con procedimientos de uso de elementos de protección personal</label></div>'+
        '<div class="input-radio"><input type="checkbox" id="equipamiento" name="altura[]" value="equipamiento">'+
        '<label for="equipamiento" class="unselectable">Cuenta con equipamiento y accesorios certificados propios o de terceros</label></div>'+
        '<div><br></div><div><hr></div></div>').appendTo("#altura");
    }
}

function occultAltura(){
    if(altura == 1){
        altura--;
        var parent = document.getElementById("altura");
        var child = document.getElementById("alturaNext");
        parent.removeChild(child);
    }
}