#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk, font
import getpass


class Terminal():
    """
        Este objeto recoge todas las propiedades de un terminal asi
        como su interfaz grafica
    """
    
    
    def __init__(self,Parent,row,focus = False):
        
        self.enumPtos = ['RA0','RA1','RA2','RA3','RA4','RA5','RA6',# """,'RA7'"""
                        'RB0','RB1','RB2','RB3','RB4','RB5','RB6','RB7',
                        'RC0','RC1','RC2','RC3','RC4','RC5','RC6','RC7',
                        'RD0','RD1','RD2','RD3','RD4','RD5','RD6','RD7',
                        'RE0','RE1','RE2','RE3', # 'RB4','RB5','RB6','RB7'
                        'No']
        
        self.enumDir = ['I','O','Clk','AN']
        self.enumEdo = ['H','L','Z']
        
        self.Pin = self.enumPtos[row] #Debe coincidir con los enumerados
        self.Dir = self.enumDir[0]
        self.Edo = self.enumEdo[0]
        self.botonPin = ttk.Button(Parent.raiz, text = self.Pin, 
                                 command = self.SeleccionPin)        
        self.botonDir = ttk.Button(Parent.raiz, text=self.Dir, 
                                 command = self.SeleccionDir)
        self.botonVal = ttk.Button(Parent.raiz, text=self.Edo, 
                                 command = self.SeleccionVal)
                                 
        self.botonPin.grid(column=0, row=row, padx=3, pady=5,
                            sticky=(N, S, E, W))
        self.botonDir.grid(column=1, row=row, padx=3, pady=5,
                            sticky=(N, S, E, W))
        self.botonVal.grid(column=2, row=row, padx=3, pady=5,
                            sticky=(N, S, E, W))                         
                                 
                                 
        if focus : self.botonPin.focus_set()   
        
                                                        
    def SeleccionPin(self):
        
        i = self.enumPtos.index(self.Pin)
        i +=1
        if i>=len(self.enumPtos): i=0;
        self.Pin = self.enumPtos[i]
        self.botonPin.config(text = self.Pin)  
        
        
        
            
    def SeleccionDir(self):
        
        i = self.enumDir.index(self.Dir)
        i +=1
        if i>=len(self.enumDir): i=0;
        self.Dir = self.enumDir[i]
        self.botonDir.config(text = self.Dir) # Cambiar de color
        
        
        pass # Configurar el puerto
        

        
            
    def SeleccionVal(self):
        
        i = self.enumEdo.index(self.Edo)
        i +=1
        if i>=len(self.enumEdo): i=0;
        self.Edo = self.enumEdo[i]
        self.botonVal.config(text = self.Edo) # ambiar de color
            
        pass # Enviar el valor
             # o clockear    
    
    

class Aplicacion():
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("MEPIC18F GPIO")
        
        # Cambia el formato de la fuente actual a negrita para
        # resaltar las dos etiquetas que acompañan a las cajas
        # de entrada. (Para este cambio se ha importado el  
        # módulo 'font' al comienzo del programa):
        
        fuente = font.Font(weight='bold')
        # Define la dimensión de la ventana
        self.raiz.geometry("300x650")
       
        
        # Se definen dos botones con dos métodos: El botón
        # 'Aceptar' llamará al método 'self.aceptar' cuando
        # sea presionado para validar la contraseña; y el botón
        # 'Cancelar' finalizará la aplicación si se llega a
        # presionar:
        
        self.Pin1 = Terminal(self,0,True)
        self.Pin2 = Terminal(self,1)
        self.Pin2 = Terminal(self,2)
        self.Pin2 = Terminal(self,3)
        self.Pin2 = Terminal(self,4)
        self.Pin2 = Terminal(self,5)
        self.Pin2 = Terminal(self,6)
        self.Pin2 = Terminal(self,7)
        self.Pin2 = Terminal(self,8)
        self.Pin2 = Terminal(self,9)
        self.Pin2 = Terminal(self,10)
        self.Pin2 = Terminal(self,11)
        self.Pin2 = Terminal(self,12)
        self.Pin2 = Terminal(self,13)
        self.Pin2 = Terminal(self,14)
        self.Pin2 = Terminal(self,15)
        
        
        
        
        
        self.separ1 = ttk.Separator(self.raiz, orient=HORIZONTAL)
                                                                  
        self.botonQuit = ttk.Button(self.raiz, text = "Quit", 
                                    command=quit)
        self.botonConfig = ttk.Button(self.raiz, text = "Config", 
                                    command=self.Configuracion)
                                 
        """
                    Para conseguir que la cuadricula y los widgets se
            adapten al contenedor, si se amplia o reduce el tamaño
            de la ventana, es necesario definir la opción 'sticky'.
            Cuando un widget se ubica en el grid se coloca en el
            centro de su celda o cuadro. Con 'sticky' se
            establece el comportamiendo 'pegajoso' que tendrá el
            widget dentro de su celda, cuando se modifique la
            dimensión de la ventana. Para ello, se utilizan para
            expresar sus valores los puntos cardinales: N (Norte),
            S (Sur), (E) Este y (W) Oeste, que incluso se pueden
            utilizar de forma combinada. El widget se quedará
            'pegado' a los lados de su celda en las direcciones
            que se indiquen. cuando la ventana cambie de tamaño.
            Pero con definir la opción 'sticky' no es suficiente:
            hay activar esta propiedad más adelante.
        """
        
        self.separ1.grid(column=0, row=50, columnspan = 3, padx=10, pady=5,
                            sticky=(N, S, E, W))
                         
        self.botonQuit.grid(column=0, row=51, padx=5, pady=5,
                            sticky=(N, S, E, W))
        self.botonConfig.grid(column=2, row=51, padx=5, pady=5,
                            sticky=(N, S, E, W))
        
        # pueda empezar a escribir directamente:
                
        
        self.raiz.mainloop()
    def Configuracion(self):
        
        ### Leer de configuración
        PtoSerial = "/dev/ttyACM0"
        import serial
        ser = serial.Serial(PtoSerial)  # open serial port
        print(ser.name)         # check which port was really used
        #line = ser.readline()   # read a '\n' terminated line
        #print(line)
        ser.write(b'out ra4 hi\n')     # write a string
        ser.close()             # close port

        pass
    
    

def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()
