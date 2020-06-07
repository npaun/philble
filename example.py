import uuid
import time
import Adafruit_BluefruitLE
import philble.client

ble = Adafruit_BluefruitLE.get_provider()
ble.initialize()

def blink(client):
    for i in range(10):
        time.sleep(.5)
        client.power(True)
        time.sleep(.5)
        client.power(False)

def main():
    ble.clear_cached_data()
    adapter = ble.get_default_adapter()
    adapter.power_on()
    adapter.start_scan()
    # ... Ensure your device gets loaded
    device = ble.find_device(uuid.UUID('7733a6b6-7027-4704-927c-8e3705c1b8d2'))
    adapter.stop_scan()
    device.connect()
    
    time.sleep(.5)
    client = philble.client.Client(device)
    blink(client)

    time.sleep(.5)
    adapter.poweroff()



ble.run_mainloop_with(main)
