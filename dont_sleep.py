import time as t
import pyautogui as pag
if __name__ == "__main__":
	it, two_min = 0, 2 * 60
	pag.FAILSAFE = False
	print(f"[dont_sleep] - started!")
	while True:
		it += 1
		hours = (it * two_min)//60
		for i in range((two_min )//5):
			t.sleep(1)
			print(f"\r > sleeping for: {i * 1}", end="")
		print(f"\n[{it}] - tot: {hours}min; {hours//60}hours\n > waited: { two_min}s")
		pag.hotkey("Esc")
		pag.hotkey("Esc")
