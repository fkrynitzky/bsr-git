
def adding(x,y):
    anwser = 0
    reverse_x = x[::-1]
    reverse_y = y[::-1] 
    if(len(x) > len(y)):
        for z in range(0,len(y)):
            if(int(reverse_x[z]) > int(reverse_y[z])):
                anwser = anwser + int(reverse_x[z])* pow(10,z)
            else: anwser = anwser + int(reverse_y[z]) * pow(10,z)
        for z in range(len(y),len(x)):
            anwser = anwser + int(reverse_x[z]) * pow(10,z)
    else:
        for z in range(0,len(x)):
            if(int(reverse_x[z]) > int(reverse_y[z])):
                anwser = anwser + int(reverse_x[z])*pow(10,z)
            else: anwser = anwser + int(reverse_y[z]) * pow(10,z)
        for z in range(len(x),len(y)):
            anwser = anwser + int(reverse_y[z]) * pow(10,z)
    return anwser



def multiplication(x,y):              
    if(int(x) < 10 and int(y) < 10):
        if (int(x) > int(y)):
            return x
        else:
            return y


print("Welcome to lunar arthmetic.")

while True:
    number_a = input("Please write first number: ")
    number_b = input("Please wrtie second number: ")
    choice = input("Do you want to multiply or add. [m/a]  ")
    if (choice == 'm'):
        print("This anwser is not ready yet. Please try later.")
    elif (choice == 'a'):
        print(f"The answer is {adding(number_a,number_b)}")
    else: print("Wrong anwser please try again")

        


