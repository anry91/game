from os import system
_ = 0
R = 1
M = 2
rc = 0

game_map = [R,_,_,_,_,_,M,_,_,_]

while True:
    system('cls')
    for c in game_map:
        if c == _:
            print("_", end=" ")
        elif c == R:
            print("R", end=" ")
        elif c == M:
            print("M", end=" ")
    print()
    print()

    if rc+1 <= 9 and game_map[rc+1] == M or rc-1 >= 0 and game_map[rc-1] == M:
        print("Warning: immediate danger")
    elif rc+2 <= 9 and game_map[rc+2] == M or rc-2 >= 0 and game_map[rc-2] == M:
        print("Warning: danger near")
    elif rc+3 <= 9 and game_map[rc+3] == M or rc-3 >= 0 and game_map[rc-3] == M:
        print("Warning: danger ahead")
    
    print(rc) #robot's index_place  now
    
    input()


    game_map[rc] = _
    rc += 1
    game_map[rc] =R
