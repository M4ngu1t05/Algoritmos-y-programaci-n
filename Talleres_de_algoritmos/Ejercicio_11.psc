Algoritmo Nota_final
	Escribir "Ingrese las notas del estudiante"
	Escribir "Digite las Notas parciales"
	leer Notap1
	leer Notap2
	Leer Notap3
	Escribir "Digite la nota del examen final"
	Leer NotaEx
	Escribir "Digite la nota del trabajo final"
	Leer NotaTF
	NotaP<-(Notap1+Notap2+Notap3/3)*0.55
	NotaE<-NotaEx*0.30
	NotaTF_1<-NotaTF*0.15
	NotaF<-NotaP+NotaE+NotaTF_1
	Escribir "El estudiante final tiene una nota final de: " NotaF
FinAlgoritmo
