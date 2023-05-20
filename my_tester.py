
from main import floating_point_number
def is_real_number(p_test_string):  
    #The code below is built on the valid integer function discussed in  class  
    valid = True
    character = ''
    decimal_point_index = -1
    length = len(p_test_string)

    #Using an if statement to ensure that users enter at least one character
    if (length < 1):
        valid = False
        return valid
    else:
        #if it has more than 1 char, character is given the first element
        character = p_test_string[0]

    #Detecting leading positive or negative signs
    if (character == '+' or character == '-') and length >1:
        p_test_string = p_test_string[1:]
        #adusting the string length variable
        length = len(p_test_string) 

    #Determining the index of the radix point     
    for i in range(length): 
        if p_test_string[i] == '.':
            decimal_point_index = i
            break 
        
    for i in range(length): 
        #if radix point has been found just continue
        if i == decimal_point_index: 
            continue
        #check if character is not within an acceptable number range 
        ord_value = ord(p_test_string[i]) 
        if ord_value < 48 or ord_value > 57:
            valid = False
            break 
    
    return valid


#Declaring variables
def is_valid_ieee_num (p_test_string):
    is_valid = True
    length = len(p_test_string)
    
    #checking if the length is less than 32 bits
    if length != 32:
        is_valid = False 
    else:
        # checking for every character to see if its 0 or 1. If it isn't we return false,
        # otherwise we continue
        for i in p_test_string:
            if i == '0' or i == '1':
                continue
            else:
                is_valid = False
        
    return is_valid

menu_option = ''
user_real_num_as_string = ""
user_ieee_num_as_string = ""

print('Welcome to the floating point converter program!!!')


while True:
    #displaying early greeting messages
    print('\tA) A base 10 real number to string representation of the IEEE floating point format')
    print('\tB) A string representation of the IEEE floating point format to a base 10 real number')
    print('\tQ) Quit')

    
    menu_option = input('\nPlease enter A, B, or Q: ').lower()
    
    #Using an if-else ladder to display appropriate results
    if menu_option == 'a' or menu_option == 'b' or menu_option == 'q':
        if menu_option == 'a':
            while True:
                user_real_num_as_string = input('Please enter your real number: ')
                
                #calling on the is_real_number to ensure that only valid characters go through
                if is_real_number(user_real_num_as_string) == False :
                    continue
                else:
                #calling on the convert_Real_to_floating function to convert the input to a float
                    print(floating_point_number.convert_real_to_floating_point_number(user_real_num_as_string))
                    break
    
        elif menu_option == 'b':
            while True:
                user_ieee_num_as_string = input('Please enter your IEEE single precision ' 
                + 'floating point number (as a binary): ')
            #calling on the is_valid_ieee_num to ensure that only valid inputs go through
                if is_valid_ieee_num(user_ieee_num_as_string) == False : 
                    continue
                else:
                #calling on the convert_floating_point_number_to_real function to convert 
                #the input  
                    print(floating_point_number.convert_floating_point_number_to_real(user_ieee_num_as_string))
                    break
        elif menu_option == 'q':
            print('Thank you for using my program!')
            break
    else:
        continue
    
