# python3
import heapq


def build_min_heap(arr):
    n = len(arr)
    for i in range(n // 2, -1, -1):
        heapify_up(arr, i)

def heapify_up(arr, i):
    while i > 0:
        parent = (i - 1) // 2
        if arr[parent] > arr[i]:
            arr[parent], arr[i] = arr[i], arr[parent]
            i = parent
        else:
            break


    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)



def main():
    atbilde = input("F vai I?")
    if "I" in atbilde:
       n = int(input())
       parents = list(map(int,input().split()))
       assert len(arr) == n
       swaps = build_min_heap(arr)
       print(len(swaps))
       for i, j in swaps:
           print(i,j)
    elif "F" in atbilde:
         failanos = input()
         file = './test/' + failanos
         if "a" not in failanos:
             try: 
                 with open(file) as file1:
                    n = int(file1.readline())
                    parents = list(map(int, file1.readline().split()))
                    assert len(arr) == n
                    swaps = build_min_heap(arr)
                    print(len(swaps))
                    for i, j in swaps:
                        print(i, j)
             except Exception as kluda:
                 print("kluda:", str(kluda))
                 return
         else:
             print("nepareizs nosaukums")
             return

    print(compute_height(n, parents))
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard

    # checks if lenght of data is the same as the said lenght
    

    # calls function to assess the data 
    # and give back all swaps
    

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps



if __name__ == "__main__":
    main()
