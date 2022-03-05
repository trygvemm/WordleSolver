import numpy as np

print("wordle Solver")
print("type 0 for incorrect, 1 for wrong spot and 2 for correct")
print("------------\nStart with CRANE")

startWord = 'crane'
curWord = startWord

badwords = []
THEWORD = [0,0,0,0,0]
ishwords = []
guesses = []
bigwin = [2,2,2,2,2]
ishplace = []

def ask(curword):
    correct = list(input('Enter numbers: '))
    corArray = []

    for i in range(len(correct)):
        corArray.append(int(correct[i]))

    if corArray != bigwin:
        check(curword,corArray)
    else:
        print("Congratulations!")

def badWords(correctlist,wordlist,curWord):
    for i in range(len(correctlist)):
        if correctlist[i] == 1:
            isharr = ['','','','','']
            isharr.pop(i)
            isharr.insert(i,wordlist[i])
            ishplace.append(isharr)
            if wordlist[i] not in ishwords:
                ishwords.append(wordlist[i])
        elif correctlist[i] == 2:
            for k in range(len(ishwords)):
                if wordlist[i] == ishwords[k]:
                    ishwords.pop(k);
                    break
            THEWORD.pop(i)
            THEWORD.insert(i,wordlist[i])
        elif correctlist[i] == 0 and wordlist[i] not in ishwords and wordlist[i] not in badwords and wordlist[i] not in THEWORD:
            badwords.append(wordlist[i])

        elif correctlist[i] == 3:
            print("Skipped")
            guesses.append(curWord[:-1])


def check(curWord,correctarray):
    wordlist = list(curWord)
    badWords(correctarray,wordlist,curWord)
    nextWord(badwords,THEWORD,ishwords,curWord)

def nextguess(badwords,THEWORD,ishwords,curWord):
    print("-----------\nNext guess: ")
    print(curWord)
    guesses.append(curWord[:-1])
    ask(curWord)

def nextWord(badwords,THEWORD,ishwords,currentWord):
    print("Bad letters:",badwords,"\nGood letters:",THEWORD,"\nIsh letters:",ishwords)
    word2 = currentWord
    words = open('Common.txt','r')
    for i in words.readlines():
        charlist = list(i)
        charlist.pop()
        error = False
        ish2 = ishwords.copy()
        for j in range(5):
            for k in range(len(ishplace)):
                if charlist[j] == ishplace[k][j]:
                    error = True
                    break
            if charlist[j] in badwords:
                error = True
                break
            if THEWORD[j] != 0:
                if charlist[j] != THEWORD[j]:
                    error = True
                    break
            if charlist[j] in ish2:
                ish2.remove(charlist[j])
            if (error):
                break
        if error == False and len(ish2)==0 and i[:-1] not in guesses:
            curWord = i
            nextguess(badwords,THEWORD,ishwords,curWord)
            break


    if currentWord == word2:
        print("no more guesses")

ask(curWord)
