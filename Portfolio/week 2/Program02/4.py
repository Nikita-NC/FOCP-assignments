"""A kindly teacher wishes to distribute a tub of sweets between her pupils. She will
first count the sweets and then divide them according to how many pupils attend
that day. Write a program that will tell the teacher how many sweets to give to each
pupil, and how many she will have left over."""

num_of_sweets=input("Enter the number of sweets: ")
num_of_pupils=input("Enter the number of Pupils: ")

ans=int(num_of_sweets)//int(num_of_pupils)
leftover=int(num_of_sweets)%int(num_of_pupils)

print(f"There will be sweets {ans} given to each pupil and {leftover} sweets will be left over")