#include <SPI.h>
#include <LoRa.h>
#include <Servo.h>

void setup() {
  Serial.begin(115200);
  Serial.println("LoRa Receiver");

  LoRa.setPins(8, 25, 16); // NSS, RESET y DIO0
  if (!LoRa.begin(915E6)) { // Frecuencia de la banda libre ISM en Europa. (868MHz)
    Serial.println("Starting LoRa failed!");
    while (1);
  
  const int servoPin = 9;
  Servo myServo;

  myServo.attach(servoPin);
  myServo.write(0); // Mueve el servomotor al extremo inicial
  delay(1000); // Espera un segundo

  myServo.write(180); // Mueve el servomotor al otro extremo
  delay(1000); // Espera un segundo
  }
}

void loop() {
  int packetSize = LoRa.parsePacket();
  if (packetSize) { // Se ha recibido un paquete.
    String receivedText = "";
    while (LoRa.available()) {
      receivedText += (char)LoRa.read();
    }
    
    // Separar y formatear el paquete recibido
    Serial.println("Received packet:");
    processPacket(receivedText);
    
    // Print RSSI of packet
    Serial.print(" with RSSI ");
    Serial.println(LoRa.packetRssi());
  }
}

void processPacket(String packet) {
    int startIndex = 0;
    int endIndex = packet.indexOf('|');

    int counter = packet.substring(startIndex, endIndex).toInt();

    startIndex = endIndex + 1;
    endIndex = packet.indexOf('|', startIndex);
    String ax = packet.substring(startIndex, endIndex);

    startIndex = endIndex + 1;
    endIndex = packet.indexOf('|', startIndex);
    String ay = packet.substring(startIndex, endIndex);

    startIndex = endIndex + 1;
    endIndex = packet.indexOf('|', startIndex);
    String az = packet.substring(startIndex, endIndex);

    startIndex = endIndex + 1;
    endIndex = packet.indexOf('|', startIndex);
    String temp = packet.substring(startIndex, endIndex);

    startIndex = endIndex + 1;
    endIndex = packet.indexOf('|', startIndex);
    String gz = packet.substring(startIndex, endIndex);

    startIndex = endIndex + 1;
    endIndex = packet.indexOf('|', startIndex);
    String gy = packet.substring(startIndex, endIndex);

    startIndex = endIndex + 1;
    endIndex = packet.indexOf('|', startIndex);
    String gx = packet.substring(startIndex, endIndex);

    startIndex = endIndex + 1;
    endIndex = packet.indexOf('|', startIndex);
    String lm35Data = packet.substring(startIndex, endIndex);

    startIndex = endIndex + 1;
    endIndex = packet.indexOf('|', startIndex);
    String g1 = packet.substring(startIndex, endIndex);

    startIndex = endIndex + 1;
    endIndex = packet.indexOf('|', startIndex);
    String g2 = packet.substring(startIndex, endIndex);

    startIndex = endIndex + 1;
    String breal = packet.substring(startIndex);

    // Print out the parsed data
    Serial.print("Counter: ");
    Serial.println(counter);

    Serial.print("AX: ");
    Serial.println(ax);

    Serial.print("AY: ");
    Serial.println(ay);

    Serial.print("AZ: ");
    Serial.println(az);

    Serial.print("Temperature: ");
    Serial.println(temp);

    Serial.print("GX: ");
    Serial.println(gx);

    Serial.print("GY: ");
    Serial.println(gy);

    Serial.print("GZ: ");
    Serial.println(gz);

    Serial.print("LM35: ");
    Serial.println(lm35Data);

    Serial.print("G1: ");
    Serial.println(g1);

    Serial.print("G2: ");
    Serial.println(g2);

    Serial.print("Breal: ");
    Serial.println(breal);
}


