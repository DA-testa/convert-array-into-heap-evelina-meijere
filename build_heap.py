import os.path
import sys
# python3

def heapsort(kaudze):
    n = len(kaudze)
    swaps = []
    for i in range((n// 2)-1, -1, -1):
        o = i 
        while True:
            left = 2*o+1
            right = 2 * o + 2
            if left < n and kaudze[left] < kaudze [o]:
                o = left
            if right < n and kaudze [right] < kaudze[o]:
                o = right
            if i !=o:
                kaudze[i], kaudze[o]=kaudze[o], kaudze[i]
                swaps.append((i,o))
                i=o 
            else : break
    if len(swaps)>4*len(kaudze):
        raise Exception("EXCEPTION")

    return swaps
   





def main():
    try:
        atbilde = input("F vai I?")
    except EOFError:
        print("Nekas nav ievadīts")
        return

    if "F" in atbilde:
         failanos = input("Faila nosaukums: ")
         file = './tests/' + failanos
         if os.path.isfile(file) and os.stat(file).st_size > 0:
             with open(file, mode="r") as file1:
                 k = int(file1.readline())
                 kaudze = list(map(int,file1.readline().split()))
         else:
            print("Error: File not found or empty")
            return
    
    elif "I" in atbilde:
         k = int (input())
         kaudze = list(map(int, input().split()))
            
    else : 
        print("ERROR")
        return

    assert len(kaudze) == k
    swaps = heapsort(kaudze)

    print(len(swaps))
    for i, o in swaps:
        print(i, o)

if __name__ == "__main__":
    main()
    
    
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
