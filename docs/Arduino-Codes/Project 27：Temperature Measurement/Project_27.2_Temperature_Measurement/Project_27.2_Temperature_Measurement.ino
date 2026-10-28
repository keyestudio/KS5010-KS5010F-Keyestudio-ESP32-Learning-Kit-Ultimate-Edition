//**********************************************************************************
/*  
 * Filename    : Temperature Measurement
 * Description : Different leds light up when the LM35 senses different temperatures
 * Author      : http//www.keyestudio.com
*/
#define PIN_ADC0       36      //the pin of the LM35 Sensor
#define PIN_GREENLED   4      //the pin of the Green led
#define PIN_YELLOWLED  2      //the pin of the Yellow led
#define PIN_REDLED     15      //the pin of the Red led
void setup() {
  Serial.begin(115200);
  pinMode(PIN_GREENLED, OUTPUT); //set PIN_GREENLED to OUTPUT
  pinMode(PIN_YELLOWLED, OUTPUT);//set PIN_YELLOWLED to OUTPUT
  pinMode(PIN_REDLED, OUTPUT);//set PIN_REDLED to OUTPUT
  pinMode(PIN_ADC0, INPUT);//set PIN_ADC0 to INPUT
}

void loop() {
  int adcVal = analogRead(PIN_ADC0);
  double voltage = adcVal / 4095.0 * 3.3;
  float temperatureC = (voltage * 1000.0) / 10.0 ;
  float temperatureF = (temperatureC * 1.8) + 32.0;
  Serial.print("ADC Value: " + String(adcVal));
  Serial.print("---Voltage Value: " + String(voltage) + "V");
  Serial.print("---temperatureC: " + String(temperatureC) + "℃");
  Serial.println("---temperatureF: " + String(temperatureF) + "F");
  if (temperatureC >= 25) {
    delay(100);
    digitalWrite(PIN_GREENLED, LOW);
    digitalWrite(PIN_YELLOWLED, LOW);
    digitalWrite(PIN_REDLED, HIGH);
  }
  else if (temperatureC >= 20 && temperatureC < 25) {
    digitalWrite(PIN_GREENLED, LOW);
    digitalWrite(PIN_YELLOWLED, HIGH);
    digitalWrite(PIN_REDLED, LOW);
  }
  else {
    digitalWrite(PIN_GREENLED, HIGH);
    digitalWrite(PIN_YELLOWLED, LOW);
    digitalWrite(PIN_REDLED, LOW);
  }

  delay(500);
}
//**********************************************************************************
