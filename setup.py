from setuptools import setup

setup(name='philble',
      version='0.1',
      description='Philips Hue Bluetooth Low Energy (BLE) light client',
      url='http://github.com/npaun/philble',
      author='Nicholas Paun',
      packages=['philble'],
      install_requires=[
          # Version from pip doesn't work on macOS Mojave
          # Adafruit version doesn't work on modern Linux
          'Adafruit_BluefruitLE @ git+https://github.com/donatieng/Adafruit_Python_BluefruitLE'
          ],
      zip_safe=False)
