import Hangman_creator

hangman = Hangman_creator.Hangman(
    "E:\\Sumit\\Programs\\Python\\Udemy_Python\\Hangman Game\\wordlist.txt")
hangman.choose_the_word()
hangman.fill_the_word_status()
while True:
    hangman.get_word_status()
    hangman.guess_the_letter()

    if (hangman.Life == 0):
        print("😭 Game Over\nThe Word was '{}' ".format(
            hangman.chosen_word))
        break
    elif (hangman.chosen_word == ''.join(hangman.word_status)):
        print("'{}'\n🎉🎉 Hurray! You Guessed the word.".format(
            hangman.chosen_word))
        break
