Algoritmo Comisiones
	Escribir "Dígite el salario base del vendedor"
	Leer salario
	Escribir "Digite la ganancia por la primer venta"
	Leer venta1
	Escribir "Digite la ganancia por la segunda venta"
	Leer venta2
	Escribir "Digite la ganancia por la tercer venta"
	Leer venta3
	comision1<-venta1*0.1
	comision2<-venta2*0.1
	comision3<-venta3*0.1
	comisionTotal<-comision1+comision2+comision3
	Total<-salario+comisionTotal
	Escribir "El vendedor gana un salario base de: " salario " y unas comisiones de: " comisionTotal " para un total de" Total
FinAlgoritmo
