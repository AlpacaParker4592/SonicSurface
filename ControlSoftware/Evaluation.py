from Python.SonicSurface import SonicSurface
import random
import time
import numpy as np
import Brailles
import keyboard



DIST = 0.1 #focus at 0.1 meter
#put 0.12 to focus at 12cm and feel the focal point with your hand

MOD_FREQ = 250
TIME_PER_POS = 0.1

WAIT_SWITCH = 1.0 / MOD_FREQ / 2
N_SWITCHES = int(TIME_PER_POS / WAIT_SWITCH)

STEERING_SPEED = (15 * 2 *np.pi) / WAIT_SWITCH  # 15Hz * 2pi / WAIT_SWITCH(waiting time)

direction = 1  # 1 for text order increasing, -1 for decreasing
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
    
def sendOnePoint(array, position, useIBP=True):
    points = np.zeros([1, 3])
    points[0,0] = (position[0] - 8) * 0.01  # x
    points[0,1] = position[1]  # y
    points[0,2] = (position[2]) * 0.01  # z
    #print(points)
    
    if useIBP: array.multiFocusIBP(points)
    else: array.multiFocusChecker(points)


def question(brailles):
    start_time = time.time()
    idx = 0
    positionsByBraille = Brailles.slicePosition(brailles,0)
    positionsToFocus = [[pos[0] * 0.01,DIST,pos[1] * 0.01] for pos in positionsByBraille]  #[[x1,y1,z1], ... ]

    #positionsToFocus = [positionsToFocus[3]]
    print("\nBraille Table")
    sampleBrailles = list("⠀⠁⠂⠃⠄⠅⠆⠇⠈⠉⠊⠋⠌⠍⠎⠏⠐⠑⠒⠓⠔⠕⠖⠗⠘⠙⠚⠛⠜⠝⠞⠟⠠⠡⠢⠣⠤⠥⠦⠧⠨⠩⠪⠫⠬⠭⠮⠯⠰⠱⠲⠳⠴⠵⠶⠷⠸⠹⠺⠻⠼⠽⠾⠿")
    for i in range(len(sampleBrailles)):
        print("{0:2d}: {1}".format(i, sampleBrailles[i]), end="  ")
        if i != 0 and i % 16 == 15: print("")
    print("=============")
    
    print("Please press ESC button when you figure out.")
    
    while True:
        positionsToFocus = [[pos[0],DIST,pos[2]] for pos in positionsToFocus]  #[[x1,y1,z1], ... ]
        is_enter_pressed = False
        
        angle = 0
        while not is_enter_pressed:
            if keyboard.is_pressed('esc'):
                is_enter_pressed = True
                break
            
            x = positionsToFocus[idx][0]
            y = positionsToFocus[idx][1]
            z = positionsToFocus[idx][2] + 0.005 * np.sin(angle)
            #print(x, y, z)
            array.focusAtPos(x,y,z)
            array.switchOnOrOff(False)

            for _ in range(N_SWITCHES): #swap quickly between the last two send phases (focus and off) that creates modulation
                array.sendCommit()
                #time.sleep(WAIT_SWITCH)
                active_wait(WAIT_SWITCH)

            idx = (idx+1) % len(positionsToFocus)
            if idx == 0: angle += STEERING_SPEED
        
        time.sleep(0.1)
        array.switchOnOrOff(False)
        input_answer = input("Write 3 answers by number (i.e. 23 34 40).\nPlease just press enter if you did not figure out: ")

        if input_answer == "":
            array.switchOnOrOff(True)
            is_enter_pressed = False
            continue
        
        answer = list(map(int,input_answer.split()))
        while len(answer) < 3: answer.append(-1)
        if len(answer) > 3: answer = answer[:3]
        break

    end_time = time.time()
    elapsed_time = end_time - start_time  # 단위: 초
    return answer, elapsed_time


if __name__ == "__main__":
    array = SonicSurface()
    array.connect( -1 )
    data = []  # [정답, 사용자 제공 답안, 걸린 시간] 별 리스트

    print("Tutorial")
    print("This brailles means ⠿ ⠿ ⠿.\nFeel the haptic sensation and input the number of braille type.\n")
    question(list("⠿⠿⠿"))


    sampleBrailles = list("⠀⠁⠂⠃⠄⠅⠆⠇⠈⠉⠊⠋⠌⠍⠎⠏⠐⠑⠒⠓⠔⠕⠖⠗⠘⠙⠚⠛⠜⠝⠞⠟⠠⠡⠢⠣⠤⠥⠦⠧⠨⠩⠪⠫⠬⠭⠮⠯⠰⠱⠲⠳⠴⠵⠶⠷⠸⠹⠺⠻⠼⠽⠾⠿")
    braillesIdx = [i for i in range(len(sampleBrailles))]
    random.shuffle(braillesIdx)

    print("\nBraille Table")
    for i in range(len(sampleBrailles)):
        print("{0:2d}: {1}".format(i, sampleBrailles[i]), end="  ")
        if i != 0 and i % 16 == 15: print("")
    print("=============")

    for i in range(0, len(sampleBrailles), 3):
        print("\nProblem {0}-{1}.".format(i+1, min(i+3,len(braillesIdx))))
        braillesForQuestion = [sampleBrailles[i] for i in braillesIdx[i:min(i+3,len(braillesIdx))]]
        answer, elapsed_time = question(braillesForQuestion)
        right_answer = braillesIdx[i:min(i+3,len(braillesIdx))]
        data.append([right_answer,answer,elapsed_time])

    total = 0
    correct = 0
    for d in data:
        right_answer, your_answer = d[0], d[1]
        for i in range(len(right_answer)):  #answer 개수
            total += 1
            if right_answer[i] == your_answer[i]:
                correct += 1

    print("\n=============")
    print("\nRESULT")
    print("\n=============\n")
    
    print("total: {0}, correct: {1}".format(total, correct))
    print("Rate: {} %".format(correct/total*100))
    print("================")
    print("Elapsed time:")
    for d in data:
        print("{}s".format(round(d[2],4)), end="  ")
        print("")
    print("Agerage Time: {}s".format(round(sum([d[2] for d in data])/len(data),4)))