#!/usr/bin/env python3

import sys
import subprocess
from time import sleep
import pifacecad
import pifacecad.tools
from pifacecad.lcd import LCD_WIDTH

if __name__ == "__main__":
  cad = pifacecad.PiFaceCAD()
  lcd = cad.lcd
  lcd.backlight_on()
  lcd.blink_off()

  if "clear" in sys.argv:
    lcd.clear()
    lcd.display_off()
    lcd.backlight_off()
    lcd.cursor_off()
  else:
    lcd.write("Reflex Testing\nTime!")
    sleep(1)
    while True:
      scanner = pifacecad.tools.LCDScanf("Text: %c%2i%.%r")
      print(scanner.scan())
