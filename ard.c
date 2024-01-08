const int ldrPin = A0;
const int noisePin = A1;
const int micPin = A2;


void setup() {
  Serial.begin(9600);
  delay(2000);
}

void loop() {
  int ldrValue = analogRead(ldrPin);
  Serial.println(ldrValue);
  delay(500);

  int micValue = analogRead(micPin);
  Serial.println(micValue);
  delay(500);

  int noiseValue = analogRead(noisePin);
  Serial.println(noiseValue);
  delay(500);
}
