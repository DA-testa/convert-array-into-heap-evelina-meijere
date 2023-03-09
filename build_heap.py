# python3


def build_heap(data):
    n = len(data)
    levels = int(math.log2(n)) + 1
    
    swaps = 0
    for level in range(levels-2, -1, -1):
        for i in range(2**level - 1, 2**(level+1) - 1):
            parent = i
            left_child = 2*i + 1
            right_child = 2*i + 2
            if right_child < n and data[right_child] < data[left_child]:
                smallest = right_child
            else:
                smallest = left_child
            if smallest < n and data[smallest] < data[parent]:
                data[parent], data[smallest] = data[smallest], data[parent]
                swaps += 1
                
    return swaps
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)



def main():
    atbilde = input("F vai I?")
    if "I" in atbilde:
       n = int(input())
       parents = list(map(int,input().split()))
       assert len(data) == n
       swaps = build_heap(data)
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
                    assert len(data) == n
                    swaps = build_heap(data)
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
