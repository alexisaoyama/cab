from smbus2 import SMBus
import time
# Nvidia Jetson Nano i2c Bus 0
bus = SMBus(0)

# This is the address we setup in the Arduino Program
address = 0x40


def writeNumber(value):
    bus.write_byte(address, value)
    # bus.write_byte_data(address, 0, value)
    return -1


def readNumber():
    number = bus.read_byte(address)
    # number = bus.read_byte_data(address, 1)
    return number


while True:
    var = input("")
    if not var:
        continue

    writeNumber(int(var))
    number = readNumber()
