int greenLED = 2;
int redLED   = 3;
int buzzer   = 5;
int in1      = 7;   // L298N IN1
int in2      = 8;   // L298N IN2

void setup() {
  pinMode(greenLED, OUTPUT);
  pinMode(redLED, OUTPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);

  Serial.begin(9600);
  motorOff();  // start with motor off
}

void loop() {
  if (Serial.available()) {
    char c = Serial.read();

    if (c == 'O') {             // Eyes open
      digitalWrite(greenLED, HIGH);
      digitalWrite(redLED, LOW);
      digitalWrite(buzzer, LOW);
      motorOn();

    } else if (c == 'C') {      // Eyes closed
      digitalWrite(greenLED, LOW);
      digitalWrite(redLED, HIGH);
      digitalWrite(buzzer, HIGH);
      motorOff();

    } else if (c == 'N') {      // No face detected
      digitalWrite(greenLED, LOW);
      digitalWrite(redLED, LOW);
      digitalWrite(buzzer, LOW);
      motorOff();

    } else {
      // Unknown input → safe fallback
      motorOff();
      digitalWrite(greenLED, LOW);
      digitalWrite(redLED, LOW);
      digitalWrite(buzzer, LOW);
    }
  }
}

// ---------------- Motor Functions ----------------
void motorOn() {
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);   // motor runs in one direction
}

void motorOff() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);   // motor stops
}