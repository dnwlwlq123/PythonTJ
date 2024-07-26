builder = 0

def building_fun():
    global builder
    while True:
        user_now = int(input("현재 층수 입력 (1~6): "))
        user_input = int(input("가고자 하는 층 입력 (1~6): "))
        
        if user_now < 1 or user_now > 6 or user_input < 1 or user_input > 6:
            print("유효하지 않은 층입니다. 1~6 사이의 층을 입력해주세요.")
            continue
        
        builder = user_now
        target_floor = user_input

        if builder == target_floor:
            print(f"이미 {builder}층에 있습니다.")
            continue
        
        if builder < target_floor:
            for floor in range(builder + 1, target_floor + 1):
                builder = floor
                print(f"올라가는중 {builder}층입니다")
        else:
            for floor in range(builder - 1, target_floor - 1, -1):
                builder = floor
                print(f"내려가는중 {builder}층입니다")

        print(f"{builder}층에 도착했습니다 안녕히가삼.")
        continue

building_fun()
