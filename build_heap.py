# python3
def heapsort(kaudze):
    n = len(kaudze)
    swaps = []
    for i in range(n// 2-1, -1, -1):
        left = 2*i+1
        right = 2 * i + 1
        if left < n and kaudze[left] < kaudze [i]:
            kaudze[left], kaudze [i] = kaudze[i], kaudze[left]
            swaps.append((kaudze[left], kaudze[i]))
        if right < n and kaudze [right] < kaudze[i]:
            kaudze[right], kaudze[i] = kaudze[i], kaudze[right]
            swaps.append((kaudze[right], kaudze[i]))
    return kaudze[::-1], swaps[::-1]


    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)



def main():
    atbilde = input("F vai I?")
    if "I" in atbilde:
       b = int(input())
       kaudze = list(map(int,input().split()))
       min = kaudze_to_min(kaudze)
       print(" ".join(map(str, min)))
    elif "F" in atbilde:
         failanos = input()
         file = './test/' + failanos
         if "a" not in failanos:
             try: 
                 with open(file, "r") as file1:
                    kaudze = list(map(int, file.readLine().split()))
                 min, swaps = kaudze_to_min(kaudze)
                 for swap in swaps:
                    print(f"{swap[0]} un {swap[1]}")
                 with open(file2, "w") as file1:
                    file.write(" ".join(map(str,min)))
             except Exception as kluda:
                 print("kluda:", str(kluda))
                 return
         else:
             print("nepareizs nosaukums")
             return
    
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



#if __name__ == "__main__":
main()
