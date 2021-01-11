//======== Motor Left =========
#define pin_MOTOR_DIRL 10
#define pin_MOTOR_PWML 9
//======== Motor Right =========
#define pin_MOTOR_DIRR 11
#define pin_MOTOR_PWMR 12

char data;

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);
  pinMode(pin_MOTOR_DIRR, OUTPUT);
  pinMode(pin_MOTOR_PWMR, OUTPUT);
  pinMode(pin_MOTOR_DIRL, OUTPUT);
  pinMode(pin_MOTOR_PWML, OUTPUT);
}

void loop() {
  delayMicroseconds(1000);
  while (Serial.available()) {
    data = Serial.read();
    switch (data) {
      case 'A':
        // motorMaju(); with Wall Follower
        digitalWrite(LED_BUILTIN, HIGH);
        delay(50);
        break;
      case 'B':
        // motorMaju(); with Wall Follower
        digitalWrite(LED_BUILTIN, HIGH);
        delay(50);
        break;
      case 'C':
        // motorMaju(); with Wall Follower
        digitalWrite(LED_BUILTIN, HIGH);
        delay(50);
        break;
      case 'D':
        // motorMaju(); with Wall Follower
        digitalWrite(LED_BUILTIN, HIGH);
        delay(50);
        break;
      case 'E':
        // motorMaju(); with Wall Follower
        digitalWrite(LED_BUILTIN, HIGH);
        delay(50);
        break;
      case 'F':
        // motorMaju(); with Wall Follower
        digitalWrite(LED_BUILTIN, HIGH);
        delay(50);
        break;
      case 'S':
        //        Serial.println("0");
        // motorMati();
        digitalWrite(LED_BUILTIN, LOW);
        delay(50);
        break;
      case 'T':
        // BukaSampah(); with Wall Follower
        digitalWrite(LED_BUILTIN, HIGH);
        delay(50);
        break;
      case 'U':
        // TutupSampah(); with Wall Follower
        digitalWrite(LED_BUILTIN, HIGH);
        delay(50);
        break;
      case 'V':
        // DorongSampah(); with Wall Follower
        digitalWrite(LED_BUILTIN, HIGH);
        delay(50);
        break;
      case 'W':
        // TarikSampah(); with Wall Follower
        digitalWrite(LED_BUILTIN, HIGH);
        delay(50);
        break;
    }
  }
  Serial.print(data);
  delay(100);
}


void motor(int L, int R) {
  if (L > 0) {
    analogWrite(pin_MOTOR_DIRL, 0);
    analogWrite(pin_MOTOR_PWML, L);
  } else {
    L = L * (-1);
    analogWrite(pin_MOTOR_DIRL, L);
    analogWrite(pin_MOTOR_PWML, 0);
  }
  //======================================
  if (R > 0) {
    analogWrite(pin_MOTOR_DIRR, 0);
    analogWrite(pin_MOTOR_PWMR, R);
  } else {
    R = R * (-1);
    analogWrite(pin_MOTOR_DIRR, R);
    analogWrite(pin_MOTOR_PWMR, 0);
  }
}
