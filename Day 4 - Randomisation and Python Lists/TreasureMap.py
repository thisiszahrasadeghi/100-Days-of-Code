#Exercise 4.3 :
#A program which will mark a spot with 💰.

row1 = ["⬜️" , "⬜️" , "⬜️"]
row2 = ["⬜️" , "⬜️" , "⬜️"]
row3 = ["⬜️" , "⬜️" , "⬜️"]
map = [row1 , row2 , row3]
print(f"{row1}\n{row2}\n{row3}\n ")
position = input ("Where do you want to put the treasure?\n")

horizonal = int(position[0])
vertical = int(position[1])
# selected_row = map[vertical-1]
# selected_row[horizonal-1] = "💰"
#or :
map[vertical -1][horizonal -1] = "💰"
print(f"{row1}\n{row2}\n{row3}\n ")
