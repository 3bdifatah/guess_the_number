import random

correct = 'you guessed correctly!'
too_low = 'Too Low'
too_high = 'too high'

def configure_range():
    """ Set the high and low values for the random number """
    return 1, 10


def generate_secret(low, high):
    """ Generate a secret number for the user to guess """
    return random.randint(low, high)


def get_guess():
    """ get user's guess, as an integer number """
    return int(input('Guess the secret number? '))


def check_guess(guess, secret):
    """ compare guess and secret, return string describing result of comparison """
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():

    guess_count = 0

    (low, high) = configure_range()
    secret = generate_secret(low, high)


    try:
        while True:
            guess = get_guess()
            result = check_guess(guess, secret)
            print(result)

            guess_count += 1
            
            if result == correct:
                break

        print(f'Thanks for playing the game! You won in {str(guess_count)} guesses.')
    except ValueError as e:
        print("Error, please enter integer between 1-10 and restart the program")



if __name__ == '__main__':
    main()
