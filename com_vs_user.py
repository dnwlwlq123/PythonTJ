import random

choice_game = ['가위', '바위', '보']
score = {
    "player": 0,
    "com": 0
}
count = 0
while count < 3:
    print('컴퓨터와 가위바위보 게임입니다')
    player_choice = input("가위 바위 보 중 하나 입력 : ")
   
    if player_choice not in choice_game:
        print("잘못된 입력입니다. 가위, 바위, 보 중 하나를 입력해주세요.")
        continue
   
    com_choice = random.choice(choice_game)
    print(f"컴퓨터: {com_choice}")
   
    if player_choice == com_choice:
        print("무승부입니다!")
    elif ((player_choice == "가위" and com_choice == "보") or
         (player_choice == "바위" and com_choice == "가위") or
         (player_choice == "보" and com_choice == "바위")):
        print("당신 승")
        score["player"] += 1
    else:
        print("컴퓨터 승")
        score["com"] += 1
    count += 1
    print()
print(f"당신: {score['player']},vs 컴퓨터: {score['com']}")
if score["player"] > score["com"]:
    print("당신의 승리입니다!")
elif score["player"] < score["com"]:
    print("컴퓨터의 승리입니다!")
else:
    print("무승부입니다!")