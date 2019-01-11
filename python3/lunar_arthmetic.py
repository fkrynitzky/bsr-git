
def adding(x,y):
    if(len(y) > len(x)):
        x,y = y,x
    anwser = ""
    reverse_x = x[::-1]
    reverse_y = y[::-1]
    for z in range(0,len(y)):
        if(int(reverse_x[z]) > int(reverse_y[z])):
            anwser += reverse_x[z]
        else: anwser += reverse_y[z]
    for z in range(len(y),len(x)):
        anwser += reverse_x[z]            
    return ''.join(reversed(anwser))

def multiplication(x,y):
    if(len(y) > len(x)):
        x,y = y,x
    sum1 = ""
    sum2 = ""        
    reverse_x = x[::-1]
    reverse_y = y[::-1]
    for z in range(0,len(y)):
        for t in range(0,len(x)):
            if(int(reverse_y[z]) < int(reverse_x[t])):
               sum1 += reverse_y[z]
            else: sum1 += reverse_x[t]
        sum1 = sum1[::-1]
        u = z
        while(u>0):
            sum1 += "0"
            u -= 1
        sum2 = adding(sum1,sum2)
        sum1 = ""
    return ''.join(sum2)

    
if(__name__ == "__main__"):
    while True:
        print("Welcome to lunar arthmetic.")
        number_a = input("Please write first number: ")
        number_b = input("Please wrtie second number: ")
        choice = input("Do you want to multiply or add. [m/a]  ")
        if (choice == 'm'):
            print(f"This anwser is {multiplication(number_a,number_b)}")
        elif (choice == 'a'):
            print(f"The answer is {adding(number_a,number_b)}")
        else: print("Wrong anwser please try again")

        


