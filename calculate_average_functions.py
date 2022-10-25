#Gianna Rao
#CS175-L
#Calculate average and functions


def main():
    score1, score2, score3, score4, score5 = input_scores()
    calc_average(score1, score2, score3, score4, score5)
    response = repeat()
    if response == "yes":
        main()
    



def input_scores():
    score1 = float(input("Enter score 1: "))
    score2 = float(input("Enter score 2: "))
    score3 = float(input("Enter score 3: "))
    score4 = float(input("Enter score 4: "))
    score5 = float(input("Enter score 5: "))
    return score1, score2, score3, score4, score5
    
def determine_score(grade):
    if 90 <= grade <= 100:
        return "A"
    elif 80 <= grade <= 89:
        return "B"
    elif 70 <= grade <= 79:
        return "C"
    elif 60 <= grade <= 69:
        return "D"
    else:
        return "F"



def calc_average(score1, score2, score3, score4, score5):
    total = score1 + score2 + score3 + score4 + score5
    average = total/5
        
    print("Score                     Numeric Grade          Letter Grade")
    print("score 1: ", "               ", score1, "                  ", determine_score(score1))
    print("score 2: ", "               ", score2, "                  ", determine_score(score2))
    print("score 3: ", "               ", score3, "                  ", determine_score(score3))
    print("score 4: ", "               ", score4, "                  ", determine_score(score4))
    print("score 5: ", "               ", score5, "                  ", determine_score(score5))
    print("Average score: ", "         ", average, "                  ", determine_score(average))


       
        

    

def repeat():
    another_calculation = input("Enter 'yes' if you would like to do another calculation: ")
    return another_calculation
main()
