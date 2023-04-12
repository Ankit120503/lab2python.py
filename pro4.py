myNumbers = [2, 4, 12, 15, 16, 22, 3, 21]

def print_elements(list):
     print("all numbers in the list:")
     for num in list:
        print(num)
     print("numbers greater than 12: ")
     for num in myNumbers:
        if num > 12:
            print(num)

     

print_elements(myNumbers)