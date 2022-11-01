#Gianna Rao
#CS175L
#AverageFromInput

def main():
    infile = open("numbers.txt", "r")
    
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    
    
    line_1 = float(line1)
    line_2 = float(line2)
    line_3 = float(line3)
    
    total2 = (line_1 + line_2)
    total3 = (line_1 + line_2 + line_3)
    
    average = (line_1+line_2+line_3)/3
    
    for x in range(1,2):
        print("I read in", x, "number(s) Current number is: ", end="")
        print(f'{line_1:.2f}', end=" ")
        print("Total is: ", end="")
        print(f'{line_1:.2f}')
        
        print("I read in", x+1, "number(s) Current number is: ", end="")
        print(f'{line_2:.2f}', end=" ")
        print("Total is: ", end="")
        print(f'{total2:.2f}')
        
        print("I read in", x+2, "number(s) Current number is: ", end="")
        print(f'{line_3:.2f}', end=" ")
        print("Total is: ", end="")
        print(f'{total3:.2f}')
        
        print("Average:", average)

    infile.close
        
if __name__ == "__main__":
    main()
