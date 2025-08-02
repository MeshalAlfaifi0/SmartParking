// مداخل اللمبات
const int RED_LED = 2;
const int GREEN_LED = 3;

const int DIR_RIGHT_LED = 4;
const int DIR_LEFT_LED = 5;

const int ZONE1_LED = 6;
const int ZONE2_LED = 7;
const int ZONE3_LED = 8;
const int ZONE4_LED = 9;

void setup() {
  // تحديد كل المخارج
  pinMode(RED_LED, OUTPUT);
  pinMode(GREEN_LED, OUTPUT);
  pinMode(DIR_RIGHT_LED, OUTPUT);
  pinMode(DIR_LEFT_LED, OUTPUT);
  pinMode(ZONE1_LED, OUTPUT);
  pinMode(ZONE2_LED, OUTPUT);
  pinMode(ZONE3_LED, OUTPUT);
  pinMode(ZONE4_LED, OUTPUT);

  // تشغيل الاتصال مع الحاسب
  Serial.begin(9600);
  
  clearAll();  // بداية نظيفة
}

void loop() {
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');
    command.trim();  // تنظيف المسافات الزائدة

    if (command == "OPEN_RIGHT") {
      openGate();
      showDirection("RIGHT");
    } else if (command == "OPEN_LEFT") {
      openGate();
      showDirection("LEFT");
    } else if (command == "FULL") {
      closeGate();
    } else if (command.startsWith("SHOW_ZONE")) {
      showZone(command);
    } else if (command == "CLEAR_ALL") {
      clearAll();
    }
  }
}

// فتح البوابة
void openGate() {
  digitalWrite(GREEN_LED, HIGH);
  digitalWrite(RED_LED, LOW);
}

// إغلاق البوابة
void closeGate() {
  digitalWrite(GREEN_LED, LOW);
  digitalWrite(RED_LED, HIGH);
}

// توجيه السائق
void showDirection(String dir) {
  digitalWrite(DIR_RIGHT_LED, dir == "RIGHT");
  digitalWrite(DIR_LEFT_LED, dir == "LEFT");
}

// تفعيل منطقة مواقف واحدة
void showZone(String command) {
  clearZones(); // أولًا نطفي الكل

  if (command == "SHOW_ZONE 1") digitalWrite(ZONE1_LED, HIGH);
  else if (command == "SHOW_ZONE 2") digitalWrite(ZONE2_LED, HIGH);
  else if (command == "SHOW_ZONE 3") digitalWrite(ZONE3_LED, HIGH);
  else if (command == "SHOW_ZONE 4") digitalWrite(ZONE4_LED, HIGH);
}

// مسح كل المؤشرات
void clearAll() {
  closeGate();
  digitalWrite(DIR_RIGHT_LED, LOW);
  digitalWrite(DIR_LEFT_LED, LOW);
  clearZones();
}

// إطفاء لمبات المناطق فقط
void clearZones() {
  digitalWrite(ZONE1_LED, LOW);
  digitalWrite(ZONE2_LED, LOW);
  digitalWrite(ZONE3_LED, LOW);
  digitalWrite(ZONE4_LED, LOW);
}
