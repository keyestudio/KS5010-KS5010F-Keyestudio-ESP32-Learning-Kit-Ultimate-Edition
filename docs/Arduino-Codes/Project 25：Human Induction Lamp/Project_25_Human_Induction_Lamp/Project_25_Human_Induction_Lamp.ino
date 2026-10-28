//**********************************************************************************
/*  
 * Filename    : Human Induction Lamp
 * Description : Controlling the LED by photosensitive sensor and PIR motion sensor.
 * Author      : http//www.keyestudio.com
*/
#define PIN_ADC0  36   //the pin of the photosensitive sensor
#define PIN_LED   4  // the pin of the LED
#define pirPin   15     // the pin of the PIR motion sensor
byte pirStat = 0;   // the state of the PIR motion sensor
void setup() {
  Serial.begin(115200);
  pinMode(PIN_LED, OUTPUT);
  pinMode(PIN_ADC0, INPUT);
  pinMode(pirPin, INPUT);
}

void loop() {
  int adcVal = analogRead(PIN_ADC0); //read the ADC value of photosensitive sensor
  pirStat = digitalRead(pirPin); //read the value of PIR motion sensor
  if (adcVal >= 2000) {
      if (pirStat == HIGH){
         digitalWrite(PIN_LED, HIGH);//turn on the LED
         } 
      else{
         digitalWrite(PIN_LED, LOW);//turn off the LED   
        }
  }
   else{
      digitalWrite(PIN_LED, LOW);//turn off the LED
      }
}
//**********************************************************************************
