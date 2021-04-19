#References
#https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/
#https://www.thecrazyprogrammer.com/2018/05/caesar-cipher-in-python.html
#https://inventwithpython.com/chapter14.html
#https://snakify.org/en/lessons/for_loop_range/
#https://stackoverflow.com/questions/6193498/pythonic-way-to-find-maximum-value-and-its-index-in-a-list
#https://inventwithpython.com/hacking/chapter20.html
import Frequency as FrequencyChecker                                                #### I struggled to get the idea of correlation, read many resources, worked on my own script, but eventually, I read and understood the following article and relied on the code in following article https://inventwithpython.com/hacking/chapter20.html, we imported it to be used in Bruteforce.
print('\n' + '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print('\n' + 'CAESAR CIPHER GENERATION TOOL - IGSR - 1404709 - Spring 2021')
print('\n' + '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
menu_string = '\n' + 'Please select the required operation:' + '\n' + \
                'MENU' + '\n' + \
                '----------------------------------------' + '\n' + \
                '1 Encrypt Plain Text with a Key' + '\n' + \
                '2 Decrypt Cipher Text with a key' + '\n' + \
                '3 Bruteforce Cipher Text' + '\n' + \
                '4 Exit' + '\n'                                                     #### tool menu
valid_options = ['1','2','3','4']                                                   #### (we have four operations with our tool)
KeyMAX=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25'] ## Max Shifts is 25 (total letters in english)
while True:
    while True:                                                                     #### Ensure interaction with Menu
        var = input('\n ...press enter to continue...')
        if not(var):
            print(menu_string)
            menu_input = input('Enter Menu Choice: ')
            break
        else:
            print('Press enter to continue')
    if menu_input in valid_options:
        if menu_input == '1':                                                         ####Triger Encryption Module
            PlainText=input('Enter The Plain Text:')                                  #### Enter Plaintext value
            Key = (input('Enter the Shifting value (1-25):'))                         #### Enter key value, you can type anything, but input checking will be at the next step
            if Key in KeyMAX:                                                         #### input validation, if true do the encryption
                Encryption = [chr((ord(i) + int(Key))) for i in PlainText]            #### Perform encryption using functions chr() & ord(), this two functions depends on ASCII table, this happens letter by letter, by adding the key value as shifting
                CipheredText=''.join(map(str,Encryption))                             #### the ciphered text is placed seperated, the join function allow to combine text in readable format
                print('Ciphered Text with key',Key,'is :',CipheredText)               #### print out the cipher text
            else:
                print('Key Value must be between 1 to 25, Please restart')            #### if you entered key that not in range of KeyMAX, this message will appear.
        if menu_input == '2':                                                         #### Triger decryption module
            CipheredText=input('Enter The Ciphered text:')                            #### enter ciphered text
            Key = (input('Enter the Shifting value (1-25):'))                         #### enter key value, same as line 33, the validation check occur.
            if Key in KeyMAX:                                                         #### input validation, if true do the decryption
                Decryption = [chr((ord(i) - int(Key))) for i in CipheredText]         #### Perform decryption, in this case we subtract using the given Key value.
                DecryptedText=''.join(map(str,Decryption))                            #### the deciphered text is placed seperated, the join function allow to combine text in readable format
                print('Plain Text with key',Key,'is :',DecryptedText)                 #### print out the plain text
            else:
                print('Key Value must be between 1 to 25, Please restart')            #### print out the cipher text
        if menu_input == '3':                                                         #### activate the bruteforcing module
            CipheredText=input('Enter The Ciphered text:')                            #### enter the ciphered value
            VALUES = []                                                               #### in following for loop, we will calculate the frequencies of most used letters in english, and add the coefficient values of each possible key 1-26, append in in this array.
            for x in KeyMAX:                                                          #### let's bruteforce with every possible value in KeyMAX
                BruteForce = [chr((ord(i) - int(x))) for i in CipheredText]           #### Bruteforce Function
                RecoveredText=''.join(map(str,BruteForce))                            #### the deciphered text is placed seperated, the join function allow to combine text in readable format
                Score = FrequencyChecker.englishFreqMatchScore(RecoveredText)         #### using the Frequency.py, englishFreqMatchScore function for the text, we get the score of possible decryption.
                VALUES.append(Score)                                                  #### append calculated score value in the VALUES array
            HighestFrequancyScore = max(VALUES)                                       #### determine what is the highest score calculated during bruteforce operation.
            CorrectKeyIndex = VALUES.index(HighestFrequancyScore)                     #### determine the index of the highest score in the array
            CorrectKeyValue = CorrectKeyIndex+1                                       #### add +1 to the index value, this because the array calculation starts with 0,1,2 - and as bruteforce run sequential, then score will be predictable by getting the index of value after adding 1.
            print('This Cipher Text is Encrypted with Key value of',CorrectKeyValue)  #### show the key used for encryption.
            Decryption = [chr((ord(i) - int(CorrectKeyValue))) for i in CipheredText] #### perform the decryption using the correct
            DecryptedText = ''.join(map(str, Decryption))                             #### the deciphered text is placed seperated, the join function allow to combine text in readable format
            print('--------------------------------------------------')
            print('Decrypted Text is:')
            print('--------------------------------------------------')
            print(DecryptedText)                                                     #### print out decryption result with key associated with highest score
            print('--------------------------------------------------')
        if menu_input == '4':                                                        #### exit the tool.
            print('\n' + 'Terminating the tool, Please close this window!' + '\n')
            break
    else:                                                                            #### if value other than 1,2,3,4 chosen, the following prompt will appear.
        print('\n' + 'INVALID MENU OPTION: Please try again' + '\n')
