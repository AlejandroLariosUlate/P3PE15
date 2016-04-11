__author__ = "Alejandro"
__date__ = "$10-abr-2016 19:44:14$"
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Menu.py
from Empleado import Empleado
import Operaciones
class Menu:
	
	
	def menu(self):
		
		opcion=0
		opcion2=0
		
		while(opcion<9):
			
			print("""
                    1. Ingresar un empleado nuevo.
                    2. Listado general de empleados.
                    3. Mostrar información de un empleado específico.
                    4. Modificar un empleado existente.
                    5. Mostrar el salario de un empleado.
                    6. Calcular el monto de planilla de cada empleado.
                    7. Calcular y mostrar el monto de total de egresos
                    8. Calcular y mostrar la cantidad de horas laboradas
                    9. Salir	
			""")
			
			opcion=int(input("Digite una opcion   > "))
			
			if(opcion ==1):
				codigo=int (input("Digite el codigo     "))
				nombre=input("Digite el nombre     ")
				fecha_Nacimiento=input("Digite la fecha de nacimiento     ")
				numero_departamento=int (input("Digite el numero de departamento     "))
				codigo_jefe=int (input("Digite el codigo del jefe     "))
				horas_extras=int (input("Digite las horas extras     "))
				horas_ordinarias=int (input("Digite las horas ordinarias     "))
				monto_hora=int (input("Digite el monto de la hora     "))
				print("\n\n\n")
                
				empleado_nuevo=Empleado(codigo, nombre, fecha_Nacimiento, numero_departamento, codigo_jefe, horas_extras, horas_ordinarias, monto_hora)
				print (Operaciones.agregar_empleado(empleado_nuevo))
				
			elif(opcion ==2):
				print (Operaciones.mostrar_empleados(self))
				
			elif(opcion==3):
				codigo=int (input("Digite el codigo     "))
				if(Operaciones.verificar_empleado(codigo)):
					print(Operaciones.empleado_especifico())
				else:
					print("Este codigo de empleado no existe")
			
			elif(opcion ==4):
				codigo=int (input("Digite el codigo"))
				if(Operaciones.verificar_empleado(codigo)):
					print("""
						Que desea Cambiar:
						
						1. Nombre
						2. Fecha de nacimiento
						3. Numero de departamento
						4. Codigo del jefe.
						5. Horas extras
						6. Horas ordinarias
						7. Monto hora
						
					""")
					opcion2=int(input("Digite una opcion > "))
					
					if(opcion2==1):
						nombre=input("Digite el nombre    ")
						Operaciones.cambiar_nombre(nombre)
					elif(opcion2==2):
						fecha_Nacimiento=input("Digite la fecha de nacimiento    ")
						Operaciones.cambiar_Fecha(fecha_Nacimiento)
					elif(opcion2==3):
						numero_departamento=int(input("Digite el numero del departamento    "))
						Operaciones.cambiar_departamento(numero_departamento)
					elif(opcion2==4):
						codigo_jefe=int(input("Digite el codigo del jefe     "))
						Operaciones.cambiar_codigoJefe(codigo_jefe)
					elif(opcion2==5):
						horas_extras=int(input("Digite la cantidad de horas extras      "))
						Operaciones.cambiarHoras_extras(horas_extras)
					elif(opcion2==6):
						horas_ordinarias=int(input("Digite la cantidad de horas ordinarias      "))
						Operaciones.cambiarHoras_ordinarias(horas_ordinarias)
					elif(opcion2==7):
						monto_hora=int(input("Digite el monto de hora     "))
						Operaciones.cambiarMonto_hora(monto_hora)
						
				else:
					print("El codigo que usted digito no pertenece a ningun empleado")
					
			elif(opcion==5):
				codigo=int (input("Digite el codigo"))
				if(Operaciones.verificar_empleado(codigo)):
					print ("Salario: "+Operaciones.mostrar_salario())
				else:
					print("El codigo que usted digito no pertenece a ningun empleado")
				
			elif(opcion==6):
				print (Operaciones.mostrar_planilla())
				
			elif(opcion==7):
				print (Operaciones.mostrar_egresos())
				
			elif(opcion==8):
				print (Operaciones.mostrar_horasLaboradas(self))
				
			elif(opcion==9):
				SystemExit(0)
				
menu=Menu()
menu.menu()