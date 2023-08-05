def fileWork(list):
    
    
    negativeC = 0
    oddC = 0
    negativeS = 0
    positiveS = 0
    positiveN = 0
    for i in list:
        j = i.split(' ')
        num = int(j[1])
        if num<0:
            negativeS+=num
            negativeC+=1
        else:
            positiveS+=num
            positiveN+=1
        if num%2==1:
            oddCount+=1
    print("negative count =",negativeC)
    print("odd count =",oddC)
    print("negative sum =",negativeS)
    print("positive average =",positiveS/positiveN)


fp = open('file.txt', 'r')
list = fp.readlines()
fileWork(list)
fp.close( )
