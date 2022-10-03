Algoritmo Velocidades
	Escribir "Ingrese distancia"
	leer D
	Escribir "Ingrese velocidad del primer vehiculo"
	Leer v1
	Escribir "Ingrese velocidad del segundo vehiculo"
	leer v2
	th<-D/v2
	ts<-th*3600
	vm<-trunc(ts/60)
	vs<-ts mod 60
	Escribir "Le tomará " vm " Minutos y " vs " segundos en alcanzar al otro vehículo"
FinAlgoritmo
