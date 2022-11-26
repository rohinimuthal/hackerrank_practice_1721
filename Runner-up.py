if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lst=list(arr)
    lst.sort()
    def runnerUp(lst):
        l=len(lst)
        while l>0:

            if lst[-2]<lst[-1]:
                return lst[-2]
            else:
                lst.pop()
            l-=1
    print(runnerUp(lst))