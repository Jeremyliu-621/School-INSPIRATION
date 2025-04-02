"""

Switch inspired from instagram reels. Infinite loop.

switch2.py recursive switch
Jeremy Liu
2/23/2025

"""

import time

def main():
    switch(17)

def switch(ammo):
    if ammo >= 0:
        time.sleep(0.1)
        print(f"Ammo:{ammo}")
        print("POP")
        return switch(ammo - 1)
    else:
        print("RELOADING...")
        time.sleep(1)
        return switch(17)
    
main()
