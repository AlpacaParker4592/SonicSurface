INTERNAL_INTERVAL = 2.5  # (unit: cm)
EXTERNAL_INTERVAL = 3.5  # (unit: cm)

def convertStringtoBraille(string):
    pass


def convertBrailleToPositions(brailles: list) -> dict:
    """Convert braille text to tactile positions

    Parameters
    ----------
    brailles : list
        braille text to convert (e.g. ["⠿", "⠍", "⠎"])

    Returns
    -------
    positions_by_braille : dict
        tactile positions by braille text
        e.g. {
                0 : [[x01, z01], [x02, z02], ...]  <- ⠿
                1 : [[x11, z11], [x12, z12], ...]  <- ⠍
                ...
             }
    """
    braille_table = "⠀⠁⠂⠃⠄⠅⠆⠇⠈⠉⠊⠋⠌⠍⠎⠏⠐⠑⠒⠓⠔⠕⠖⠗⠘⠙⠚⠛⠜⠝⠞⠟⠠⠡⠢⠣⠤⠥⠦⠧⠨⠩⠪⠫⠬⠭⠮⠯⠰⠱⠲⠳⠴⠵⠶⠷⠸⠹⠺⠻⠼⠽⠾⠿"  # 0 ~ 2^6-1(=63)
    position_template = [[0,-INTERNAL_INTERVAL],
                         [0,0],
                         [0,INTERNAL_INTERVAL],
                         [INTERNAL_INTERVAL,-INTERNAL_INTERVAL],
                         [INTERNAL_INTERVAL,0],
                         [INTERNAL_INTERVAL,INTERNAL_INTERVAL]
                        ]  # [[x1, z1], [x2, z2], ...] (0 <= xn, zn <= 16, unit: cm)
    positions_by_braille = {}
    pos = 0
    for braille in brailles:
        idx = braille_table.find(braille) if braille_table.find(braille) != -1 else 0
        position_by_braille = []

        for n in range(5,-1,-1):
            if idx >= 2 ** n: position_by_braille.insert(0, position_template[n])
            idx = idx - 2 ** n if idx >= 2**n else idx
        positions_by_braille[pos] = position_by_braille
        pos += 1
    return positions_by_braille


def determineIndices(brailles:str,start_idx:int) -> tuple[int, int]:
    MAXIMUM_LENGTH_FOR_ARRAY = 3  # maximum length of string to implement into the tactile array
    start_idx = start_idx if start_idx >= 0 else 0
    start_idx = min(len(brailles)-MAXIMUM_LENGTH_FOR_ARRAY,start_idx)
    end_idx = min(len(brailles),start_idx+MAXIMUM_LENGTH_FOR_ARRAY)
    return start_idx,end_idx


def printPosition(brailles:list,start_idx:int,end_idx:int) -> None:
    braille_table = "⠀⠁⠂⠃⠄⠅⠆⠇⠈⠉⠊⠋⠌⠍⠎⠏⠐⠑⠒⠓⠔⠕⠖⠗⠘⠙⠚⠛⠜⠝⠞⠟⠠⠡⠢⠣⠤⠥⠦⠧⠨⠩⠪⠫⠬⠭⠮⠯⠰⠱⠲⠳⠴⠵⠶⠷⠸⠹⠺⠻⠼⠽⠾⠿"  # 0 ~ 2^6-1(=63)
    print_list = [[],  # 1st list
                  [],  # 2nd list
                  []   # 3rd list
                 ]

    brailles_print = brailles[start_idx:end_idx]
    for braille in reversed(brailles_print):
        idx = braille_table.find(braille) if braille_table.find(braille) != -1 else 0
        for i in range(len(print_list)): print_list[i].insert(0, " "*4)
        for n in range(5,-1,-1):
            mark = "●" if idx >= 2**n else "X"
            idx = idx - 2 ** n if idx >= 2**n else idx
            print_list[n % 3].insert(0,mark+" "*3)
    
    for p in print_list: print("\n"+"".join(p))
    return None


def slicePosition(brailles: list,initial_start_idx:int) -> list:
    # TODO: convertBrailleToPositions 함수를 통해 만들어진 점자별 리스트 -> 1차원 상으로 펼치기(+EXTERNAL_INTERVAL 더해서)
    """Slice the position variable by braille text into the list for tactile array. 

    Parameters
    ----------
    brailles : list
        braille text to convert (e.g. ["⠿", "⠍", "⠎"])
    start_idx : int
        beginning index to slice

    Returns
    -------
    positions: list
        (Sliced) position list to use a tactile array
        e.g. [[x1, z1], [x2, z2], ...]
    """

    positions_by_braille = convertBrailleToPositions(brailles)
    start_idx,end_idx = determineIndices(brailles,initial_start_idx)

    positions = []
    for i in range(start_idx,end_idx):
        n = i - start_idx
        for position in positions_by_braille[i]:
            adjusted_position = [position[0] + n * (EXTERNAL_INTERVAL + INTERNAL_INTERVAL),
                                 position[1]]
            positions.append(adjusted_position)
    return positions


if __name__ == "__main__":
    import time
    import keyboard

    brailles = list("⠿⠍⠝⠞⠟⠠⠎")
    positions_by_braille = convertBrailleToPositions(brailles)
    for i in range(len(positions_by_braille)):
        print("{0} : {1}".format(brailles[i], positions_by_braille[i]))
    print("")

    start_idx=0

    start_idx,end_idx = determineIndices(brailles,start_idx)
    print("Braille to Implement: {}".format(brailles[start_idx:end_idx]))
    print("Return: {}".format(slicePosition(brailles,start_idx)))
    printPosition(brailles,start_idx,end_idx)

    while True:
        try:
            is_right_pressed = keyboard.is_pressed('right') or keyboard.is_pressed('d')
            is_left_pressed = keyboard.is_pressed('left') or keyboard.is_pressed('a')
            if is_right_pressed or is_left_pressed:
                direction = 1 if is_right_pressed else -1
                start_idx += direction
                start_idx, end_idx = determineIndices(brailles,start_idx)

                print("\n\nStart Index: {0}, End Index: {1}".format(start_idx, end_idx))
                printPosition(brailles,start_idx,end_idx)
                time.sleep(0.1)
            
        except KeyboardInterrupt: 
            break
    print("Disconnect")