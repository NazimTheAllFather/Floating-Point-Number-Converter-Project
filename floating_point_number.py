
def string_to_real(valid_number_string):
    fractional_string = ''
    interger_string = ''
    real_fraction = 0.0
    integer_part = 0
    has_fraction = False
    character = valid_number_string[0] 
    index = 1
    is_negative = False
    return_real_number = 0
    int_string_length = 0
     
    #checking if has been entered as a positive or negative number 
    if character == '+':
        valid_number_string = valid_number_string[1:]   
    elif character == '-':
        is_negative = True
        valid_number_string = valid_number_string[1:]  
        
    #a for loop to perform the operation of extracting integer and fractional parts as string characters
    for i in valid_number_string: 
        if i == '.':
            has_fraction = True
            continue
        if not has_fraction:
            interger_string += i
        else:
            fractional_string += i
                
    #Converting the integer string to a real number
    int_string_length = len(interger_string)
    for i in range(int_string_length):  
        integer_part += (ord(interger_string[i]) - 48) * power(10, int_string_length - 1)
        int_string_length -= 1
            
    #Converting the fractional string into a real number
    fractional_string = '.' + fractional_string    
    for index in range(index, len(fractional_string), 1):
        real_fraction += (ord(fractional_string[index]) - 48) * power(10, index * -1) 
        
    #Assinging the return value and ensuring that all negative values are returned as negative
    return_real_number = integer_part + real_fraction  
    if is_negative:
        return_real_number *= -1
        
    return return_real_number 
def fractional_part_as_real(valid_number_string):
    fractional_string = ''
    real_fraction = 0
    has_fraction = False
    index = 1
    #a for loop to perform the operation of extracting fractional part as string characters
    for i in valid_number_string: 
        if i == '.':
            has_fraction = True
            continue
        if has_fraction:
            fractional_string += i
                  
    #Converting the fractional string into a real number
    fractional_string = '.' + fractional_string  
    for index in range(index, len(fractional_string) , 1):
        real_fraction += (ord(fractional_string[index]) - 48) * power(10, index * -1) 
        
    return float(real_fraction) 
def int_part_as_int(valid_number_string):
    interger_string = ''
    integer_part = 0
    has_fraction = False
    character = valid_number_string[0] 
    int_string_length = ''
     
    #checking if has been entered as a positive or negative number 
    if character == '+':
        valid_number_string = valid_number_string[1:]   
    elif character == '-':
        is_negative = True
        valid_number_string = valid_number_string[1:]  
        
    #a for loop to perform the operation of extracting integer and fractional parts as string characters
    for i in valid_number_string: 
        if i == '.':
            has_fraction = True
            continue
        if not has_fraction:
            interger_string += i
     
    #Converting the integer string to a real number
    int_string_length = len(interger_string)
    for i in range(int_string_length):  
        integer_part += (ord(interger_string[i]) - 48) * power(10, int_string_length - 1)
        int_string_length -= 1
  
    return integer_part  
def power(base, power):
    #a simple power function to substitute math.pow 
    is_negative = False
    new_base = 1
    #converting power to a positive number
    if power < 0:
        power *= -1
        is_negative = True
        
    #performing the operation
    for i in range(power):
        new_base *= base
    
    #checking if power was indeed a negative value
    if is_negative == True:
        new_base = 1 / new_base
        
    return new_base
def int_to_binary_converter (int_num):
    #declaring intitial variables
    int_part_as_binary_rev = ""
    valid_numbers = '01'
    binary_int_part = ""
    
    #checking if int_num is 0
    if int_num == 0:
        binary_int_part = '0'
    else:
        #performing the operation 
        while int_num > 0:
            remainder = int_num % 2
            int_part_as_binary_rev += valid_numbers[float_to_int(remainder)] 
            int_num = int_num // 2
        
        #reversing the results
        binary_int_part = int_part_as_binary_rev[::-1]
    
    #returning the results as a string
    return binary_int_part
def equality_detector (num):
    #declaring a tolerance detector 
    tolerance = 1e-23
    
    #determining if num can be considered equal to 1 (by using the abs function)
    if abs(num - 1.0) < tolerance:
        return True
    return False
def convert_real_to_floating_point_number (string_arg):  
    #declaring variables
    int_part = 0
    fractional_part = 0
    fractional_part_as_binary = ""
    int_part_as_binary = ""
    int_and_frac_as_binary = ""
    character = string_arg[0]
    is_negative = False
    converted_binary_num = 0
    valid_numbers ='01'
    result = 0.0
    index = -1
    shifted_index = -1
    to_the_left = False
    Zeros = 0
    mantissa = ""
    sign = ""
    
    #checking if string_arg has been entered as a negative number 
    if character == '-':
        is_negative = True
        
    #extracting the integer part of string_arg by calling int_part_as_int and converting it
    #to binary by calling the int_to_binary_converter()
    int_part = int_part_as_int(string_arg)
    int_part_as_binary = int_to_binary_converter(int_part) 
    
    #extracting the fractional part of string_arg
    fractional_part = fractional_part_as_real(string_arg)
    
    #Converting the fractional part into binary
    while True:
        result = fractional_part * 2
        remainder = float_to_int(result) 
        fractional_part_as_binary += valid_numbers[float_to_int(remainder)] 
        fractional_part = result - remainder
        
        #The exit condition (it ensures that result is == 1 or 126 iterations have been performed)
        if ((equality_detector(result)) or len(fractional_part_as_binary) == 126) :
            break
        
    #adding the two parts up to create a binary number that isn't in scientific notation
    int_and_frac_as_binary = int_part_as_binary + '.' + fractional_part_as_binary
    
    #Determining the exponent part
    
    #determining the position of the radix point (at the number that isn't in scientific notation)
    for i in range(len(int_and_frac_as_binary)):
        if int_and_frac_as_binary[i] == '.':
            index = i
    
    #Using a loop to check if the radix point needs to go left in oder to Normalize it
    for i in range(0, index):        
        if int_and_frac_as_binary[i] == '1':
            to_the_left = True
            int_and_frac_as_binary = int_part_as_binary[i] + '.' + int_part_as_binary[i+1:] + fractional_part_as_binary
            break
    
    #Accounting for cases where the radix point shifts to right 
    if to_the_left == False:
        for i in range(index, len(int_and_frac_as_binary)):          
            if int_and_frac_as_binary[i] == '1':
                #counting 0s to cover up the shift
                for j in range(0,i):
                    if int_and_frac_as_binary[j] == '0':
                        Zeros += 1 
                int_and_frac_as_binary = int_and_frac_as_binary[i] + '.' + int_and_frac_as_binary[i+1:] 
                break
    
    #determining the index after the number is in a normalized form
    for i in range(len(int_and_frac_as_binary)):
        if int_and_frac_as_binary[i] == '.':
            shifted_index = i
            
    #Determining the biased exponent value
    shifted_index+= Zeros
    exponent_before_127 = index - shifted_index
    exponent = 127 + exponent_before_127
    exponent_as_binary = int_to_binary_converter(exponent)
    

    #determining the sign bit
    if is_negative:
        sign = '1'
    else:
        sign = '0'
    
    #determining the mantissa
    
    #extracting the mantissa part
    for i in range(len(int_and_frac_as_binary) - 1):
        if int_and_frac_as_binary[i] == '.':
            mantissa += int_and_frac_as_binary[i+1:] 
    
    #ensuring that mantissa is 23 bits and padding 0s when necessary
    if len(mantissa) < 23:
        for i in range(len(mantissa), 23):
            mantissa += '0'
    
    #if there are more than 23 bit, plucking them out
    if len(mantissa) > 23:
        mantissa = mantissa[0:23]
    
    return sign + " "+ exponent_as_binary + " "+ mantissa
def convert_floating_point_number_to_real(String_arg):
    sign_value = 0
    exponent_val_as_string = ''
    exponent_val = 0
    mantissa_as_string = ''
    final_val = 0
    mantissa_converted = 0
    length = -1
    new_result = 0
    sign = String_arg[0]
 
    #determining the sign part
    
    if sign == '0':
        sign_value = 1
    elif sign == '1':
        sign_value = -1
        
    
    #determining the biased exponent
    for i in String_arg[1:9]:
        exponent_val_as_string+= i
    
    #converting the string exponent to decimal and subtracting 127 from it
    exponent_val= convert_to_base_10(exponent_val_as_string)
    exponent_val -= 127
    
    #determining the mantissa part
    mantissa_as_string = String_arg[9:]
    
    #converting every character to base 10 and multiplying it by the powers of -1...-23 in order 
    #to bring to a scientific notation
    for i in mantissa_as_string:
        new_result = convert_to_base_10(i) * power(2, length)  
        length -=1
        mantissa_converted+= new_result
    
    #Adding everything up  
    
    if mantissa_converted != 0:
        final_val = sign_value * ((1.0 + mantissa_converted) * power(2, exponent_val))
    
    
    return final_val
def convert_to_base_10 (int_as_string):
    #Declaring variables
    number_part = 0
    length = len(int_as_string)

    #Using a for loop to access every character in int_as_String
    for i in int_as_string:
        #obtaining the integer value of i (by subtracting it from the ordinal value of '0' as base)
        current_character =  ord(i) - 48 

        #if current_character's value is greater than 9 or less than 36 (10-36) then current_character is changed
        if current_character > 9 and current_character <= 36:
            current_character = (ord(i) - 65 ) + 10    

        #converting every character to base 10 and adding it a returnable integer
        number_part += current_character * (2 ** (length - 1))      
        length -= 1
    
    #returning the obtained integer
    return number_part
def float_to_int (float_num):
    #converting int_part into a valid int value
    new_int_part = 0
    #using a loop to increment new_int_part until it is equal to float_num
    while new_int_part <= float_num:
        new_int_part += 1
    
    #subtracting 1 from new_int_part to achieve an int
    new_int_part -= 1
    return new_int_part  
