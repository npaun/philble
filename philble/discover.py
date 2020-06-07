import time
import sys
import os
unbuffered = os.fdopen(sys.stdout.fileno(), 'wb', 0)
MAX_TICKS = 40

def discover(ble, config):
    unbuffered.write(b'Discovering')
    ble.clear_cached_data()

    # Get the first available BLE network adapter and make sure it's powered on.
    adapter = ble.get_default_adapter()
    adapter.power_on()
    adapter.start_scan()

    found = False
    for _ in range(MAX_TICKS):
        unbuffered.write(b'.')
        time.sleep(.5)
        lights = [dev for dev in ble.find_devices() if dev.name == 'Hue Lamp']
        if len(lights) == len(config):
            found = True
            break

    if found:
        print('ok')
        for light in lights:
            light.connect()
    else:
        print('fail')
        raise SystemExit

    time.sleep(.5)
    return {config[light.id]:light for light in lights}
