import random

words = ["keyword", "computer", "programming", "security", "python"]

word = random.choice(words)
guessed_word = ["_"] * len(word)
attempts = 6

print("Welcome to Hangman!")
print("Word:", " ".join(guessed_word))

while attempts > 0 and "_" in guessed_word:
    guess = input("Enter a letter: ").lower()

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed_word[i] = guess
        print("Correct:", " ".join(guessed_word))
    else:
        attempts -= 1
        print(f"Wrong guess! Attempts left: {attempts}")

if "_" not in guessed_word:
    print("🎉 You Win! The word was:", word)
else:
    print("❌ Game Over! The word was:", word)
