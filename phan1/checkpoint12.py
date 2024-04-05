
colors = list(("blue","red","green"))
# print("Color list : ")
# print(",".join(colors))
# new_color = input ( "input a new color :" )
# colors.append(new_color)
# print ("new color list :" + ",".join(colors))

# vitri = int(input("input position :"))
# print(f"Color at position {vitri} : {colors[vitri]}")

# delete = int(input("input to delete :"))
# colors.remove(delete)
# print(colors)
import turtle

t = turtle.Turtle()

for color in colors:
    t.color(color)
    t.forward(100) 
    t.penup()
    t.forward(10) 
    t.pendown()





