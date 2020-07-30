# Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2. Go to the editor
#Test Data : 
#color_list_1 = set(["White", "Black", "Red"]) 
#color_list_2 = set(["Red", "Green"])
#Expected Output : 
#{'Black', 'White'}


color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])
l=[]
for x in color_list_1:
	if x not in color_list_2:
		l.append(x)
		
print(set(l))