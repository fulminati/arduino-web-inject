/**
 * WiFi Web Server
 * A simple web server that shows the value of the analog input pins using a WiFi shield.
 * This example is written for a network using WPA encryption.
 * For WEP or WPA, change the Wifi.begin() call accordingly.
 * Circuit:
 *  - WiFi shield attached
 *  - Analog inputs attached to pins A0 through A5 (optional)
 * Created 13 July 2010 by dlf (Metodo2 srl)
 * Modified 31 May 2012 by Tom Igoe
 */

#include <SPI.h>
#include <WiFi.h>

char ssid[] = "yourNetwork";
char pass[] = "secretPassword";
int keyIndex = 0;

int status = WL_IDLE_STATUS;

WiFiServer server(80);

String indexPage() {
    // @inject "web/index.html"
    const String indexPage = "<!DOCTYPE HTML><html></html>";

    return indexPage;
}

void setup() {
  Serial.begin(9600);
  while (!Serial) {;}
  if (WiFi.status() == WL_NO_SHIELD) {
    Serial.println("WiFi shield not present");
    while (true);
  }
  String fv = WiFi.firmwareVersion();
  if (fv != "1.1.0") {
    Serial.println("Please upgrade the firmware");
  }
  while (status != WL_CONNECTED) {
    Serial.print("Attempting to connect to SSID: ");
    Serial.println(ssid);
    status = WiFi.begin(ssid, pass);
    delay(10000);
  }
  server.begin();
  printWifiStatus();
}

void loop() {
  WiFiClient client = server.available();
  if (client) {
    Serial.println("new client");
    bool currentLineIsBlank = true;
    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        Serial.write(c);
        if (c == '\n' && currentLineIsBlank) {
          client.println("HTTP/1.1 200 OK");
          client.println("Content-Type: text/html");
          client.println("Connection: close");
          client.println("Refresh: 5");
          client.println();
          client.println("<!DOCTYPE HTML>");
          client.println("<html>");
          for (int analogChannel = 0; analogChannel < 6; analogChannel++) {
            int sensorReading = analogRead(analogChannel);
            client.print("analog input ");
            client.print(analogChannel);
            client.print(" is ");
            client.print(sensorReading);
            client.println("<br />");
          }
          client.println("</html>");
          client.println(indexPage())
          break;
        }
        if (c == '\n') {
          currentLineIsBlank = true;
        } else if (c != '\r') {
          currentLineIsBlank = false;
        }
      }
    }
    delay(1);
    client.stop();
    Serial.println("client disconnected");
  }
}

void printWifiStatus() {
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());
  IPAddress ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);
  long rssi = WiFi.RSSI();
  Serial.print("signal strength (RSSI):");
  Serial.print(rssi);
  Serial.println(" dBm");
}
