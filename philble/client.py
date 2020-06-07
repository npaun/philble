from enum import Enum
import uuid
import functools
import struct
import time


class CharacteristicWrap:
    def __init__(self, charac):
        self.charac = charac

    def read_value(self):
        return self.charac.read_value(timeout_sec=5)

    def write_value(self, value):
        return self.charac.write_value(bytes(value))


def command(code):
    def decorator(f):
        cmd_uuid = uuid.UUID('932c32bd-'+ str(code).zfill(4) + '-47a2-835a-a8d455b859dd')
        @functools.wraps(f)
        def wrapper(self, *args, **kwargs):
            return f(CharacteristicWrap(self.service.find_characteristic(cmd_uuid)), *args, **kwargs)
        wrapper.uuid = cmd_uuid
        return wrapper
    return decorator


class Client:
    uuid = uuid.UUID('932c32bd-'+ '0000' + '-47a2-835a-a8d455b859dd')

    def __init__(self, device):
        self.device = device
        #settle()
        self.service = self.device.find_service(Client.uuid)

    @command(1)
    def unknown1(raw):
        pass

    @command(2)
    def power(raw, on):
        raw.write_value([0x1 if on else 0x0])

    @command(3)
    def brightness(raw, level):
        if not 1 <= level <= 254:
            print('WARNING: Brightness may be out of range')

        raw.write_value([level])

    @command(4)
    def temperature(raw, temp_index):
        """
        Sets color temperature to temp. Index ranges from 153 (bluest), 
        to 454 (bluest), or 500 on some models.
        """
        if not 153 <= temp_index <= 454:
            print('WARNING: Temperature may be out of range')

        raw.write_value(struct.pack('h', temp_index))


    @command(5)
    def color(raw, hexstr):
        """
        Sets color by converting RGB colors to an internal color code using a formula
        of dubious accuracy:
        min(1, round(color[i]/sum(color)*255))
        """
        def convert(rgb):
            if not all([0 <= chan <= 255 for chan in rgb]):
                raise ValueError('We cannot understand this color code')

            scale = 0xff
            adjusted = [max(1, chan) for chan in rgb]
            total = sum(adjusted)
            adjusted = [int(round(chan/total * scale)) for chan in adjusted]
            if sum(adjusted) > scale:
                # Badddddd
                print('ooooooh')

            return [0x1, adjusted[0], adjusted[2], adjusted[1]]
        
        if len(hexstr) == 7:
            hexstr = hexstr[1:]

        color_bits =  [int(bit,16) for bit in [hexstr[:2], hexstr[2:4], hexstr[4:]]]
        raw.write_value(convert(color_bits))


    @command(6)
    def unknown6(raw):
        pass

    @command(7)
    def maybe_state(raw):
        pass

    @command(1003)
    def unknown1003(raw):
        pass

    @command(1005)
    def maybe_saved_state(raw):
        pass

    def __del__(self):
        pass
        #settle()
