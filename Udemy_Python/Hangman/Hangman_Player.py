import Hangman_creator

hangman = Hangman_creator.Hangman("E:\\wordlist.txt")
hangman.choose_the_word()
hangman.fill_the_word_status()
while True:
    hangman.get_word_status()
    hangman.guess_the_letter()

    if (hangman.attempts_remaining == 0):
        print("😭 Out Of Attempts.\nGame Over\nThe Word was '{}' ".format(
            hangman.chosen_word))
        break
    elif (hangman.chosen_word == ''.join(hangman.word_status)):
        print("{}\n🎉🎉 Hurray! You Guessed the word.".format(hangman.chosen_word))
        break
