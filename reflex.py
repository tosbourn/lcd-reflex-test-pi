#!/usr/bin/env python3

import sys
import subprocess
from time import sleep
import pifacecad

if __name__ == "__main__":
  cad = pifacecad.PiFaceCAD()

  if "clear" in sys.argv:
    cad.lcd.clear()
    cad.lcd.display_off()
    cad.lcd.backlight_off()
  else:
    cad.lcd.write("Reflex Testing Time Press any button to continue")
