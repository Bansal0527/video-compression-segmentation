#include "frame_array.h"

void compressFrameDelta(const uint8_t input[64][64]);  // Function declaration

void setup() {
  Serial.begin(115200);
  while (!Serial);  // Wait for PC serial connection

  compressFrameDelta(frame);
}

void loop() {
  // Empty loop, only compress once in setup()
}

void compressFrameDelta(const uint8_t input[64][64]) {
  uint8_t prev = input[0][0];

  Serial.println("Compressed Frame: [delta values]");

  // Send initial value (required to reconstruct the image)
  Serial.print("Base: ");
  Serial.println(prev);

  for (int i = 0; i < 64; ++i) {
    for (int j = 0; j < 64; ++j) {
      // Skip the very first pixel
      if (i == 0 && j == 0) continue;

      uint8_t current = input[i][j];
      int16_t delta = (int16_t)current - (int16_t)prev;

      // Optional: clamp delta to fit in int8_t if needed
      if (delta < -128) delta = -128;
      if (delta > 127) delta = 127;

      Serial.println(delta);
      prev = current;
    }
  }
}