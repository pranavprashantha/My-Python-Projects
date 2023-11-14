# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Pranav Rao
# Section:      564
# Assignment:   9.15
# Date:         24 10 2023

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
    

