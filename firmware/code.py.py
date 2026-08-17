import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

BUTTON_PINS = {
    board.D1: Keycode.W,
    board.D2: Keycode.A,
    board.D3: Keycode.S,
    board.D4: Keycode.D,
    board.D0: Keycode.SPACE,
}

switches = []
for pin, key in BUTTON_PINS.items():
    sw = digitalio.DigitalInOut(pin)
    sw.direction = digitalio.Direction.INPUT
    sw.pull = digitalio.Pull.UP
    switches.append((sw, key))

last_states = [True] * len(switches)

while True:
    for idx, (sw, key) in enumerate(switches):
        current_state = sw.value
        
        if current_state != last_states[idx]:
            if not current_state:
                kbd.press(key)
            else:
                kbd.release(key)
            last_states[idx] = current_state