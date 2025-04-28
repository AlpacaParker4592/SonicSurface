from Python.SonicSurface import SonicSurface
import time
import numpy as np
import Brailles
import keyboard

array = SonicSurface()
array.connect( -1 )

DIST = 0.1 #focus at 0.1 meter
#put 0.12 to focus at 12cm and feel the focal point with your hand

MOD_FREQ = 250
TIME_PER_POS = 0.1

WAIT_SWITCH = 1.0 / MOD_FREQ / 2
N_SWITCHES = int(TIME_PER_POS / WAIT_SWITCH)

STEERING_SPEED = 0.5 * (np.pi/180) 

direction = 1  # 1 for increasing, -1 for decreasing
angle = 0

def active_wait(seconds):
    start = time.perf_counter()  # Get the precise start time
    while time.perf_counter() - start < seconds: pass  # Busy-wait loop (uses CPU but is accurate)

def sendPoints(array, positions, distance, useIBP=True):
    nPoints = len([pos for pos in positions if pos[0] != -1])
    points = np.zeros([nPoints, 3])
    index = 0
    for pos in positions:
        if pos[0] == -1: continue
        points[index,0] = (pos[0] - 8) * 0.01  # x
        points[index,1] = distance             # y
        points[index,2] = (pos[1]) * 0.01      # z
        index += 1
         
    if nPoints == 0: array.switchOnOrOff( False )
    elif nPoints == 1: array.focusAt(points[0])
    elif useIBP: array.multiFocusIBP(points)
    else: array.multiFocusChecker(points)
    
start_idx = 0
brailles = list("⠿⠍⠝⠞⠟⠠⠎")

try:
    while True:
        is_right_pressed = keyboard.is_pressed('right')
        is_left_pressed = keyboard.is_pressed('left')
        if is_right_pressed or is_left_pressed:
            direction = 1 if is_right_pressed else -1
            start_idx += direction
            start_idx, end_idx = Brailles.determineIndices(brailles,start_idx)

            print("Start Index: {0}, End Index: {1}".format(start_idx, end_idx))
            Brailles.printPosition(brailles,start_idx,end_idx)
            time.sleep(0.1)
        
        positions = Brailles.slicePosition(brailles,start_idx)
        positions = [[0.005*np.sin(angle)+pos[0],pos[1]] for pos in positions]
        sendPoints(array, positions, DIST, True)

        array.switchOnOrOff(False)
        
        angle += direction * STEERING_SPEED



        for _ in range(N_SWITCHES): #swap quickly between the last two send phases (focus and off) that creates modulation
            array.sendCommit()
            #time.sleep(WAIT_SWITCH)
            active_wait(WAIT_SWITCH)
            
except KeyboardInterrupt: array.disconnect()