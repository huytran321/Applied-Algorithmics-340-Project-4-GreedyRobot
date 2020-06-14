#Huy Tran
#Driver Code used to start the greedyrobot module

from greedyrobot import GreedyRobot

x1 = eval(input("What is the x value of the robot? "))
y1 = eval(input("What is the y value of the robot? "))
x2 = eval(input("What is the x value of the treasure? "))
y2 = eval(input("What is the y value of the treasure? "))

print("(", x1, ", ", y1, ") ", "---> ", "(", x2, ", ", y2, ") ")
print()
GreedyRobot.combiningBothPaths(x1,y1,x2,y2)
    