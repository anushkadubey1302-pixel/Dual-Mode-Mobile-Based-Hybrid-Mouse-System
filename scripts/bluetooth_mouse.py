import asyncio
from bleak import BleakScanner, BleakClient
import pyautogui

pyautogui.FAILSAFE = False

TARGET_NAME = "HYBRID_MOUSE"

def process_command(cmd):
    print("CMD:", cmd)

    try:
        if cmd.startswith("MOVE"):
            _, values = cmd.split(":")
            x, y = values.split(",")
            pyautogui.moveRel(int(x), int(y), duration=0)

        elif cmd == "LEFT":
            pyautogui.click()

        elif cmd == "RIGHT":
            pyautogui.rightClick()

        elif cmd == "DOUBLE":
            pyautogui.doubleClick()

        elif cmd == "DOWN":
            pyautogui.mouseDown()

        elif cmd == "UP":
            pyautogui.mouseUp()

        elif cmd == "SCROLL_UP":
            pyautogui.scroll(20)

        elif cmd == "SCROLL_DOWN":
            pyautogui.scroll(-20)

    except Exception as e:
        print("Error:", e)

async def main():
    print("Scanning for phone...")

    while True:
        devices = await BleakScanner.discover()

        target = None
        for d in devices:
            if d.name == TARGET_NAME:
                target = d
                break

        if target:
            print("Found phone:", target.name)

            async with BleakClient(target.address) as client:
                print("Connected!")

                while True:
                    await asyncio.sleep(1)

        else:
            print("Waiting for phone...")
            await asyncio.sleep(2)

asyncio.run(main())