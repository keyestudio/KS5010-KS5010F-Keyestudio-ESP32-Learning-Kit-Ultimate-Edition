//**********************************************************************************
/*  
 * Filename    : Sound Control Fan
 * Description : Controlling the fan by Sound sensor.
 * Author      : http//www.keyestudio.com
*/
#define PIN_ADC0   36  //the pin of the Sound sensor
#define PIN_Motorla    15  // the Motor_IN+ pin of the motor
#define PIN_Motorlb    2 // the Motor_IN- pin of the motor

void setup() {
  pinMode(PIN_Motorla, OUTPUT);//set Motorla to OUTPUT
  pinMode(PIN_Motorlb, OUTPUT);//set Motorlb to OUTPUT
  pinMode(PIN_ADC0, INPUT);//set PIN_ADC2 to INPUT
}

void loop() {
  int adcVal = analogRead(PIN_ADC0); //read the ADC value of Sound sensor
  if (adcVal > 600) {
    digitalWrite(PIN_Motorla,HIGH); //rotate
    digitalWrite(PIN_Motorlb,LOW);
    delay(5000); //delay 5S
  }
  else
  {
    digitalWrite(PIN_Motorla,LOW); //stop rotating
    digitalWrite(PIN_Motorlb,LOW); 
  }
}
//**********************************************************************************
