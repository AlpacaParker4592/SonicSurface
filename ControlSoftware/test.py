import time, keyboard, random

def question(brailles):
    start_time = time.time()
    print("Write 3 answers by number (i.e. 34 23 40).\nPlease just press enter if you did not figure out: ")
    while True:
        if keyboard.is_pressed('enter'):
            time.sleep(0.1)
            input_answer = input("Write 3 answers by number (i.e. 34 23 40).\nPlease just press enter if you did not figure out: ")
            print(input_answer)
            if input_answer == "":
                print("Tried the test one more")
                continue

            answer = list(map(int,input_answer.split()))[:3]
            break

        continue

    end_time = time.time()
    elapsed_time = end_time - start_time  # 단위: 초
    return answer, elapsed_time


if __name__ == "__main__":
    data = []  # [정답, 사용자 제공 답안, 걸린 시간] 별 리스트

    sampleBrailles = list("⠀⠁⠂⠃⠄⠅⠆⠇⠈⠉⠊⠋⠌⠍⠎⠏⠐⠑⠒⠓⠔⠕⠖⠗⠘⠙⠚⠛⠜⠝⠞⠟⠠⠡⠢⠣⠤⠥⠦⠧⠨⠩⠪⠫⠬⠭⠮⠯⠰⠱⠲⠳⠴⠵⠶⠷⠸⠹⠺⠻⠼⠽⠾⠿")
    braillesIdx = [i for i in range(len(sampleBrailles))]
    random.shuffle(braillesIdx)
    
    print("Braille Table")
    for i in range(len(sampleBrailles)):
        print("{0:2d}: {1}".format(i, sampleBrailles[i]), end="  ")
        if i != 0 and i % 8 == 7: print("")
    print("===============")

    for i in range(0, len(sampleBrailles), 3):
        print("Problem {0}-{1}.".format(i+1, min(i+3,len(braillesIdx))))
        braillesForQuestion = [sampleBrailles[i] for i in braillesIdx[i:min(i+3,len(braillesIdx))]]
        answer, elapsed_time = question(braillesForQuestion)
        right_answer = braillesIdx[i:min(i+3,len(braillesIdx))]
        data.append([right_answer,answer,elapsed_time])

    total = 0
    correct = 0
    for d in data:
        right_answer, your_answer = d[0], d[1]
        print(right_answer, your_answer)
        for i in range(len(right_answer)):  #answer 개수
            total += 1
            if right_answer[i] == your_answer[i]:
                correct += 1

    print("\n=============")
    print("\nRESULT\n")
    print("\n=============\n")
    
    print("total: {0}, correct: {1}".format(total, correct))
    print("Rate: {} %".format(correct/total*100))
    print("================")
    print("Elapsed time:")
    for d in data:
        print("{}s".format(round(d[2],4)), end="  ")
    print("Agerage Time: {}s".format(round(sum([d[2] for d in data]/len(data)),4)))
    print("Agerage Time: {}s".format(round(sum([d[2] for d in data]/len(data)),4)))