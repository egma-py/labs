import turtle as t


def draw_digit(number: list):
    for i in range(len(number)):
        if number[i][2] == 0:
            t.forward(number[i][0])
            t.left(number[i][1])
        else:
            t.pendown()
            t.forward(number[i][0])
            t.left(number[i][1])
            t.penup()
        

def def_number(number, font_number, lines_number):
    for i in range(lines_number):
        number.append(list(map(int, font_number.readline().split())))
    return number
    
    
t.shape('turtle')
t.color('red')
t.width(2)
t.speed(5)
t.penup()
lines = [5, 7, 0, 0, 7, 0, 0, 5, 0, 0]
index = []
font_index = open('font_index.txt', 'r')
draw_digit(def_number(index, font_index, lines[1]+lines[4]+lines[1]+lines[7]+lines[0]+lines[0]))
font_index.close()
