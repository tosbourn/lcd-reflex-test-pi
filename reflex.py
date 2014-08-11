#!/usr/bin/env python3

import sys
import subprocess
from time import sleep
import pifacecad

if __name__ == "__main__":
  cad = pifacecad.PiFaceCAD()
  lcd = cad.lcd
  lcd.backlight_on()
  lcd.blink_off()

  if "clear" in sys.argv:
    lcd.clear()
    lcd.display_off()
    lcd.backlight_off()
  else:
    lcd.write("Reflex Testing\nTime!")
