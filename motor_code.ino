/*


*/
// Varibles
int EN_A = 11;
int IN1 = 9;
int IN2 = 8;
int motor_speed;
int motor_speed2;
int motor_speed3;
int motor_speed4;
int switch_pin = 3;
const int trigPin = 12;
const int echoPin = 13;
int switch_state = 0;
float distance, duration;


void setup() {
// set up the pins and start monitor
pinMode(EN_A, OUTPUT);
pinMode(IN1, OUTPUT);
pinMode(IN2, OUTPUT);
pinMode(switch_pin, INPUT);
pinMode(trigPin, OUTPUT);
pinMode(echoPin, INPUT);
Serial.begin(9600);
}


void loop() {
  // set the switch equal to zero
  switch_state = digitalRead(switch_pin);
  // get the distance sensor to run contantly
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // set the distance varible
  duration = pulseIn(echoPin, HIGH);
  distance = (duration * 0.034)/2;
  // print the distance
  Serial.print("Distance: ");
  Serial.println(distance);
  delay(100);
  // set the different motor speeds
  motor_speed = 255;
  motor_speed2 = 200;
  motor_speed3 = 150;
  motor_speed4 = 150;
  // set the differnt zones
  if((switch_state == HIGH) && (distance > 101)){
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  analogWrite(EN_A, motor_speed);
  }
 
  else if((switch_state == HIGH) && (distance < 100) && (distance > 81)){
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  analogWrite(EN_A, motor_speed2);
  }


  else if((switch_state == HIGH) && (distance < 80) && (distance > 51)){
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  analogWrite(EN_A, motor_speed3);
  }


  else if((switch_state == HIGH) && (distance < 50) && (distance > 0)){
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  analogWrite(EN_A, motor_speed4);
  }
  // when off
  else{
  digitalWrite(EN_A, LOW);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  }
}
