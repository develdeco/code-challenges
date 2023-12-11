<?php
//Extendemos la precision del float de php
ini_set('precision', 100);

//Definimos el numero de iteraciones para calcular Pi
//Usando BBP se demuestra que solo con 10 iteraciones
//se llega a un valor estandard con 48 decimales
define('NUM_ITERATIONS', 10);

//Devuelve true si es primo utilizando los polinomios de
//las formas 6k-1 y 6k+1 cuyos excluyentes nunca son primos
function isPrime($n) {
    //Si es 1 no es primo
    if($n == 1)
        return false;

	//Si es 2 o 3 es primo
    if($n == 2)
        return true;
    if($n == 3)
        return true;

    //Si es divisible por 2 o 3 no es primo
    if($n % 2 == 0)
        return false;
    if($n % 3 == 0)
        return false;

    //El resto de divisores a probar mayores a 3 no deben ser multiplos
    //de 2 ni 3 para evitar iteraciones redundantes.
    //Usando la forma (6k-1) o (6k+1) obtenemos números potencialmente
    //primos para evitar dividir por dichos multiplos la menor cantidad 
    //de veces posible.
    $i = 5; //Empezamos dividiendo a partir del 5
    $w = 2; //Artificio para oscilar entre 6k-1 y 6k+1

    //Iteramos máximo hasta sqrt(n) para no repetir
    //el proceso en modo inverso (i<=sqrt(n) o i^2<=n)
    while($i * $i <= $n) {
    	//Si es divisible no es primo
        if($n % $i == 0)
            return false;
        //6k-1 cuando w=4, 6k+1 cuando w=2
        $i += $w;
        $w = 6 - $w; //w oscila entre 2 y 4
    }

    //Si nunca pudo dividirse es primo
    return true;
}

//Calcula Pi y devuelve una cadena con sus decimales.
//Utilizamos la sumatoria de serie infinita Bailey–Borwein–Plouffe
//Esta formula converge rápido por lo que no es necesario utilizar
//demasiadas iteraciones.
function getPiDecimals($precision) {
	$p16 = 1;
	$pi = 0;
	//Aplicamos la sumatoria "infinita" cuya precision
	//dependera del número de iteraciones
    for($k=0; $k<=$precision; $k++) {
    	//Formula BBP
        $pi += 1.0/$p16 * (4.0/(8*$k + 1) - 2.0/(8*$k + 4) - 1.0/(8*$k + 5) - 1.0/(8*$k+6));
        $p16 *= 16;
    }
    //Solo necesitamos los decimales en forma de cadena
    return str_replace('3.','',strval($pi));
}

//Obtenemos la aproximación de pi usando n iteraciones
$piDec = getPiDecimals(NUM_ITERATIONS);
echo "Aproximación de ".strlen($piDec)." decimales: ".$piDec."\n";

//Inicializamos el contador de números primos encontrados
$primeCount = 0;

//Buscamos números primos de 10 dígitos en los decimales
for($i = 0; $i < strlen($piDec); $i++) {
	//Extraemos 10 digitos de la cadena
	$part = substr($piDec, $i, 10);
	//Si la cadena extraida es menor a 10 digitos paramos
	if(strlen($part) < 10)
		break;
	//Preguntamos si la cadena extraida es un número primo
	if(isPrime(intval($part))) {
		//Si lo es: incrementamos el contador
		$primeCount++;
		//Si el contador ya encontró un número primo
		//anteriormente paramos e imprimos el 2do encontrado
		if($primeCount > 1) {
			echo "Número Primo ".$primeCount.": ".$part."\n";
			break;
		}
	}
}