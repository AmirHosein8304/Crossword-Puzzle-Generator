row,col = list(map(int,input(" pls Enter the row and the column of the puzzle : ").split()))
puzzle = []
print("now Enter youre puzzle pattern : ")
for i in range(row):
    puzzle.append(input())
name_list = list(input(" Enter the list of the names : ").split()) 

def checker(word,row,col,puzzel,direction):
    if direction == "rowy":
        for i in range(len(word)):
            if puzzle[row][col+i] == "#":
                return False
        if puzzle[row][col+len(word)+1] == "#":
            return True
    elif direction == "coly":
        for i in range(len(word)):
            if puzzel[row+i][col] == "#":
                return False
        if puzzel[row+len(word)+1][col] == "#":
            return True
    return False


def puzzel_solver(len_list , name_list):