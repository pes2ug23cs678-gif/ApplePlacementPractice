def giveMax(Input:list[int])->int:
    OutputList = []
    n = len(Input)
    for i in range(n-1):
        a = Input[i]
        for j in range(i+1, n):
            InputList = []
            b = Input[j]
            width = min(a, b)
            length = j - i
            InputList.append([a, b])
            InputList.append(width * length)
            OutputList.append(InputList)
    Maximum = OutputList[0][1]
    for g in OutputList:
        if Maximum < g[1]:
            Maximum = g[1]
    return Maximum
def main():
    FirstEntry = input().strip().split()
    Input = list(map(int, FirstEntry)) #This is the second part to be seen over here!!
    TwoLines = giveMax(Input) #This is the next part to be seen over here!!
    print(TwoLines)
if __name__ == "__main__":
    main()
