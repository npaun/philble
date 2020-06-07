import uuid
import time
import Adafruit_BluefruitLE
import philble.client

ble = Adafruit_BluefruitLE.get_provider()
ble.initialize()

def blink(client):
    print('Blinking')
    for i in range(10):
        time.sleep(1)
        print('on')
        client.power(True)
        time.sleep(1)
        print('off')
        client.power(False)

def main():
    print('Discovering')
    ble.clear_cached_data()
    adapter = ble.get_default_adapter()
    adapter.power_on()
    adapter.start_scan()
    device = ble.find_device()
    adapter.stop_scan()
    print('Discovered')

    device.connect()
    
    time.sleep(.5)
    client = philble.client.Client(device)
    blink(client)

    time.sleep(.5)
    adapter.power_off()



ble.run_mainloop_with(main)
