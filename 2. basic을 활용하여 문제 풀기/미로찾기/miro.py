# 미로찾기 게임 정답
# 미로를 찾는 방법은 좌수법으로 혹은 우수법으로 한쪽 벽면을 따라서 찾는 방법이다.
# 해당 정답은 오른손을 두고 가는 방법이다.
# step 1 오른쪽이 비어 있다면 오른쪽으로 돌아라
# step 2 앞이 비어 있다면 앞으로 가라
# step 3 앞이 막혀 있다면 왼쪽으로 돌아라
# step 4 최초에 시작할때 벽을 오른손으로 잡게 만들어라


def turn_right():
    turn_left()
    turn_left()
    turn_left()


while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
