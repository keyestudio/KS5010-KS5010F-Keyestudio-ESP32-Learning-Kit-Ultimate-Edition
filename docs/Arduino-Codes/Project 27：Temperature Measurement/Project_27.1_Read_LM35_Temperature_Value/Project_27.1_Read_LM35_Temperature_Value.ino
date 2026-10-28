//**********************************************************************************
/*  
 * Filename    : Read LM35 Temperature Value
 * Description : ADC value is converted to LM35 temperature value
 * Author      : http//www.keyestudio.com
*/
#define PIN_ANALOG_IN  36  //the pin of the Temperature Sensor

void setup() {
  Serial.begin(115200);
}

//In loop()，the analogRead() function is used to obtain the ADC value, 
//and then the map() function is used to convert the value into an 8-bit precision DAC value. 
//Calculate the measured voltage value,Celsius and Fahrenheit valuesthrough the formula, 
//and print these data through the serial port monitor.
void loop() {
  int adcVal = analogRead(PIN_ANALOG_IN);
  int dacVal = map(adcVal, 0, 4095, 0, 255);
  double voltage = adcVal / 4095.0 * 3.3;
  float temperatureC = (voltage * 1000.0) / 10.0 ;
  float temperatureF = (temperatureC * 1.8) + 32.0;
  Serial.print("ADC Value: " + String(adcVal));
  Serial.print("--DAC Value: " + String(dacVal));
  Serial.print("--Voltage Value: " + String(voltage) + "V");
  Serial.print("--temperatureC: " + String(temperatureC) + "℃");
  Serial.println("--temperatureF: " + String(temperatureF) + "F");
  delay(200);
}
//**********************************************************************************
