int led0 = 2;
int led1 = 3;
int led2 = 4;


void setup() {
  Serial.begin(9600); //on initialise la communication série

  //déclaration des différentes diodes
  pinMode(led0, OUTPUT);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);

}

int calcDelai() {
  int sensorValue = analogRead(A0);
  int delai = (sensorValue/5)+30;
  Serial.println(delai);
  return delai;
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(led0, HIGH);
  delay(calcDelai());
  digitalWrite(led0, LOW);
  digitalWrite(led1, HIGH);
  delay(calcDelai());
  digitalWrite(led1, LOW);
  digitalWrite(led2, HIGH);
  delay(calcDelai());
  digitalWrite(led2, LOW);
  delay(calcDelai());
}
