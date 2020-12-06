import random
def generate_num():
    digits=list(range(9))
    return digits[:3]    
def user_input():
    inp=list(map(int,(input("ONCE AGAIN, GET IT RIGHT? "))))
    return inp

def get_clues(dig,tell):
    if(dig==tell):
        clue="YOU GUESSED IT RIGHT! GENIUS"
    elif(dig[0]==tell[0] or dig[1]==tell[1] or dig[2]==tell[2]):
        clue="MATCH"
    elif((dig[0] in tell or dig[1] in tell or dig[2] in tell) and (dig[0]!=tell[0] or dig[1]!=tell[1] or dig[2]!=tell[2])):
        clue="CLOSE"
    else:
        clue="NOPE"
    return clue

if __name__ == "__main__":
    dig=[]
    dig=generate_num()
    print("-------HEY USER!-------")
    print("RULES ARE AS FOLLOWS:")
    print("     1. YOU'LL GET A CLUE AFTER YOUR EVERY ATTEMPT")
    print("     2. CLUES WILL BE MATCH, CLOSE AND NOPE")
    print("     3. NOPE MEANS NO DIGIT MATCHED")
    print("     4. CLOSE YOU'VE GUESSED A CORRECT DIGIT BUT IN THE WRONG POSITION")
    print("     5. MATCH MEANS YOU HAVE GUESSED A DIGIT IN ITS CORRECT POSITION")
    print("-------NOW YOU ARE GOOD TO GO!-------")
    print("START")
    first_attempt=list(map(int,(input("GUESS IT RIGHT THE FIRST TIME: "))))
    tell=[]
    clue=get_clues(dig,first_attempt)
    print(clue)
    count=0
    while(clue!=" ##### YOU GUESSED IT RIGHT! GENIUS! #####"):
        count+=1
        if(count%3==0 and count%5!=0):
            print("--TRY TRY, YOU'LL SUCCEED--")
            print("COME ON, BRAINSTORM MORE!")
        elif(count%5==0):
            print("---------TRY---------")
            print("--DONT YOU GIVE UP!--")
        tell=[]
        tell=user_input()
        clue=""
        clue=get_clues(dig,tell)
        print(clue)
        
