import random

words_list = ["pokemon", "digimon", "dragonball", "Monsterhunter", "Cardcapters"]
magic_word = random.choice(words_list).upper()
magic_word_list = list(magic_word)
magic_word_display = []
for i in range(len(magic_word)):
    magic_word_display.append("_")

print(magic_word)
print(magic_word_display)
print("Welcome to the game. \nThe theme is 90's television.")


def changer(inputt):
    if inputt not in magic_word_list:
        guess_count = 1
        return magic_word_display, guess_count
    for i in range(len(magic_word)):
        if magic_word[i] == inputt:
            magic_word_display[i] = inputt
            guess_count = 0
    return magic_word_display, guess_count

def full_guess(inputt):
    if inputt.upper() == magic_word:
        return magic_word_list


mistake_count = 0
max_guess = 6
polkadot = True
while polkadot is True:
    if magic_word_display != magic_word_list and mistake_count != max_guess:
        attempt = input("Guess a letter: ")
        attempts = attempt.upper()
        a, b = (changer(attempts))
        mistake_count += b
        c = full_guess(attempts)
        if c is not None:
            magic_word_display = c
            print(magic_word_list)
            print("\nHooray the man is not hung.")
            break
        print(a)
    elif magic_word_display == magic_word_list:
        polkadot = False
        print("\nHooray the man is not hung.")
    elif mistake_count == max_guess:
        polkadot = False
        print("\nYou hung the man. We all lose.")























