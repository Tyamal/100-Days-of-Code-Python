print("Selamat datang di permainan Hangman!")
print(display_hangman(tries))
print(word_completion)
print("\n")

while not guessed and tries > 0:
    guess = input("Tebak huruf atau kata: ").lower()

    if len(guess) == 1 and guess.isalpha():
        if guess in guessed_letters:
            print("Anda sudah menebak huruf ini:", guess)
        elif guess not in word:
            print(guess, "bukan huruf yang benar.")
            tries -= 1
            guessed_letters.append(guess)
        else:
            print("Bagus! Huruf", guess, "ada dalam kata.")
            guessed_letters.append(guess)
            word_as_list = list(word_completion)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
                word_as_list[index] = guess
            word_completion = "".join(word_as_list)

            if "_" not in word_completion:
                guessed = True
    elif len(guess) == len(word) and guess.isalpha():
        if guess in guessed_words:
            print("Anda sudah menebak kata ini:", guess)
        elif guess != word:
            print(guess, "bukan kata yang benar.")
            tries -= 1
            guessed_words.append(guess)
        else:
            guessed = True
            word_completion = word
    else:
        print("Input tidak valid. Silakan coba lagi.")

    print(display_hangman(tries))
    print(word_completion)
    print("\n")

if guessed:
    print("Selamat! Anda berhasil menebak kata:", word)
else:
    print("Sayang sekali! Anda kehabisan percobaan. Kata yang benar adalah:", word)
