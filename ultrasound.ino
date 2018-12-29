int enL=10;
const int motor1Pin = 6;
const int motor2Pin = 3;

void setup() {
   Serial.begin(9600);
   pinMode(enL,OUTPUT);
   pinMode(motor1Pin, OUTPUT);
   pinMode(motor2Pin, OUTPUT);
}

void loop() {
  digitalWrite(motor1Pin, HIGH);
  digitalWrite(motor2Pi n, LOW);
  analogWrite(enL,255); 
  delay(1500); 
  digitalWrite(motor1Pin, LOW);
  digitalWrite(motor2Pin, HIGH);
  analogWrite(enL,255); 
  delay(1500); 
}
  
