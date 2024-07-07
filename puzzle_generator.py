from itertools import permutations
from copy import deepcopy
def checker(word,row,col,puzzel,direction):
    if direction == "rowy":
        for i in range(len(word)):
            if col + len(word)> len(puzzle[0]):
                return False
            if puzzle[row][col+i] == "_":
                continue
            if puzzle[row][col+i] =="#":
                return False
            if puzzle[row][col+i] != word[i] :
                return False
        

    elif direction == "coly":
        for i in range(len(word)):
            if row + len(word) > len(puzzle):
                return False
            if puzzle[row+i][col] == "_":
                continue
            if puzzel[row+i][col] == '#':
                return False
            if puzzle[row+i][col] != word[i]:
                return False
    return True
flag = False
def puzzle_solver(puzzle , name_list , index = 0):
    global flag
    if flag:
        return
    puzzle_setter = deepcopy(puzzle)
    for per in permutations(name_list):
        name_list = list(per)
        if len(name_list) == index+1:
            flag = True
            puzzle_printer(puzzle)
            return 
        word = name_list[index]
        for direction in ["rowy","coly"]:
            for row in range(len(puzzle)):
                for col in range(len(puzzle[0])):
                    if checker(word,row,col,puzzle,direction):
                        #print(word)
                        #print(name_list)
                        place_word(word,row,col,puzzle,direction)
                        puzzle_solver(puzzle , name_list,index = index + 1)
        puzzle = puzzle_setter
    

def place_word(word,row,col,puzzle,direction):
    if direction == "rowy" :
        for i in range(len(word)):
            puzzle[row][col+i] = word[i]
    elif direction == "coly" :
        for i in range(len(word)):
            puzzle[row+i][col] = word[i]
    return puzzle,name_list

def puzzle_printer(puzzle):
    for i in range(len(puzzle)):
        print(puzzle[i])
    return


# تابع دیگری نیاز داریم ؟
row,col = list(map(int,input(" pls Enter the row and the column of the puzzle : ").split()))
puzzle = []
mini_puzzle =[]
print("now Enter youre puzzle pattern : ")
for i in range(row):
    line = input()
    for j in line:
        mini_puzzle.append(j)
    puzzle.append(mini_puzzle)
    mini_puzzle = []
name_list = list(input(" Enter the list of the names : ").split())
puzzle_solver(puzzle,name_list)