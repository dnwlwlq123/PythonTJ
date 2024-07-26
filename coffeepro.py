coffee_price = 300
coffee_amount = 10

def coffee_fun():
    global coffe_price
    global coffee_amount
    while coffee_amount > 0 :
        user_input = int(input("돈을 넣어주세요 : "))

        if user_input < coffee_price:
            print("돈이 부족합니다. 다시 시도해주세요.")
            continue

        coffee_amount -= 1
        change = user_input - coffee_price
        print(f"커피를 드립니다. 잔돈은 {change}원입니다.")
        print(f"남은 커피 수량: {coffee_amount}개")

    print("커피가 다 떨어졌습니다.")
coffee_fun()