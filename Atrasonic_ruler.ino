
const int TRIG_PIN = 7;
const int ECHO_PIN = 6;
float duration, distanceCm, distanceIn;

void setup() {
 
  Serial.begin(9600);
  pinMode(TRIG_PIN,OUTPUT);
  pinMode(ECHO_PIN,INPUT);
}
 
void loop()
{
   
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  duration = pulseIn(ECHO_PIN,HIGH);
 
  distanceCm = duration / 29.1 / 2 ;
  distanceIn = duration / 74 / 2;
  Serial.println(distanceCm);
/*
  if (distanceCm <= 0){
    Serial.println("Out of range");
  }
  else {
  
//ersal maghadir az tarigh serial
    Serial.print(distanceIn);
    Serial.print("in, ");
    Serial.print(distanceCm);
    Serial.print("cm");
    Serial.println(); 
  }
  */

  delay(300);
}
