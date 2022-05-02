

# This function grabs and edits the data to become usable.
def file_grab():
    # This prompts the user to input a text file.
    file_request = input("Learning data file name: ")
    
    word_set = set()
    the_dictionary = {}
    # When the file opens, it will add words from the lines
    # and apply them to a set. Since it's a set, no repeats exist.
    with open(file_request) as file:
        lines = file.readlines()
        for line in lines:
            line = removal(line)
            # This helps handle reviews that lack words.
            if len(line) != 0:
                for i in range(1, len(line)):
                    word = line[i]
                    word_set.add(word)
                # This creates a dictionary key that will be later updated.
                for word in word_set:
                    the_dictionary[word] = 0.0
                    word_value = 0
                    word_count = 0
                # For every wrod that passes through, it'll collect...
                # How many times the word appears
                # What is the sum of all the values
                
                # It then divides the sum by the count and takes the result
                # and updates the dictionary's corresponding key.
                    for line in lines:
                        if word in line:
                            value = line[0]
                            word_value += int(value)
                            word_count += 1
                            final_score = word_value / word_count
                            the_dictionary[word] = final_score
    return(the_dictionary)

def removal(lines):
    # This does a loop to strip all of the punctuation,
    # if any of the elements in punctuation are found,
    # they are removed.
    for elements in lines:
            punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            if elements in punctuation:
                lines = lines.replace(elements, "")
    # then the line is lowered and split into a list.
    lines = lines.lower()
    lines = lines.split()
    return lines
    

def score_grab(file_data):


    word_valid = False
    is_value_right = False
    sentiment = None


    while word_valid == False:
        print()
        print("Menu Options")
        print("1: Return to menu.")
        print("2: Continue.")
        print()
        menu_request = input("What would you like to do? ")
        if int(menu_request) == 1:
            menu_loop(file_data)
        elif int(menu_request) == 2:
            word_request = input("What word would you like to see the score of? ")
            try:
                selected_word = file_data[word_request]
                # If the word has a rating of...
                # 2.01 or higher --> say its postive.
                # 1.99 or lower --> say its negative.
                # neither --> say its neutral.
                if selected_word >= 2.01:
                    sentiment = "positive."
                elif selected_word <= 1.99:
                    sentiment = "negative."
                else:
                    sentiment = "neutral."
                print(word_request, "is seen as {}".format(sentiment))
                print(word_request, "has a score of {}.".format(selected_word))
                # Asks if the sentiment is correct.
                value_query = input("Is this sentiment correct? (yes/no): ")
                # Checks if no, anything else does nothing.
                # If no, it'll ask to recorrect.
                if value_query == "no":
                    new_value = input("What should be the correct score? ")
                    # This ensures the number is within the rating limits of 0-4.
                    if float(new_value) <= 4.0:
                        if float(new_value) >= 0.0:
                            
                            final = float(new_value)
                            # Updates the word's value.
                            file_data[word_request] = final

                            print("That word's value has been changed to", final)
                        else:
                            print("Invalid number!")
                    else:
                        print("Invalid number!")
                    
            except:
                print("Invalid input. Try again.")
                word_valid = False


def average_score(file_data):
    
    menu_bool = False
    while menu_bool == False:
        print()
        print("Menu Options")
        print("1: Return to menu.")
        print("2: Continue.")
        print()
        menu_input = input("What would you like to do? ")
        try:
            if int(menu_input) == 1:
                menu_loop(file_data)
            if int(menu_input) == 2:
                dictionary_count = 0
                dictionary_value = 0
                # In this loop, we take all the values in the dictionary
                # and all the keys.

                # For every key, add 1.
                # For every value, add the value.
                for word in file_data:
                    dictionary_count += 1
                    dictionary_value += file_data[word]
                    # value/key = the true total average.
                    final_result = dictionary_value / dictionary_count
                print("The average score for the words are {}".format(final_result))
        except:
            print("Invalid input. Try again.")
            menu_bool = False

def high_low(file_data):
    menu_bool = False
    while menu_bool == False:
        print()
        print("Menu Options")
        print("1: Return to menu.")
        print("2: Continue.")
        print()
        menu_input = input("What would you like to do? ")
        try:
            if int(menu_input) == 1:
                menu_loop(file_data)
            if int(menu_input) == 2:
                # Convert the dictionary into a list
                dictionary = file_data
                dict_convert =list(dictionary.items())
                l=len(dict_convert)
                # Sort the list (because we can't sort a dictionary)
                # BUBBLE SORTING
                for i in range(l-1):
                    for j in range(i+1,l):
                        if dict_convert[i][1]>dict_convert[j][1]:
                            t=dict_convert[i]
                            dict_convert[i]=dict_convert[j]
                            dict_convert[j]=t
                    sorted_dict=dict(dict_convert)
                    # Using the sorted list, grab the first and last values
                    # Last is highest
                    h_word = dict_convert[-1][0]
                    h_score = dict_convert[-1][1]
                    # First is lowest.
                    l_word = dict_convert[0][0]
                    l_score = dict_convert[0][1]
                    # Print the results.
                print("The highest-rated word is '{}'.".format(h_word))
                print("with a score of {}".format(h_score))
                print("The lowest-rated word is '{}'.".format(l_word))
                print("with a score of {}".format(l_score))
                
        except:
            print("Invalid input. Try again.")
            menu_bool = False

def file_writer(file_data):
    menu_bool = False
    while menu_bool == False:
        print()
        print("Menu Options")
        print("1: Return to menu.")
        print("2: Continue.")
        print()
        menu_input = input("What would you like to do? ")
        if int(menu_input) == 1:
            menu_loop(file_data)
        if int(menu_input) == 2:
            # This creates two files, positive and negative.
            # If the files already exist, they'll just write
            # Using the pre-existing files.
            positive_out = open("positive.txt", "a")
            negative_out = open("negative.txt", "a")
            print("File write in progress.")
            print("Please be patient.")
            for word in file_data:
                # If the word meets the positive rating, it'll be sent
                # to the positive file.
                if file_data[word] >= 2.01:
                    positive_out.write(word + "\n")
                    print("\n")
                # Same applies, but for negative words.
                # All neutrals are sent nowhere.
                elif file_data[word] <= 1.99:
                    negative_out.write(str(word + "\n"))
                    print("\n")
            print("File write complete.")
            positive_out.close()
            negative_out.close()
                
                

def menu_loop(file_data):
    menu_choice = False
    while menu_choice == False:
            print()
            print("What would you like to do?")
            print("1: Get the score of a word")
            print("2: Get the average score of words in a file")
            print("3: Find the highest / lowest scoring words in a file")
            print("4: Sort the words into positive.txt and negative.txt")
            print("5: Exit the program")
            decision = input("Enter a number 1 - 5: ")

            # Sends the user to different functions based on input.
            if decision == "1":
                menu_choice = True
                score_grab(file_data)
            elif decision == "2":
                menu_choice = True
                average_score(file_data)
            elif decision == "3":
                menu_choice = True
                high_low(file_data)
            elif decision == "4":
                menu_choice = True
                file_writer(file_data)
                menu_choice = True
            elif decision == "5":
                quit()
            # If the input doesn't match, it's invalid.
            else:
                print("Invalid input.")
                menu_choice = False
    


    


            
    
def main():
    # Grab the data, send it to the menu loop for further use.
    file_data = file_grab()
    menu_loop(file_data)
main()
