// ArduinoJson - arduinojson.org
// Copyright Benoit Blanchon 2014-2018
// MIT License
//
// This example shows how to deserialize a JSON document with ArduinoJson.

#include <iostream>
#include "ArduinoJson.h"

int main()
{
  // Memory pool for JSON object tree.
  //
  // Inside the brackets, 200 is the size of the pool in bytes,
  // If the JSON object is more complex, you need to increase that value.
  // See https://bblanchon.github.io/ArduinoJson/assistant/
  StaticJsonBuffer<200> jsonBuffer;

  // StaticJsonBuffer allocates memory on the stack, it can be
  // replaced by DynamicJsonBuffer which allocates in the heap.
  //
  // DynamicJsonBuffer  jsonBuffer(200);

  // JSON input string.
  //
  // It's better to use a char[] as shown here.
  // If you use a const char* or a String, ArduinoJson will
  // have to make a copy of the input in the JsonBuffer.
  char json[] =
      "{\"sensor\":\"gps\",\"time\":1351824120,\"data\":[48.756080,2.302038]}";

  // Root of the object tree.
  //
  // It's a reference to the JsonObject, the actual bytes are inside the
  // JsonBuffer with all the other nodes of the object tree.
  // Memory is freed when jsonBuffer goes out of scope.
  JsonObject& root = jsonBuffer.parseObject(json);

  // Test if parsing succeeds.
  if (!root.success()) {
    std::cerr << "parseObject() failed" << std::endl;
    return 1;
  }

  // Fetch values.
  //
  // Most of the time, you can rely on the implicit casts.
  // In other case, you can do root["time"].as<long>();
  const char* sensor = root["sensor"];
  long time = root["time"];
  double latitude = root["data"][0];
  double longitude = root["data"][1];

  // Print values.
  std::cout << sensor << std::endl;
  std::cout << time << std::endl;
  std::cout << latitude << std::endl;
  std::cout << longitude << std::endl;
    
  return 0;
}
