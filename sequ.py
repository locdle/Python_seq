##check how many input users have type in command line
##make the function count input separate by space
def countInput(user_input):
    if len(user_input) == 0 :
        return 0
    count = 0
    for index in range (len(user_input)):
        if user_input[index] == ' ':
            count +=1
    if count == 0:
        return 1
    else:
        return count + 1

## take the operand input from users
def getOperand(user_input):
    for index in range(len(user_input)):
        if user_input[index] == ' ':
            operand = user_input[:index]
            break
    return operand

## get the last operand input from users
def getLastOperand(user_input):
    operand = user_input[len(getOperand(user_input))+1:]
    return operand

def isFloatNumber(user_input):
    for index in range(len(str(user_input))):
        if str(user_input)[index] == '.' :
            return True
    return False

##get length of number of float before dot
def getLengthPrefix(number):
    if isFloatNumber(number) == True:
        for index in range(len(str(number))):
            if str(number)[index] == '.':
                return index
    else:
        return len(str(number))
    return
                                
##get length of number of float after dot
def getLengthPostfix(number):
    if isFloatNumber(number) == True:
        return len(str(number)) - getLengthPrefix(number) -1
    return 0

##check type of value
def typeOfValue(text):
    try:
        int(text)
        return int
    except ValueError:
        pass

    try:
        float(text)
        return float
    except ValueError:
        pass

    return str

def getSymbol(text):
    if text[:2] == '-s':
       symbol = text[2:]
    elif text[:10] == '--separate':
        symbol = text[10:]
    return symbol

def getPad(text):
    if text[:2] == '-p':
       pad = text[2:]
    elif text[:5] == '--pad':
        pad = text[5:]
    return pad

def printVersion():
    version_file = open('version.txt', 'r')
    print(version_file.read())
    version_file.close()
    return

def printHelp():
    help_file = open('help.txt', 'r')
    print(help_file.read())
    help_file.close()
    return

####################################################################################################
##### make traditional sequence ####################################################################
####################################################################################################

def makeSequenceWithOneNum(number):
    try:
        decimal_number = number - int(number)
        if(number >= 1):
            for index in range(1, int(number) + 1):
                if(index + decimal_number <= number):
                    print(index)
        else:
            print("Invalid input")
    except ValueError:
        print("Invalid input %s" %number)
    return

def makeSequenceWithTwoNum(first_num, last_num):
    try:
        decimal = first_num - int(first_num)
        num_of_decimal = getLengthPostfix(first_num)
        if (last_num > first_num):
            for index in range(int(first_num), int(last_num)+1):
                if(index + decimal <= last_num):
                    result = round(index + decimal, num_of_decimal)
                    print(result)
        elif (last_num == first_num):
            print(first_num)
        else:
            print("First number %s is bigger than last number %s" %(first_num, last_num))
    except ValueError:
        print("Invalid input %s and %s" %(first_num, last_num))
    except TypeError:
        print("Invalid input %s and %s" %(first_num, last_num))

def makeSequenceWithThreeNum(first_num, increment, last_num):
    try:
        decimal = first_num - int(first_num)
        num_of_decimal = getLengthPostfix(first_num)
        if (last_num > first_num):
            print(first_num)
            index = first_num + increment
            while(index + decimal <= last_num):
                result = round(index + decimal, num_of_decimal)
                print(result)
                index += increment
        elif (last_num == first_num):
            print(first_num)
        else:
            print("First number %s is bigger than last number %s" %(first_num, last_num))
    except ValueError:
        print("Invalid input %s and %s" %(first_num, last_num))
    except TypeError:
        print("Invalid input %s and %s" %(first_num, last_num))
        


####################################################################################################
##### make the sequence with feature format ########################################################
####################################################################################################

def makeSequenceFormatWithOneNum(format_type, number ):
    try:
        if number >= 1:
            for index in range(1,int(number)+1):
                print(format_type % index)
    except  ValueError:
        print("unsupport this type of format %s" %format_type)
    return

def makeSequenceFormatWithTwoNum(format_type, first_num, last_num):
    try:
        decimal_number = first_num - int(first_num)    
        if last_num > first_num:
            for index in range(int(first_num), int(last_num)+1):
                result = index + decimal_number
                print(format_type % result)
        elif last_num == first_num:
            print(format_type % first_num)
    except  ValueError:
        print("unsupport this type of format %s" %format_type)
    except TypeError:
        print("Invalid input %s and %s" %(first_num, last_num))
    return

def makeSequenceFormatWithThreeNum(format_type, first_num, increment, last_num):
    try:
        if last_num > first_num:
            print(format_type % first_num)
            result = first_num + increment
            while (result + increment < last_num):
                print(format_type % result)
                result += increment
        elif last_num == first_num:
            print(format_type % first_num)
    except  ValueError:
        print("unsupport this type of format %s" %format_type)
    except TypeError:
        print("Invalid input %s, %s, and %s" %(first_num, increment, last_num))
    return

####################################################################################################
##### make the sequence with feature separator #####################################################
####################################################################################################

def changeBackSlash(text):
    backN = text.replace('\\n','\n')
    backT = backN.replace('\\t', '\t')
    backA = backT.replace('\\a','\a')
    backF = backA.replace('\\f','\f')
    backR = backF.replace('\\r','\r')
    backV = backR.replace('\\v','\v')
    backSlash = backV.replace('\\\\','\\')
    return text

def makeSequenceSeparatorWithOneNum(symbol, number):
    try:
        output = ''
        symbol = changeBackSlash(symbol)
        decimal_number = number - int(number)
        if(number >= 1):
            for index in range(1, int(number)+1):
                output += str(index)
                if(index + decimal_number< number):
                    output += symbol
            print(output)
    except TypeError:
        print("Invalid input %s and %s" %(symbol, number))
    except ValueError:
        print("Invalid input %s and %s" %(symbol, number))
    return

def makeSequenceSeparatorWithTwoNum(symbol, first_num, last_num):
    try:
        decimal_number = first_num - int(first_num)
        num_of_decimal = getLengthPostfix(first_num)
        output = ''
        symbol = changeBackSlash(symbol)
        if last_num > first_num:
            for index in range(int(first_num), int(last_num)+1):
                result = round(index + decimal_number, num_of_decimal)
                if(result <= last_num):
                    output += str(result)
                    if(index + decimal_number + 1 <= last_num):
                        output += symbol
            print(output)
    except TypeError:
        print("Invalid input %s, %s, and %s" %(symbol, first_num, last_num))
    except ValueError:
        print("Invalid input %s, %s, and %s" %(symbol, first_num, last_num))
    return

def makeSequenceSeparatorWithThreeNum(symbol, first_num, increment, last_num):
    try:
        decimal_number = first_num - int(first_num)
        num_of_decimal = getLengthPostfix(first_num)
        output = ''
        symbol = changeBackSlash(symbol)
        if last_num > first_num:
            result = first_num
            output = str(first_num) + symbol
            while(result + increment <= last_num):
                result += increment
                output += str(result)
                if(result + increment <last_num):
                    output += symbol
            print(output)
        elif last_num == first_num:
            print(first_num)
    except TypeError:
        print("Invalid input %s, %s, %s, and %s" %(symbol, first_num, increment, last_num))
    except ValueError:
        print("Invalid input %s, %s, %s, and %s" %(symbol, first_num, increment, last_num))
    return     

####################################################################################################
##### make the sequence with feature equal width ###################################################
####################################################################################################

def makeSequenceEqualWidthOneNum(number):
    try:
        length = len(str(int(number)))
        decimal_number = number - int(number)
        if number >= 1:
            for index in range(1, int(number) + 1):
                if index + decimal_number < number +1:
                    print(('{:0%s}' % length).format(index))
    except TypeError:
        print("Invalid input %s" %number)
    except ValueError:
        print("Invalid input %s" %number)
    return

def makeSequenceEqualWidthTwoNum(first_num, last_num):
    try:
        decimal_number = first_num - int(first_num)
        num_of_decimal = getLengthPostfix(first_num)
        if num_of_decimal == 0:
            max_length = max(getLengthPrefix(first_num), getLengthPrefix(last_num))
        else:
            max_length = max(getLengthPrefix(first_num), getLengthPrefix(last_num)) + num_of_decimal + 1
                             
        if last_num > first_num:
            for index in range(int(first_num), int(last_num) + 1):
                if (index + decimal_number <= last_num):
                    result = round(index + decimal_number, num_of_decimal)
                    print(('{:0%s}' % max_length).format(result))
        elif last_num == first_num:
            print(('{:0%s}' % max_length).format(first_num))
    except TypeError:
        print("Invalid input %s and %s" %(first_num, last_num))
    except ValueError:
        print("Invalid input %s and %s" %(first_num, last_num))
    return

def makeSequenceEqualWidthThreeNum(first_num, increment, last_num):
    try:
        decimal_number = first_num - int(first_num)
        num_of_decimal = getLengthPostfix(first_num)
        if num_of_decimal == 0:
            max_length = max(getLengthPrefix(first_num), getLengthPrefix(last_num))
        else:
            max_length = max(getLengthPrefix(first_num), getLengthPrefix(last_num)) + num_of_decimal + 1
        result = first_num
        if last_num > first_num:
            while(result <= last_num):
                print(('{:0%s}' % max_length).format(result))
                result += increment
                result = round(result, num_of_decimal)
        elif last_num == first_num:
            print(('{:0%s}' % max_length).format(first_num))
    except TypeError:
        print("Invalid input %s, %s, and %s" %(first_num, last_num))
    except ValueError:
        print("Invalid input %s, %s, and %s" %(first_num, last_num))
    return

####################################################################################################
##### make the sequence with feature words #########################################################
####################################################################################################

def makeSequenceWordsWithOneWord(word):
    space = ' '
    output = ''
    length = len(word)
    if length < 1:
        print("Please enter the input!")
    else:
        for index in range(length):
            output += word[index]
            if(index < length):
                output += space
        print(output)
    return

def makeSequenceWordsWithTwoWords(first_word, second_word):
    space = ' '
    output = ''
    length_of_first_word = len(first_word)
    length_of_second_word = len(second_word)
    if length_of_first_word < 1 or length_of_second_word < 1:
        print("Please enter the input!")
    else:
        for index_of_first_word in range(length_of_first_word):
            output += first_word[index_of_first_word]
            output += space

        for index_of_second_word in range(length_of_second_word):
            output += second_word[index_of_second_word]
            if(index_of_second_word < length_of_second_word):
                output += space
        print(output)
    return

####################################################################################################
##### make the sequence with feature pad ###########################################################
####################################################################################################

def makeSequencePadWithOneNum(pad, number):
    if len(pad) == 1 and number >= 1:
        maxLength = len(str(int(number)))
        for index in range(1, int(number) + 1):
            if len(str(index)) < maxLength:
                fill_missing_path = maxLength - len(str(index))
                print(pad * fill_missing_path + str(index))
            else:
                print(index)
    return

def makeSequencePadWithTwoNum(pad, first_num, last_num):
    try:
        pad = changeBackSlash(pad)
        decimal = first_num - int(first_num)
        num_of_decimal = getLengthPostfix(first_num)
        max_length_prefix = max(getLengthPrefix(first_num), getLengthPrefix(last_num))
        if len(pad) == 1 and last_num > first_num:
            for index in range(int(first_num), int(last_num) + 1):
                index = round(index +decimal , num_of_decimal)
                if (index <= last_num):
                    if getLengthPrefix(index) < max_length_prefix:
                        fill_missing_path = max_length_prefix - getLengthPrefix(index)
                        print(pad * fill_missing_path + str(index))
                    else:
                        print(index)
    except TypeError:
        print("Invalid input %s, %s, and %s" %(pad, first_num, last_num))
    except ValueError:
        print("Invalid input %s, %s, and %s" %(pad, first_num, last_num))
    return

def makeSequencePadWithThreeNum(pad, first_num, increment, last_num):
    try:
        pad = changeBackSlash(pad)
        decimal = first_num - int(first_num)
        num_of_decimal = max(getLengthPostfix(first_num), getLengthPostfix(increment))
        max_length_prefix = max(getLengthPrefix(first_num), getLengthPrefix(last_num))
        if last_num > first_num:
            index = first_num
            while (index + decimal <= last_num):
                index = round(index , num_of_decimal)
                fill_missing_path = max_length_prefix - getLengthPrefix(index)
                if getLengthPrefix(index) < max_length_prefix:
                    print(pad * fill_missing_path + str(index))
                else:
                    print(index)                
                index += increment
    except TypeError:
        print("Invalid input %s, %s, %s, and %s" %(pad, first_num, increment, last_num))
    except ValueError:
        print("Invalid input %s, %s, %s, and %s" %(pad, first_num, increment,last_num))
    return

####################################################################################################

def makeSequence(user_input):
    if countInput(user_input) == 1:
        operand1 = user_input
        if operand1 == '-v' or operand1 == '--version':
            printVersion()
        elif operand1 == '-h' or operand1 == '--help':
            printHelp()
        else:
            makeSequenceWithOneNum(typeOfValue(operand1)(operand1))

    elif countInput(user_input) == 2:
        operand1 = getOperand(user_input)
        operand2 = getLastOperand(user_input)
        if operand1[:2] == '-s' or operand1[:10] == '--separate' :
            makeSequenceSeparatorWithOneNum(getSymbol(operand1), typeOfValue(operand2)(operand2))
        elif operand1 == '-w' or operand1 == '--equal-width':
            makeSequenceEqualWidthOneNum(typeOfValue(operand2)(operand2))
        elif operand1 == '-W' or operand1 == '--words':
           makeSequenceWordsWithOneWord(operand2)
        elif operand1[:2] == '-p' or operand1[:5] == '--pad' :
            makeSequencePadWithOneNum(getPad(operand1), typeOfValue(operand2)(operand2))
        elif operand1 == '-P' or operand1 == '--pad-spaces':
            makeSequencePadWithOneNum(' ', typeOfValue(operand2)(operand2))
        else:
            makeSequenceWithTwoNum(typeOfValue(operand1)(operand1), typeOfValue(operand2)(operand2))

    elif countInput(user_input) == 3:
        operand1 = getOperand(user_input)
        operand2 = getOperand(user_input[len(operand1)+1:])
        operand3 = getLastOperand(user_input[len(operand1)+1:])
        if operand1 == '-f' or operand1 == '--format':
            makeSequenceFormatWithOneNum(operand2, typeOfValue(operand3)(operand3))
        elif operand1[:2] == '-s' or operand1[:10] == '--separate' :
            makeSequenceSeparatorWithTwoNum(getSymbol(operand1), typeOfValue(operand2)(operand2), typeOfValue(operand3)(operand3))
        elif operand1 == '-w' or operand1 == '--equal-width':
            makeSequenceEqualWidthTwoNum(typeOfValue(operand2)(operand2), typeOfValue(operand3)(operand3))
        elif operand1 == '-W' or operand1 == '--words':
           makeSequenceWordsWithTwoWords(operand2, operand3)
        elif operand1[:2] == '-p' or operand1[:5] == '--pad' :
            makeSequencePadWithTwoNum(getPad(operand1), typeOfValue(operand2)(operand2), typeOfValue(operand3)(operand3))
        elif operand1 == '-P' or operand1 == '--pad-spaces':
            makeSequencePadWithTwoNum(' ', typeOfValue(operand2)(operand2), typeOfValue(operand3)(operand3))            
        else:
            makeSequenceWithThreeNum(typeOfValue(operand1)(operand1), typeOfValue(operand2)(operand2),
                                   typeOfValue(operand3)(operand3))
            
    elif countInput(user_input) == 4:
        operand1 = getOperand(user_input)
        operand2 = getOperand(user_input[len(operand1)+1:])
        operand3 = getOperand(user_input[len(operand1)+len(operand2)+2:])
        operand4 = getLastOperand(user_input[len(operand1)+len(operand2)+2:])
        if operand1 == '-f' or operand1 == '--format':
            makeSequenceFormatWithTwoNum(operand2, typeOfValue(operand3)(operand3), typeOfValue(operand4)(operand4))
        elif operand1[:2] == '-s' or operand1[:10] == '--separate' :   
            makeSequenceSeparatorWithThreeNum(getSymbol(operand1), typeOfValue(operand2)(operand2),
                                              typeOfValue(operand3)(operand3), typeOfValue(operand4)(operand4))
        elif operand1 == '-w' or operand1 == '--equal-width':
            makeSequenceEqualWidthThreeNum(typeOfValue(operand2)(operand2), typeOfValue(operand3)(operand3),
                                         typeOfValue(operand4)(operand4))
        elif operand1[:2] == '-p' or operand1[:5] == '--pad' :
            makeSequencePadWithThreeNum(getPad(operand1), typeOfValue(operand2)(operand2),
                                        typeOfValue(operand3)(operand3), typeOfValue(operand4)(operand4))
        elif operand1 == '-P' or operand1 == '--pad-spaces':
            makeSequencePadWithThreeNum(' ', typeOfValue(operand2)(operand2), typeOfValue(operand3)(operand3),
                                        typeOfValue(operand4)(operand4))


    elif countInput(user_input) == 5:
        operand1 = getOperand(user_input)
        operand2 = getOperand(user_input[len(operand1)+1:])
        operand3 = getOperand(user_input[len(operand1)+len(operand2)+2:])
        operand4 = getOperand(user_input[len(operand1)+len(operand2)+len(operand3)+3:])
        operand5 = getLastOperand(user_input[len(operand1)+len(operand2)+len(operand3)+3:])
        if operand1 == '-f' or operand1 == '--format':
            makeSequenceFormatWithThreeNum(operand2, typeOfValue(operand3)(operand3),
                                           typeOfValue(operand4)(operand4), typeOfValue(operand5)(operand5))

    return

def main():
    running = True
    while(running == True):
        user_input = input("Enter numbers separate by space: ")
        makeSequence(user_input)
        user_repeat_to_run = input("Do you want to re-run program: ")

        if(user_repeat_to_run.upper() == 'Y' or
           user_repeat_to_run.upper() == "YES"):
                running = True
        else:
            running = False

    return
    
    
main()                                
