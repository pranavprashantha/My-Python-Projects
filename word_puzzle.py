'''
1. Create a function named get_valid_letters that takes in as an argument one string representing
	a puzzle and returns one string of ten (10) unique letters found in the puzzle. For the example
	puzzle above, your function should return the string RUEAMOSIKT
2. Create a function named is_valid_guess that takes in as arguments two strings and returns a
	Boolean value. The first string passed to the function is the string of valid letters from step 1; the
	second string is a guess from the user. The function should return True only if the user’s guess
	string contains exactly 10 unique letters from the valid letters string. This function does NOT
	check if the user’s guess is the correct solution to the puzzle. For example, if the user’s guess is
	TAKEOURSIM or IMAKETOURS, the function returns True; if the user’s guess is
	IMAKEIMAKE, TAKEOUR, TAKEOURSIMM, or TAKEOURSBD, the function returns False
3. Create a function named check_user_guess that takes in as arguments four integers
	representing the dividend, quotient, divisor, and remainder (in that order) and returns a
	Boolean value. The function should return True only if the following equation holds:
	Dividend = Quotient * Divisor + Remainder. Otherwise, the function should return False
4. Create a function named make_number that takes in as arguments two strings and returns one
	integer. The first string passed to the function contains a word to be converted to an integer;
	the second string is the user’s guess which should be used as a key to convert a word (the first
	string) to its integer equivalent. For example, if the word is RUE and the user’s guess is
	TAKEOURSIM, the integer equivalent of RUE is 653
5. Create a function named make_numbers that takes in two arguments, both of which are strings,
	and returns a tuple of four integers. The first string passed to the function is the puzzle string;
	the second string is the user’s guess. Your make_numbers function should call your
	make_number function four times to create the four integers, and then should return a tuple of
	those four values that are the equivalent integers of the words representing the dividend,
	quotient, divisor, and remainder (in that order). For the puzzle example shown above and the
	user guess TAKEOURSIM, your function should return (659467, 653, 316, 571).
6. Create a function named main that does not take in any arguments nor return any values. This
	function should take as input from the user a puzzle string, print the puzzle, ask the user to
	enter a guess, and output an appropriate message. Your main function should call your
	get_valid_letters, is_valid_guess, make_numbers, and check_user_guess functions, as well as
	the provided print_puzzle function. Format your output as shown below.

'''
def print_puzzle(puzzle):
    ''' Print puzzle as a long division problem. '''
    puzzle = puzzle.split(',')
    for i in range(len(puzzle)):
        if i == 1:
            print(f'{len(puzzle[i].split("|")[1]) * "_": >16}')
        print(f'{puzzle[i]: >16}')
        if i > 1 and i % 2 == 0:
            print(f"{'-'*len(puzzle[i]): >16}")

def get_valid_letters(puzzle):
    letters =""
    for i in range(len(puzzle)):
        if letters.find(puzzle[i]) == -1 and len(letters) < 10 and puzzle[i].isalpha():
            letters += puzzle[i]
    return letters

def is_valid_guess(valid, guess):
    if len(guess) != 10:
        return False
    
    i = 0
    j = 0
    while j < 10:
        index = valid.find(guess[i])
        
        if index == -1:
            return False
        valid = valid[:index] + valid[index +1:]
        guess = guess[i+1:]
        j+=1
    return True

def check_user_guess(dividend, quotient, divisor, remainder):
    ans = quotient*divisor+remainder
    if ans == dividend:
        return True
    return False

def make_number(convert, keys):
    fin = ""
    nums = [0,1,2,3,4,5,6,7,8,9]
    for i in range(len(convert)):
        index = keys.find(convert[i])
        if index != -1:
            fin += str(nums[index])
    return int(fin)

def make_numbers(a,b):
    splitpuzzle = a.split(" | ") #have to get rid of this yippee!!
    quodiv = splitpuzzle[0].split(",") #have to get rid of this too and idk how to do it in 1 line yippee!!!!
    everythingelse = splitpuzzle[1].split(",")
    truelist = [everythingelse[0],quodiv[0],quodiv[1],everythingelse[len(everythingelse)-1]]
    return make_number(truelist[0],b),make_number(truelist[1],b),make_number(truelist[2],b),make_number(truelist[3],b)

def main():
    puzzle = input("Enter a word arithmetic puzzle: ")
    print()
    print_puzzle(puzzle)
    guess = input("\nEnter your guess, for example ABCDEFGHIJ: ")
    letters = get_valid_letters(puzzle)
    if is_valid_guess(letters, guess) == True:
        valuetuple = make_numbers(puzzle,guess)
        if check_user_guess(valuetuple[0],valuetuple[1],valuetuple[2],valuetuple[3]) == True:
            print("Good job!")
        else:
            print("Try again!")
    else:
        print("Your guess should contain exactly 10 unique letters used in the puzzle.")

if __name__ == '__main__':
	main()
    

