//Leitura de distância com o sensor HC-SR04
#include <Ultrasonic.h>

Ultrasonic ultrassom(6,7); // define o nome do sensor(ultrassom)
//e onde esta ligado o trig(6) e o echo(7) respectivamente
 
long cm;
char flag = 'c'; 
// Esta função "setup" roda uma vez quando a placa e ligada ou resetada
 void setup() {
 Serial.begin(9600); //Habilita Comunicação Serial a uma taxa de 9600 bauds.
 pinMode(8, OUTPUT);//verde
 pinMode(9, OUTPUT);//amarelo
 pinMode(10, OUTPUT);//vermelho
 
 }
 
// Função que se repete infinitamente quando a placa é ligada
 void loop()
 {
   cm = ultrassom.Ranging(CM);// ultrassom.Ranging(CM) retorna a distancia em
                                     // centímetros(CM) ou polegadas(INC)
   if(cm >= 50 ){
    digitalWrite(8, HIGH);
    digitalWrite(9, LOW);
    digitalWrite(10, LOW);
    flag = 'g';
  }else if(cm >= 10 && cm < 50){
    digitalWrite(8, LOW);
    digitalWrite(9, HIGH);
    digitalWrite(10, LOW);
    flag = 'y';
  }else if(cm < 10){
    digitalWrite(8, LOW);
    digitalWrite(9, LOW);
    digitalWrite(10, HIGH);
    flag = 'r';
  }

  Serial.print('*');
  Serial.print(cm);
  Serial.print(flag);
  Serial.print('#');
  delay(300);
 }
 
