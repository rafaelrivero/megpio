/*-----------------------------------------------------
Author:  L(I+D)E Rafael E. Rivero N.
Date: 2019-04-30
Description: Recibe comandos mediante pto serial via USB

-----------------------------------------------------*/


/* Relación de terminales
PIC18F4550 I/P
Pin No Alias
6 29 USERLED
7 17 
40 7 RB7
39 6
38 5
37 4
36 3
35 2
34 1
33 0 RB0
PIC18F45K50 I/P
*/

#include <string.h>
#include <stdio.h>
#include <stdlib.h>
//	Input/Output on GNU/Linux:	sudo minicom -o -D /dev/ttyACM0
// 9600bps 8bit No paridad, 1bit de stop

u8 c=0;
char str[10];
char *cmd;
char *arg1;
char *arg2;
char *arg3;
u16 volatile flag = 0;
u16 volatile cycles;

void blink(int p){
//Verificar que el terminal esta de salida
	pinMode(p, OUTPUT);

	//delay(500);
    	digitalWrite(p, HIGH);
    	delay(100);    
    	digitalWrite(p, LOW);

}

void interrupt()
{
    if (Int.isFlagSet(INT_TMR0) == 1)
    {
        flag++;
        TMR0H = highByte(cycles);
        TMR0L =  lowByte(cycles);
        Int.clearFlag(INT_TMR0);
        if (flag >= 500) // 500 ms
        {
            flag = 0;
            toggle(USERLED);
        }        
    }
}


void setup() {
    // put your setup code here, to run once:

    // Timer0 1ms
    cycles = 0xFFFF - ( System.getPeripheralFrequency() / 1000 );
    TMR0H = highByte(cycles);
    TMR0L =  lowByte(cycles);
    T0CON = T0_ON | T0_16BIT | T0_SOURCE_INT | T0_PS_OFF;

    Int.clearFlag(INT_TMR0);
    Int.enable(INT_TMR0);
    Int.start();



    // Identificación del equipo
    CDC.printf("MEPIC18F GPIO L(I+D)E r*r \r\n rev 20190430\n");

    //delay(500);
    // blink(17);

    
}


void SetPin(char *strPin){

	int pin;
	pin = atoi(strPin);	
	
	//pin = 17; 
			
	//Verificar que el terminal esta de salida
	pinMode(pin, OUTPUT);
	digitalWrite(pin, HIGH);
          //blink(17);
	//CDC.printf("Setting %d\r\n\n",pin);
	//CDC.printf("USERLED %d\r\n\n",USERLED);
}

void ResetPin(char *strPin){

	int pin;
	
	pin = atoi(strPin);	
	
	//pin = 17; 
			
	//Verificar que el terminal esta de salida
	pinMode(pin, OUTPUT);
	digitalWrite(pin, LOW); 

	//blink(17);
	//CDC.printf("Resetting %d\r\n\n",pin);

}



void loop() {
   
   
   //CDC.printf("Esperando por comando: >CMD Arg1 Arg2...\n \n\r");
   //blink(29); //USERLED
   memset(str,0,10); 
   strcpy(str,CDC.getString());
   delay(500);
   //strcpy(str,"set 17");
   //strcpy(str,"reset 17");
   cmd  = strtok(str," ,:/"); // Extrayendo el comando
   cmd = strlwr(cmd);

   // Extrayendo los argumentos
   arg1 = cmd+(u8)(strlen(cmd)+1); 
   arg1 = strtok(arg1," ,:/");
   arg1 = strlwr(arg1);
   arg2 = arg1+(u8)(strlen(arg1)+1);
   arg2 = strtok(arg2," ,:/");
   arg2 = strlwr(arg2);
   arg3 = arg2+(u8)(strlen(arg2)+1);
   arg3 = strtok(arg3," ,:/");
   arg3 = strlwr(arg3);

   // Solo para fines de depuración 
   if (cmd != NULL) CDC.printf("cmd: %s\n\r",cmd);
   if (arg1 != NULL) CDC.printf("arg1: %s\n\r",arg1);
   if (arg2 != NULL) CDC.printf("arg2: %s\n\r",arg2);
   if (arg3 != NULL) CDC.printf("arg3: %s\n\r",arg3);



   // Identificando el comando y ejecutando
   if (strcmp(cmd,"set") == 0){
	 SetPin(arg1);
   } else if (strcmp(cmd,"reset") == 0){
	 ResetPin(arg1);
   };

    
    
    //delay(500); // Tiempo de espera en el lazo
    
}
