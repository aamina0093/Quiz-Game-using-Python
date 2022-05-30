#quiz game
print("Welcome to Quiz Game")
#player details
player_name = input("Name of the Player: ")
print("Hello", player_name)
#permission to play
play_permission = input("Do you want to play?(yes/no) ")
if play_permission.lower() != "yes":
    print("Thank you. Come Again!!")
    quit()
else:
    print("Let's Play!!")

#to calculate score
score = 0

#quiz questions
ques1 = input("How does a CD Player record sounds? ")
#title function to capitalize each word in a string.
# print(ques1.title())
if ques1.title() == "Laser Beam":
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer")

ques2 = input("Full form of GPU? ")
#title function to capitalize each word in a string.
# print(ques1.title())
if ques2.title() == "Graphical User Interface":
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer")

ques3 = input("The process of encoding an information in a way that only someone with a key can decode it? ")
#title function to capitalize each word in a string.
# print(ques3.title())
if ques3.title() == "Encryption":
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer")

ques4 = input("The first computer virus is:? ")
#title function to capitalize each word in a string.
# print(ques4.title())
if ques4.title() == "Creeper":
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer")

ques5 = input("Programs designed to perform specific tasks are called:? ")
#title function to capitalize each word in a string.
# print(ques5.title())
if ques5.title() == "Application Software":
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer")

ques6 = input("Which protocol is used to send email?(Write full form) ")
#title function to capitalize each word in a string.
# print(ques6.title())
if ques6.title() == "Simple Mail Transfer Protocol":
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer")

ques7 = input("Which computer program converts assembly language to machine language? ")
#title function to capitalize each word in a string.
# print(ques7.title())
if ques7.title() == "Assembler":
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer")

ques8 = input("Who is the father of Indian Supercomputing? ")
#title function to capitalize each word in a string.
# print(ques8.title())
if ques8.title() == "Vijay Bhatkar":
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer")

ques9 = input("Network Interface Card(NIC) is generally used for:? ")
#title function to capitalize each word in a string.
# print(ques9.title())
if ques9.title() == "Connectivity":
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer")

ques10 = input("Linux is a/an:? ")
#title function to capitalize each word in a string.
# print(ques10.title())
if ques10.title() == "Operating System":
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer")
print("End of the quiz!!!")
print("Total score: 10")
print("Your Score: ", score)
#end of quiz