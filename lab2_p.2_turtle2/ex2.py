import turtle as t


def draw_digit(A: list):
    for i in range(len(A)):
        if A[i][2] == 0:
            t.forward(A[i][0])
            t.left(A[i][1])
        else:
            t.pendown()
            t.forward(A[i][0])
            t.left(A[i][1])
            t.penup()
        

t.shape('turtle')
t.color('red')
t.width(2)
t.penup()
drawing = 1
not_drawing = 0
no_step = 0
side_step = 30
double_side_step = 2 * side_step
diag_step = int(1.4142 * side_step)
final_step = int(side_step + side_step / 3)  
phi_1 = 90
phi_2 = 45
phi_3 = 180
phi_4 = 270
phi_5 = 225
phi_6 = 135
phi_7 = 360
phi_8 = 315
zero = [
        (side_step, phi_4, drawing), 
        (double_side_step, phi_4, drawing), 
        (side_step, phi_4, drawing), 
        (double_side_step, phi_4, drawing),
        (final_step, phi_7, not_drawing)
       ]
one = [
       (no_step, phi_4, not_drawing),
       (side_step, phi_6, not_drawing),
       (diag_step, phi_5, drawing),
       (double_side_step, phi_4, drawing),
       (side_step, phi_4, not_drawing),
       (double_side_step, phi_4, not_drawing),
       (final_step, phi_7, not_drawing)
      ]
four = [
        (no_step, phi_4, not_drawing),
        (side_step, phi_1, drawing),
        (side_step, phi_4, drawing),
        (side_step, phi_3, drawing),
        (double_side_step, phi_1, drawing),
        (side_step, phi_3, not_drawing),
        (final_step, phi_7, not_drawing)
       ]
seven = [
         (side_step, phi_5, drawing),
         (diag_step, phi_2, drawing),
         (side_step, phi_3, drawing),
         (double_side_step, phi_4, not_drawing),
         (final_step, phi_7, not_drawing),
        ]
draw_digit(one)
draw_digit(four)
draw_digit(one)
draw_digit(seven)
draw_digit(zero)
draw_digit(zero)