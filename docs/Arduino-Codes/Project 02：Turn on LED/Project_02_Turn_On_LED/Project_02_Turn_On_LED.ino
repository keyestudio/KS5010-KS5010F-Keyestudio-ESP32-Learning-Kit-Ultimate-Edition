//**********************************************************************
/*
 * Filename    : Turn On LED
 * Description : Make an led on.
 * Author      : http//www.keyestudio.com
*/
#define LED_BUILTIN 15

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
}
void loop() {
  digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
}
//*************************************************************************************
