import Adafruit_BluefruitLE
import time
from . import client, discover
from IPython import embed
import config
from types import SimpleNamespace

ble = Adafruit_BluefruitLE.get_provider()
ble.initialize()

def main():
    lights = discover.discover(ble, config.lights)

    clients_dict = {light_id: client.Client(light) for light_id, light in lights.items()}
    clients = SimpleNamespace(**clients_dict)

    print('\033[0;35mLIGHT COMMANDER\033[0m')
    print('\033[1mLights (l) = \033[0m', ", ".join('.%s' % key for key in clients_dict.keys()))
    embed(user_ns={'l': clients}, colors='Neutral')
    # Ensure last command gets written
    time.sleep(.5) 

ble.run_mainloop_with(main)

