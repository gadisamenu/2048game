import random
import turtle
 
#creating turtle objects
turtle.title('2048 Game')
box = turtle.Turtle()
numbers = turtle.Turtle()
turtle.tracer(7)
turtle.speed(0)
turtle.ht()
turtle.pu()
box.ht()
numbers.ht()
 
#drawing physical part of the turtle graphics 
def boxs(xcor,ycor):
    '''
    Draws a square starting at specified place by numbers xcor and ycor on turtle graphics
    '''
    box.pu()
    box.home()
    box.goto(xcor,ycor)
    box.pd()
    box.fillcolor(0.5,0.9,0.9)
    box.rt(45)
    box.begin_fill()
    box.circle(95,steps = 4)
    box.end_fill()
 
 
box.pencolor(0.5,0.8,0.1)
box.pensize(15)
xcor = [-255,-125,5,135]
ycor = [115,-10,-145,-275]
for ypos in ycor:
    for xpos in xcor:
        boxs(xpos,ypos)
 
 
 
def display(the_board, point):
    '''
    Parameter: Takes an argument of class list that has 4 by 4 double list
    Writes the values in the list on the graphics area turtle.
    '''
    numbers.clear()
    numbers.pu()
    xcor = [[0, -190], [1, -60], [2, 70], [3, 200]]
    ycor = [[0, 140], [1, 10], [2, -120], [3, -250]]
 
    for xpos in xcor:
        for ypos in ycor:
            numbers.goto(xpos[1], ypos[1])
            if the_board[ypos[0]][xpos[0]] != 0:
                numbers.write(the_board[ypos[0]][xpos[0]], align='center', font=('arial', 45, 'normal'))
 
    numbers.goto(-180, -350)
    numbers.write(f'score = {point}', align='center', font=('arial', 30, 'normal'))
 
 
 
def merge(row):
        '''
        parameters: Takes an argument of type list
        merge the element of the list by adding the equal consecutive numbers
        return: returns  a  merged list type value
        '''
        global score
        row = [value for value in row if value != 0]
 
    
        for ind in range(len(row)-1):
            if row[ind] == row[ind + 1]:
                row[ind] *= 2 
                score += row[ind]
                del row[ind +1]
 
                if len(row) == 3  and ind == 0:
                    if  row[ind + 1] == row[ind + 2]:
                        row[ind + 1] *=2
                        score += row[ind +1]
                        del row[ind + 2]
                break
        if len(row) < 4:
            while len(row)< 4:
                row.append(0)
        return row
           
 
def available_space(board):
    
    '''
    Takes an argument of type list.  
    returns pair of number representing,row and column, selected randomly  one of positions at which  value of list is zero.
    Parameter: takes list type argument.
    
    '''
    free_position = []
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                free_position.append([i,j])
    return free_position
 
def win_game_over(board):
    '''
    takes one list class parameter and checks if the player is in game over state winning. 
    '''
    states = []
    for i in range(4):
        for j in range(4):
            if board[i][j] == 2048:
                turtle.home()
                turtle.write('You Won!!!',align= 'center' , font = ('arial',70,'normal'))
                turtle.clear()
                turtle.done()
 
            if available_space(board) == []:
                if i ==0 and j == 0:
                    states.append( (board[0][0] != board[0][1]) and  (board[0][0] != board[1][0]))
                elif i==0 and j  in range(1,3):
                    states.append( (board[i][j] != board[i + 1][j]) and (board[i][j] != board[i][j-1]) and (board[i][j] != board[i][j+1]))
                elif i ==0 and j == 3:
                    states.append( (board[0][3] != board[0][2]) and  (board[0][3] != board[1][3]))
                elif i in range(1,3) and j==0:
                    states.append( (board[i][j] != board[i-1][j]) and (board[i][j] != board[i + 1][j]) and (board[i][j] != board[i][j+1]))
                elif i in range(1,3) and j==3:
                    states.append( (board[i][j] != board[i-1][j]) and (board[i][j] != board[i + 1][j]) and (board[i][j] != board[i][j-1]))
 
 
                elif i ==3 and j == 0:
                    states.append( (board[3][0] != board[2][0]) and  (board[3][0] != board[3][1]))
               
                elif i ==3 and j == 3:
                    states.append( (board[3][3] != board[3][2]) and  (board[3][3] != board[2][3]))
 
                elif i==3 and j  in range(1,3):
                    states.append( (board[i][j] != board[i-1][j]) and (board[i][j] != board[i][j-1]) and (board[i][j] != board[i][j+1]))
                else:
                    states.append( (board[i][j] != board[i-1][j]) and (board[i][j] != board[i + 1][j]) and (board[i][j] != board[i][j-1]) and (board[i][j] != board[i][j+1]))
 
                for state in states:
                    if state == True:
                        if states.index(state) != (len(states)-1):
                            continue
                        turtle.pu()
                        turtle.goto(0,250)
                        turtle.write('Game Over !!!',align= 'center' , font = ('arial',70,'normal'))
                        numbers.clear()
 
                    else:
                        turtle.clear()
                        return
 
                        
 
 
def generator(board):
    '''Takes no argument.  
    produces random number one of 2 and 4.   
    returns the random number.
    Replace one zero by random number.
    No return
    '''
    available = available_space(board)
    row,column = random.choices(available).pop()
 
    available_numbers = [2,4]
    random_number = random.choices(available_numbers,cum_weights=(0.80,1)).pop()
    board[row][column] = random_number
 
def possible_movement(board,original):
    '''
    checks possible movement by comparing the first and after movement values. Then checks for any change, if there is a change it adds a new number.
    '''
    if original != board:
        generator(board)
    display(board, score)
    win_game_over(board)
    
 
    
 
def to_left():
    '''
    Take no argument but uses global variable then update the variable as wanted
    '''
    original = board[:]
    for index in range(4):
        board[index] = merge(board[index])
    possible_movement(board,original)
     
 
 
def to_right():
    '''
    No parameters. uses globally defined board and calls function merge and give it row by inverting
    and receives self.board from it and inverts.
    '''
    original = board[:]
    for index in range(4):
        board[index] = merge( board[index][::-1] ) [::-1]
    possible_movement(board,original)
    
def up_ward():
    '''
    No parameters. uses globally defined board and calls function merge and give it row by transposing
    and receives board from it and reverses.
    '''
    global board
    original = board[:]
    transposed_board = [[row[i] for row in board] for i in range(4)]
    for index in range(4):
        transposed_board[index] = merge(transposed_board[index])
    board = [[row[i] for row in transposed_board] for i in range(4)]
    possible_movement(board,original)
 
 
def down_ward():
    '''
    No parameters. uses globally defined board and calls function merge and give to  it a row by inverting and transposing
    and receives board from it and reverses.
    '''
    global board
    original = board[:]
    board = board[::-1]
    transposed_board = [[row[i] for row in board] for i in range(4)]
    for index in range(4):
        transposed_board[index] = merge(transposed_board[index])
    board = [[row[i] for row in transposed_board] for i in range(4)]
    board = board[::-1]
    possible_movement(board,original) 
 
 
 
 
#creating initial list to start the game
 
board = [[0]*4 for _ in range(4)]
score = 0
generator(board)
generator(board)
display(board, score)             
 
#pairing the functions with keys on turtle graphics 
turtle.onkey(to_left,'Left')
turtle.onkey(to_right,'Right')
turtle.onkey(up_ward,'Up')
turtle.onkey(down_ward,'Down')
turtle.listen()      
turtle.done()
 
        
 
 
 
 
 

