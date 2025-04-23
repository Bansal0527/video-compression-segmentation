import serial

# Open the serial port with a timeout
ser = serial.Serial('COM24', 115200, timeout=1)

image_data = bytearray()

print("Reading image data...")

while True:
    line = ser.readline()
    if not line:
        continue

    if b"END" in line:
        print("End of image data reached.")
        break

    image_data += line  # accumulate raw bytes

# Save received data to a binary file
with open('received_image.raw', 'wb') as f:
    f.write(image_data)

print("Image saved as 'received_image.raw'") 