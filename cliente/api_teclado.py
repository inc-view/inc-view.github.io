import win32api
import time
import os

historico = []
keyState = []
keyCount = 0
mouseCount = 0
count = 0
keyboard = []
interval = 3000
now = time.time()
for k, key in enumerate(win32api.GetKeyboardState()):
    keyState.append(0)
    keyboard.append(k)

while True:
    for k, key in enumerate(keyboard):
        curState = win32api.GetKeyState(key)
        if keyState[k] in (0, 1) and curState in (-127, -128):
            keyState[k] = curState
            if k <= 2:
                mouseCount += 1
            else:
                keyCount += 1
        elif keyState[k] in (-127, -128) and curState in (0, 1):
            keyState[k] = curState

    count += 1

    if count >= interval:
        historico.append((mouseCount, keyCount))
        keyCount = 0
        mouseCount = 0
        count = 0
        os.system('cls')
        print(historico)
        print(time.time() - now, "s")
        now = time.time()
    
    #time.sleep(0.001)