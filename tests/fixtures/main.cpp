#include <Arduino.h>

// @inject "index.html"
const String page = "<html><body><h1>%titolo%</h1> sad <style>


</style></body><br>";

const String titolo = "Titoilo2";

// @inject "index.html"
const char paginaIndex2 PROGMEM = "<html><body><h1>%titolo%</h1> sad <style>ciao{font-size:12px}</style><script>if(true)" + color + ";console.log(\"" + ciao + "\")</script></body><br>";

// @inject "index.html"
const String paginaIndex2 = "<html><body><h1>%titolo%</h1> sad <style>


</style></body><br>";


// @inject "index2.html"
const String paginaIndex2 = "File not found: /home/francesco/Develop/Fulminati/arduino-web-inject/tests/fixtures/index2.html";
