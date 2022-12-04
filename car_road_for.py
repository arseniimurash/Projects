from os import system


roadLen = 10
carY = 1
lane = 2

while True:

################## DRAWING THE MAP ##################
    system ('cls')
    print("🚧🚧🚧🚧🚧🚧🚧🚧")
    for y in range (roadLen,0,-1):
        carL = "  "
        carR = "  " 
        if y == carY:
            if lane == 1:
                carL = "🚗"
            if lane == 2:
                carR = "🚗"
        print(f"🌳 {carL}  ⬜  {carR} 🌳")
    print("🚧🚧🚧🚧🚧🚧🚧🚧")
################## DRAWING THE MAP ##################

################## USER INTERACTION #################
    move = input("move(w,s): ")
    if move == "w":
        carY += 1
        if carY > 10:
            if lane == 2:
                lane = 1
            elif lane == 1:
                lane = 2
            carY -= 1
    if move == "s":
        carY -= 1
        if carY < 1:
            if lane == 2:
                lane = 1
            elif lane == 1:
                lane = 2
            carY += 1
################## USER INTERACTION #################



