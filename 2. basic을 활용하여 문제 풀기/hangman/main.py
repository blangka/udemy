import random
from hangman_art import stages, logo
from hangman_words import word_list
import os


def clear():  # 화면 지우기
    os.system("clear")


# logo가 보이도록
print(logo)
game_is_finished = False
lives = len(stages) - 1  # stage 의 길이 만큼 목숨이 줄어 들게 한다.

# ToDo-1: Random으로 word_list에서 하나의 단어를 선택하고 chosen_word에 저장합니다.
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []

# ToDo-2: 단어의 크기 만큼 blank를 생성
for _ in range(word_length):
    display += "_"

# 종료 될때 까지 무한 반복 시킨다.
while not game_is_finished:
    # ToDo-3: 사용자에게 입력을 받고 guess에 저장합니다. 단어에 있는지 없는지를 체크함다.
    guess = input("Guess a letter: ").lower()

    # 화면을 지워서 초기화 시킨다.
    clear()

    # 사용자가 입력한 문자가 단어에 있는지 확인한다.
    if guess in display:
        print(f"You've already guessed {guess}")

    # 사용자가 입력한 문자가 단어에 없다면
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    # 사용자가 입력한 문자가 단어에 없다면
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You lose.")

    # 여전히 blank가 남아 있지 않다면
    if not "_" in display:
        game_is_finished = True
        print("You win.")

    print(stages[lives])
