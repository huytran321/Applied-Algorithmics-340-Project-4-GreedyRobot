#Huy Tran
#GreedyRobot Class
#Goal is return all the paths possible

class GreedyRobot():

    def __int__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def getX1():
        return self.__x1

    def getY1():
        return self.__y1

    def getX2():
        return self.__x2

    def getY2():
        return self.__y2

    def setX1(self, x1):
        self.__x1 = x1
 
    def setY1(self, y1):
        self.__y1 = y1

    def setX2(self, x2):
        self.__x2 = x2

    def setY2(self, y2):
        self.__y2 = y2
    
    #This methods tries to find the default path which is a list of all the letters in the program
    def findingOneOfThePaths(x1, y1, x2, y2):
        
        defaultPathList = []
        x = True
        y = True

        while(x and y):
        
            if y1 < y2:
                defaultPathList.append("N")
                y1 += 1
            elif y1 > y2:
                defaultPathList.append("S")
                y1 -= 1
            elif x1 < x2:
                defaultPathList.append("E")
                x1 += 1
            elif x1 > x2:
                defaultPathList.append("W")
                x1 -= 1
            elif x1 == x2:
                x = False
            elif y1 == y2:
                y = False

        return defaultPathList

    #This method takes a list and use a recursive function to find all the possible paths
    def findingAllPaths(list):

        if len(list) == 0:
            return [""]

        if len(list) == 1:
            return[list]

        l = []

        for i in range(len(list)):
            m = list[i]
            remaingList = list[:i] + list[i + 1:]

            for p in GreedyRobot.findingAllPaths(remaingList):
                if ([m] + p) not in l:
                    l.append([m] + p)
        return l

    #This would combine both programs to create a conhesive method that would print all the paths and the count
    def combiningBothPaths(x1, y1, x2, y2):

        defaultFirstPath = GreedyRobot.findingOneOfThePaths(x1,y1,x2,y2)
        listOfAllPaths = GreedyRobot.findingAllPaths(defaultFirstPath)
        count = len(listOfAllPaths)

        for i in listOfAllPaths:
            path = i
            word = ""
            for j in range(len(path)):
                word += path[j]
            print(word)
        print("Number of Paths: ", count)

  







