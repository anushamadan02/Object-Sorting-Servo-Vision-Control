#include <LiquidCrystal.h>  
int Contrast=20;
int data;
int LED=13;
int incrementY;
int incrementR;
int countR;
int countY;
 LiquidCrystal lcd(12, 11, 5, 4, 3, 2); 
void setup() { 
  analogWrite(6,Contrast);
  lcd.begin(16, 2);
  Serial.begin(9600);                               //initialize serial COM at 9600 baudrate
  pinMode(LED, OUTPUT);                    //declare the LED pin (13) as output
  digitalWrite (LED, LOW);                     //Turn OFF the Led in the beginning
  Serial.println("Hello!,How are you Python ?");  
  countR=0;
  countY=0;
  
}

  

void loop() {
  while (Serial.available())    //whatever the data that is coming in serially and assigning the value to the variable “data”
  { 
  data = Serial.read();
  }
  
  if (data !='1' && data !='0'  )
  {
  digitalWrite (LED, LOW);
  lcd.setCursor(0, 0);
  lcd.print("Pls Interact!!");
  incrementR=00;
  incrementY=00;
  }

  
  if (data == '1')
 {lcd.clear();
  digitalWrite (LED, HIGH);
  lcd.setCursor(0, 0);
  lcd.print("RED DETECTED  !!");
  lcd.setCursor(0, 1);
  incrementR=01;
  lcd.print(countR);
  
 }
  
  if (data == '0')
  {lcd.clear();
  digitalWrite (LED, LOW);
  lcd.setCursor(0, 0);
  lcd.print("YELLOW DETECTED!");
  lcd.setCursor(0, 1);
  incrementY=01;
  lcd.print(countY);
  }

  countR = countR + incrementR;
  countY = countY + incrementY;

  while (!Serial.available())    
  {
  incrementR=0;
  incrementY=0;
  }
}

