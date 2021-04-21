import time
import sys
import os
unbuffered = os.fdopen(sys.stdout.fileno(), 'wb', 0)
MAX_TICKS = 40

HUE_DEVICE_NAMES = frozenset([
    'Hue Lamp',
    'Hue ambiance lamp',
])

def discover(ble, config):
    unbuffered.write(b'Discovering')
    ble.clear_cached_data()

    # Get the first available BLE network adapter and make sure it's powered on.
    adapter = ble.get_default_adapter()
    adapter.power_on()
    adapter.start_scan()

    for _ in range(MAX_TICKS):
        unbuffered.write(b'.')
        time.sleep(.5)
        lights = [dev for dev in ble.find_devices() if dev.name in HUE_DEVICE_NAMES]
        if len(lights) == len(config):
            break

    if len(lights) == 0:
        raise SystemExit

    new_lights = 0
    names = dict()

    print('found %d lights:' % len(lights))
    for light in lights:
        if light.id in config:
            name = config[light.id]
        else:
            new_lights += 1
            name = "new_%d" % new_lights

        names[name] = light
        print("%s (%s %s)" % (name, light.name, light.id))
        light.connect()

    time.sleep(.5)
    return names
