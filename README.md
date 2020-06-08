# philble
Python 3 library to control Philips Hue lights over Bluetooth Low Energy (BLE). Uses
the [`Adafruit_BluefruitLE`](https://github.com/adafruit/Adafruit_Python_BluefruitLE) library to issue Bluetooth commands.

* Works on Linux and macOS (tested on 10.14)
* Install: `pip install .`
* Minimal working example: See [**`example.py`**](https://github.com/npaun/philble/blob/master/example.py)
* If things go wrong: [HOWTO: Factory reset a Hue bulb](https://github.com/mozilla-iot/wiki/wiki/HOWTO:-Factory-reset-a-Hue-bulb) by Mozilla IOT.

<img src="https://github.com/npaun/philble/blob/master/docs/blinkenlights.gif?raw=true" alt="Demo of philble controlling lights" title="Cooooooolooooors" width="300" />

## API
See `philble/client.py` for commands available and mapping on to the BLE interface.

```python
import philble.clint
client = philble.client.Client(device)
```

* `power(False | True)`
* `brightness(1..254)`
* `temperature(153...454)`: Color temperature *decreases* as index increases, for some reason.
* `color(hex string)`

## lightcom
A small demo, providing an `IPython` REPL for controlling light fixtures. Modify
`config.py` to provide names for your lights. The light client objects are available
in a global variable called `l`.

<img src="https://github.com/npaun/philble/blob/master/docs/lightcom-screenshot.png?raw=true" alt="Example lightcom session" title="The lightbulb REPL of the future" width="750" />


## TODO:
* [ ] Figure out which sleeps are due to BLE library oddness and which are due to my sloppy implementation.
* [ ] Read current values for these parameters.
* [ ] Fully understand color code.
* [ ] Provide HSL input for colors - probably easier to reason about for lighting.
* [ ] Save state after lamp power-cycle.
* [ ] Create demo to activate lamps relative to sunrise/sunset.

## Resources consulted
* <https://gist.github.com/shinyquagsire23/f7907fdf6b470200702e75a30135caf3>
* <https://www.reddit.com/r/Hue/comments/eq0y3y/philips_hue_bluetooth_developer_documentation/>
