int pinRheostat = 0;
int pinTemperature = 1;


void setup() {
 Serial.begin(9600);
}

void loop() {
 String temperature = String(getTemperature(pinTemperature));
 String positionRheostat = String(getPositionRheostat(pinRheostat));
 String toReturn = temperature + ";" + positionRheostat;
 Serial.println(toReturn);
 delay(1000);
}

float getTemperature(int pin){
  float voltage = analogRead(pin) * 0.004882814;
  float temperature = (voltage - .5) * 100;
  return temperature;
}

int getPositionRheostat(int pin){
  int valeur = map(analogRead(pin), 0, 1023, 0, 100);
  return valeur;
}
