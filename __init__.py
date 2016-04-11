__author__ = "Alejandro"
__date__ = "$10-abr-2016 19:43:25$"
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Operaciones.py
empleados=[]
posicion=0

def agregar_empleado(empleado_nuevo):
	empleados.append(empleado_nuevo)
	informacion=("SE AGREGO EXITOSAMENTE\n\n")
	return informacion
	
def mostrar_empleados(self):
	informacion="Lista de empleados:  \n"
	for empleado in empleados:
		informacion += str(empleado.getInformacion())+"\n"
	return informacion
	
def empleado_especifico():
	informacion="Empleado: \n"
	informacion+=empleados[posicion].getInformacion()
	return informacion
	
def verificar_empleado(codigo):
	resultado=False #no existe empleado con ese codigo
	for i in range(len(empleados)):
		if (empleados[i].getCodigo()==codigo):
			resultado=True
			global posicion
			posicion=i
	return resultado
	
def mostrar_salario():
	salario_ordinario=empleados[posicion].getHoras_ordinarias()* empleados[posicion].getMonto_hora()
	salario_extra=empleados[posicion].getHoras_extras()*(empleados[posicion].getMonto_hora()*1.5)
	salario_bruto=salario_extra+salario_ordinario
	deducciones= salario_bruto*0.0917
	salario_neto=salario_bruto- deducciones
	
	return str(salario_neto)
	
def mostrar_planilla():
	for i in range (0,len(empleados)):
		salario_ordinario=empleados[i].getHoras_ordinarias()* empleados[i].getMonto_hora()
		salario_extra=empleados[i].getHoras_extras()*(empleados[i].getMonto_hora()*1.5)
		salario_bruto=salario_extra+salario_ordinario
		deducciones= salario_bruto*0.0917
		salario_neto=salario_bruto- deducciones
		
		info="Codigo: " +str(empleados[i].getCodigo())+"\nNombre: "+empleados[i].getNombre() + "\nSalario bruto: "+str(salario_bruto)+"\nSalario neto: "+str(salario_neto)+"\nDeducciones: "+str(deducciones)
	return info
	
def cambiar_nombre(nombre):
	empleados[posicion].setNombre(nombre)

def cambiar_Fecha(fecha_Nacimiento):
	empleados[posicion].setFecha_Nacimiento(fecha_Nacimiento)

def cambiar_departamento(numero_departamento):
	empleados[posicion].setNumero_departamento(numero_departamento)
	
def cambiar_codigoJefe(codigo_jefe):
	empleados[posicion].setCodigo_jefe(codigo_jefe)
	
def cambiarHoras_extras(horas_extras):
	empleados[posicion].setHoras_extras(horas_extras)
	
def cambiarHoras_ordinarias(horas_ordinarias):
	empleados[posicion].setHoras_ordinarias(horas_ordinarias)
	
def cambiarMonto_hora(monto_hora):
	empleados[posicion].setMonto_horas(monto_hora)
	
def mostrar_egresos():
	contador=0
	for i in range (0,len(empleados)):
		salario_ordinario=empleados[i].getHoras_ordinarias()* empleados[i].getMonto_hora()
		salario_extra=empleados[i].getHoras_extras()*(empleados[i].getMonto_hora()*1.5)
		salario_bruto=salario_extra+salario_ordinario
		deducciones= salario_bruto*0.0917
		salario_neto=salario_bruto- deducciones
		contador+=salario_neto
	informacion="El total de egresos es: "+ str(contador)
	return informacion
	
def mostrar_horasLaboradas(self):
	contador_ordinarias=0
	contador_extras=0
	informacion=""
	for i in range(0,len(empleados)):
		contador_ordinarias+=empleados[i].getHoras_ordinarias()
		contador_extras+=empleados[i].getHoras_extras()
	informacion+=("La cantidad de horas extras trabajadas de todos los empleados es: "+str(contador_extras)+
	"\nLa cantidad de horas ordinarias trabajadas de todos los empleados es: "+str(contador_ordinarias))
	return informacion
	