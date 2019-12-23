void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  delay(100);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("99999");
  delay(100);
  Serial.println("11111");
  delay(100);
  Serial.println("22222");
  delay(100);
  Serial.println("33333");
}
