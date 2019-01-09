
def adding_beta(x,y):
    anwser = ""
    reverse_x = x[::-1]
    reverse_y = y[::-1]
    if(len(x) > len(y)):
        for z in range(0,len(y)):
            if(int(reverse_x[z]) > int(reverse_y[z])):
                anwser += reverse_x[z]
            else: anwser += reverse_y[z]
        for z in range(len(y),len(x)):
            anwser += reverse_x[z]
    else: 
        for z in range(0,len(x)):
            if(int(reverse_x[z]) > int(reverse_y[z])):
                anwser += reverse_x[z]
            else: anwser.append(reverse_y[z])
        for z in range(len(x),len(y)):
            anwser += reverse_y[z]
                   
    return ''.join(reversed(anwser))



def multiplication(x,y):
                
    
if(__name__ == "__main__"):
    while True:
        print("Welcome to lunar arthmetic.")
        number_a = input("Please write first number: ")
        number_b = input("Please wrtie second number: ")
        choice = input("Do you want to multiply or add. [m/a]  ")
        if (choice == 'm'):
            print("This anwser is not ready yet. Please try later.")
        elif (choice == 'a'):
            print(f"The answer is {adding_beta(number_a,number_b)}")
        else: print("Wrong anwser please try again")

        


