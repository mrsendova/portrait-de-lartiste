// Déclaration des constantes
const int switchA = 4;
const int switchB = 5;
const int switchC = 6;
const int switchDA = 7;
const int switchDB = 8;
const int switchEA = 9;
const int switchEB = 10;
int rheoA = 0;
int rheoB = 1;
int temp = 2;

String sA = "0";
String sB = "0";
String sC = "0";
String sDA = "0";
String sDB = "0";
String sEA = "0";
String sEB = "0";
String rA = "0";
String rB = "0";
String temperature = "0";

void setup() {
  Serial.begin(9600); //on initialise la communication série
  
  // Initialiser les input
  pinMode(switchA, INPUT);
  pinMode(switchB, INPUT);
  pinMode(switchC, INPUT);
  pinMode(switchDA, INPUT);
  pinMode(switchDB, INPUT);
  pinMode(switchEA, INPUT);
  pinMode(switchEB, INPUT);
}

void loop() {
  //Lire l'état des variables
  sA = String(digitalRead(switchA));
  sB = String(digitalRead(switchB));
  sC = String(digitalRead(switchC));
  sDA = String(digitalRead(switchDA));
  sDB = String(digitalRead(switchDB));
  sEA = String(digitalRead(switchEA));
  sEB = String(digitalRead(switchEB));
  rA = String(analogRead(rheoA));
  rB = String(analogRead(rheoB));
  temperature = String(getTemperature(temp));

  String toReturn = sA + ";" + sB + ";" + sC + ";" + sDA + ";" + sDB + ";" + sEA + ";" + sEB + ";" + rA + ";" + rB + ";" + temperature;
  Serial.println(toReturn);
  
  delay(100);
}

float getTemperature(int pin){
  float voltage = analogRead(pin) * 0.004882814;
  float temperature = (voltage - .5) * 100;
  return temperature;
}
