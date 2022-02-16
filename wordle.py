import numpy as np

print("wordle Solver")
print("type 0 for incorrect, 1 for wrong spot and 2 for correct")
print("------------\nStart with CRANE")



startWord = 'crane'
curWord = startWord
p = 0

badwords = []
THEWORD = [0,0,0,0,0]
ishwords = []
guesses = []
bigwin = [2,2,2,2,2]

def ask(curword):
    guesses.append(curWord)
    correct = list(input('Enter numbers: '))
    corArray = []

    for i in range(len(correct)):
        corArray.append(int(correct[i]))

    if corArray == bigwin:
        print("Congratulations!")
    else:
        check(curword,corArray)



def badWords(correctlist,wordlist):
    for i in range(len(correctlist)):

        if correctlist[i] == 1 and wordlist[i] not in ishwords:
                ishwords.append(wordlist[i])
        elif correctlist[i] == 2:
            THEWORD.pop(i)
            THEWORD.insert(i,wordlist[i])
        elif correctlist[i] == 0 and wordlist[i] not in ishwords and wordlist[i] not in badwords and wordlist[i] not in THEWORD:
            badwords.append(wordlist[i])


def check(curWord,correctarray):
    wordlist = list(curWord)
    badWords(correctarray,wordlist)
    nextWord(badwords,THEWORD,ishwords,curWord)

def nextguess(badwords,THEWORD,ishwords,curWord):
    print("-----------\nNext guess: ")
    print(curWord)
    ask(curWord)


def nextWord(badwords,THEWORD,ishwords,currentWord):
    print(badwords,THEWORD,ishwords)
    word2 = currentWord
    words = open('Common.txt','r')
    for i in words.readlines():
        charlist = list(i)
        charlist.pop()
        error = False
        ish2 = ishwords.copy()
        if i in guesses:
            print("allerede gjettet")
            break
        for j in range(5):
            if charlist[j] in badwords:
                error = True
                break
            if THEWORD[j] != 0:
                if charlist[j] != THEWORD[j]:
                    error = True
                    break
            if charlist[j] in ish2:
                ish2.remove(charlist[j])
        if error == False and len(ish2)==0:
            curWord = i
            nextguess(badwords,THEWORD,ishwords,curWord)
            break

    if currentWord == word2:
        print("no more guesses")

ask(curWord)
