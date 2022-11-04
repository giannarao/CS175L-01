#Gianna Rao
#CS175L
#AverageFromInput2

def main():
    total = 0
    x = 0
    try:
        infile = open("numbers.txt", "r")
        for line in infile:
            try:
                amount = float(line)
            except ValueError:
                line = line.strip('\n')
                print("Non-numeric data found in the file.")
            else:
                total = total + amount
                x = x+1
                print("I read in", x, "number(s) Current number is: ", end="")
                print(f'{amount:.2f}', end=" ")
                print("Total is: ", end="")
                print(f'{total:.2f}')   
        average = total/x    
        print("Average:", average)
            
        infile.close
        
    except IOError:
        print("An error occurred trying to read the file.")
        
if __name__ == "__main__":
    main()
