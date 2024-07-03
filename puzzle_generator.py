def checker(word,row,col,puzzel,direction):
    # فقط حرکت روبه راست و پایین بررسی میشه چونبا بکترکینگ مینویسیم برنمیگردیم درسته ؟
    if direction == "rowy":
        for i in range(len(word)):
            if col + len(word)> len(puzzle[0]):
                return False
            if puzzle[row][col+i] == "#":
                return False
    elif direction == "coly":
        for i in range(len(word)):
            if row + len(word) > len(puzzle):
                return False
            if puzzel[row+i][col] == "#":
                return False
    return True

def puzzel_solver(puzzle , name_list , index = 0):
    if len(name_list) == 0 :
        puzzle_printer(puzzle)
        return 
    word = name_list[index]
    for direction in ("rowy","coly"):
        for row in range(len(puzzle)):
            for col in range(len(puzzle[0])):
                if checker(word,row,col,puzzle,direction):
                    place_word(word,row,col,puzzle,direction)
                    name_list.remove(word)
                    puzzel_solver(puzzle , name_list , index = 0)
                    # چجوری ریکرسیو بشه ؟
                    # چجوری بک ترکینگش کنیم ؟

def place_word(word,row,col,puzzle,direction):
    if direction == "rowy" :
        for i in range(len(word)):
            puzzle[row][col+i] = word[i]
    elif direction == "coly" :
        for i in range(len(word)):
            puzzle[row+i][col] = word[i]
    return puzzle

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

puzzel_solver(puzzle,name_list)