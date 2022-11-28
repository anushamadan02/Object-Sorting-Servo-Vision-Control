#include <LiquidCrystal.h>  
int Contrast=20;
int data;
int LED=13;
 LiquidCrystal lcd(12, 11, 5, 4, 3, 2);   

void setup() { 
  analogWrite(6,Contrast);
  lcd.begin(16, 2);
  Serial.begin(9600);                               //initialize serial COM at 9600 baudrate
  pinMode(LED, OUTPUT);                    //declare the LED pin (13) as output
  digitalWrite (LED, LOW);                     //Turn OFF the Led in the beginning
  Serial.println("Hello!,How are you Python ?");
}
void loop() {
  while (Serial.available())    //whatever the data that is coming in serially and assigning the value to the variable “data”
  { 
  data = Serial.read();
  }
  
  if (data !='1' && data !='0' )
  {digitalWrite (LED, LOW);
  lcd.setCursor(0, 0);
  lcd.print("Pls Interact!!");
 
  }
  
  if (data == '1')
 { digitalWrite (LED, HIGH);
  lcd.setCursor(0, 0);
  lcd.print("YAYY IT'S BRIGHT!");
  
 }
  
  if (data == '0')
  {
  digitalWrite (LED, LOW);
  lcd.setCursor(0, 0);
  lcd.print("Nahh it's Darkk!!");
  
  
  
  }
}
