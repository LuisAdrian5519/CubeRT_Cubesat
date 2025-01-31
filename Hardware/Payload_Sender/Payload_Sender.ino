#include <SPI.h>
#include <LoRa.h>  
int counter = 0;
float c1, c2, total, volts1, volts2, signal, g1, g2, volts, br, breal, ac;
int v1, v2, i;

#include <Wire.h> // This library allows you to communicate with I2C devices.
const int MPU_ADDR = 0x68; // I2C address of the MPU-6050. If AD0 pin is set to HIGH, the I2C address will be 0x69.
int16_t accelerometer_x, accelerometer_y, accelerometer_z; // variables for accelerometer raw data
int16_t gyro_x, gyro_y, gyro_z; // variables for gyro raw data
int16_t temperature; // variables for temperature data
char tmp_str[12]; // temporary variable used in convert function
char* convert_int16_to_str(int16_t i) { // converts int16 to string. Moreover, resulting strings will have the same length in the debug monitor.
  sprintf(tmp_str, "%6d", i);
  return tmp_str;
  
}

void setup() {

  Serial.begin(115200);
  Serial.println("LoRa Sender");

  LoRa.setPins(8, 25,16);                     // NSS, RESET y DIO0.
  if (!LoRa.begin(915E6)) {                   // Frecuencia de la banda libre ISM en Europa. (868MHz) Si hay algun fallo de conexiones muestra el error.
    Serial.println("Starting LoRa failed!");
    while (1);
  }

//MPCU6050                     SETUP

  Wire.begin();
  Wire.beginTransmission(MPU_ADDR); // Begins a transmission to the I2C slave (GY-521 board)
  Wire.write(0x6B); // PWR_MGMT_1 register
  Wire.write(0); // set to zero (wakes up the MPU-6050)
  Wire.endTransmission(true); }

  void loop() {

 //MPCU6050                     LOOP
 Wire.beginTransmission(MPU_ADDR);
  Wire.write(0x3B); // starting with register 0x3B (ACCEL_XOUT_H) [MPU-6000 and MPU-6050 Register Map and Descriptions Revision 4.2, p.40]
  Wire.endTransmission(false); // the parameter indicates that the Arduino will send a restart. As a result, the connection is kept active.
  Wire.requestFrom(MPU_ADDR, 7*2, true); // request a total of 7*2=14 registers
  
  // "Wire.read()<<8 | Wire.read();" means two registers are read and stored in the same variable
  accelerometer_x = Wire.read()<<8 | Wire.read(); // reading registers: 0x3B (ACCEL_XOUT_H) and 0x3C (ACCEL_XOUT_L)
  accelerometer_y = Wire.read()<<8 | Wire.read(); // reading registers: 0x3D (ACCEL_YOUT_H) and 0x3E (ACCEL_YOUT_L)
  accelerometer_z = Wire.read()<<8 | Wire.read(); // reading registers: 0x3F (ACCEL_ZOUT_H) and 0x40 (ACCEL_ZOUT_L)
  temperature = Wire.read()<<8 | Wire.read(); // reading registers: 0x41 (TEMP_OUT_H) and 0x42 (TEMP_OUT_L)
  gyro_x = Wire.read()<<8 | Wire.read(); // reading registers: 0x43 (GYRO_XOUT_H) and 0x44 (GYRO_XOUT_L)
  gyro_y = Wire.read()<<8 | Wire.read(); // reading registers: 0x45 (GYRO_YOUT_H) and 0x46 (GYRO_YOUT_L)
  gyro_z = Wire.read()<<8 | Wire.read(); // reading registers: 0x47 (GYRO_ZOUT_H) and 0x48 (GYRO_ZOUT_L)

  
  //Aquí nos da los datos del acelerometro
  //print out data
  Serial.print("AX:");
  Serial.print(convert_int16_to_str(accelerometer_x));

  Serial.print("  | AY:"); 
  Serial.print(convert_int16_to_str(accelerometer_y));

  Serial.print("  | AZ:"); 
  Serial.print(convert_int16_to_str(accelerometer_z));

  Serial.print("  | AT:"); 
  Serial.print(temperature/340.00+36.53);
  
  Serial.print("  | GZ:");
  Serial.print(convert_int16_to_str(gyro_z));

  Serial.print("  | GY:");
  Serial.print(convert_int16_to_str(gyro_y)); 

  Serial.print("  | GX:");
  Serial.println(convert_int16_to_str(gyro_x));

 Serial.print("Sending packet: ");
 Serial.println(counter);

v1 = analogRead(A0);
  volts1 = (v1 * 3.3) /1023.0;
  c1 = volts1 * 100;
  v2 = analogRead(A1);
  volts2 = (v2 * 3.3) / 1023.0;
  c2 = volts2 * 100;
  total = c1 - c2;
  Serial.print("Temperatura: ");
  Serial.println(total);

  Serial.println("");

    signal = analogRead(A2);
    g1 = (signal * 3.3) / 1023.0;
    delay(100);
    signal = analogRead(A3);
    g2 = (signal * 3.3) / 1023.0;
    delay(100);

  Serial.println(g1);
  Serial.println(g2);

  br= analogRead(A4);
  breal=br*3.3/1023.0;
  breal=breal*3.0*1.015;
  Serial.println(breal);

   // send packet
  LoRa.beginPacket();
  LoRa.print(counter);
  LoRa.print("|");
  LoRa.print(convert_int16_to_str(accelerometer_x));
  LoRa.print("|");
  LoRa.print(convert_int16_to_str(accelerometer_y));
  LoRa.print("|");
  LoRa.print(convert_int16_to_str(accelerometer_z));
  LoRa.print("|");
  LoRa.print(temperature/340.00+36.53);
  LoRa.print("|");
  LoRa.print(convert_int16_to_str(gyro_z));
  LoRa.print("|");
  LoRa.print(convert_int16_to_str(gyro_y));
  LoRa.print("|");
  LoRa.print(convert_int16_to_str(gyro_x));
  LoRa.print("|");
  LoRa.print(total);
  LoRa.print("|");
  LoRa.print(g1);
  LoRa.print("|");
  LoRa.print(g2);
  LoRa.print("|");
  LoRa.print(breal);
  LoRa.endPacket();

  counter++;                                // Aumentar contador para el siguiente mensaje.
  delay(1000);
  }