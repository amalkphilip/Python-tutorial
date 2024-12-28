"""
Author:Amal K Philip
Description:Program that let's the user enter to initial height of the ball. show the total distance the ball bounces and total bounce.
"""

height=int(input("Enter the height that ball dropped(in Metre):"))
distance=height
bounce=1
while height>2.16:
    height=height*.6
    distance+=height
    bounce+=1
print("Total distance:",distance,"metre")
print("Total bounce:",bounce)
