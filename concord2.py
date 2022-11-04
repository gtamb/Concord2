
#!/usr/bin/env python3

import sys
import fileinput


# function that returns a list of exclusion words and the list of all words in each line
        # takes the current list of all lines, the current exclusion list, the current line, whether it is an exclusion word, and the line number
def get_words (line_list, exclusion_list,the_line, ex_flag, numlines):

        version = True
        #get rid of end of line
        the_line = the_line.strip()

        #the_line becomes a list
        the_line = the_line.split()

        #check if The_line is """"
        if numlines == 1 and the_line == ['1']:
                version = False;

        elif numlines == 2:
                return line_list, exclusion_list, ex_flag, version

        #check if The_line is """"
        elif the_line == ['""""']:
                # if it is the end of the exclusion words set ex_flag to false
                ex_flag = False

        elif ex_flag:
                #add to exclusion words list
                exclusion_list.append(the_line[0])

        else:
                # add the words in the line to
                line_list.append(the_line)


        return line_list, exclusion_list, ex_flag, version



#function that gets called to create a list of unique words for indexing
        # checks if the word in the line is an exclusion word and if not
        # whether it is unique
        # once through all the lines sorts then returns the list

def get_indexed_words(exclu_words, all_words):
        indexed_words = []


        # gets the line of words
        for any_line in all_words:

                # gets the word from each line
                for any_words in any_line:

                        # checks if both the lowercase version and original version of the word are not present in the exclusion word list
                        if any_words.lower() not in exclu_words and any_words not in exclu_words:


                                #if it is a valid word and unique then adds to indexed_words
                                in_indexed = False


                                for in_words in indexed_words:

                                        # check regardless of case if the word is already in indexed_words
                                        if any_words.lower() == in_words.lower():

                                                in_indexed = True
                                                break

                                if in_indexed == False:
                                        indexed_words.append(any_words)





        #sorts the finished list of indexed words
        indexed_words = sorted(indexed_words, key= str.lower)
        return indexed_words

# function that prints out the line with the indexed word and formats the left and right side of that word accordingly
        # takes the index of the word to capitalize and a list of all the words in the line
        # cuts off the the word on the left side of indexed word if it passes a length of 29 including 9 blank spaces
        # prints the capitalized version of the indexed word at position 30
        # cuts off the words on right side if the pass the 60 character total mark

def format_line(index, line):

        #the maximum length the left side of indexed word can be
        left_max_len = 20

        # get the max length the right line can be after the indexed word
        right_max_len = 31 - len(line[index])

        cur_left_len = 0
        left_string = ''

        # go through the words starting with the word to the left of the indexed word
        for left in reversed(line[:index]):

                # check if adding the next word and a space to the existing string will go out of bounds
                if (cur_left_len + len(left) + 1) <= left_max_len:
                        left_string = left + ' ' + left_string

                        cur_left_len = cur_left_len + len(left) + 1
                else:
                        # if it would be out of bounds, then no more words can be added
                        break

        # fill in blank space on left side
        # 9 charcter buffer

        left_string = 9*' ' +(left_max_len-cur_left_len)*' ' + left_string

        cur_right_len = 0
        right_string = ''

        #go through the words to right of indexed word
        for right in line[index +1:]:

                if (cur_right_len + len(right) + 1) <= right_max_len:

                        right_string = right_string + ' ' + right

                        cur_right_len = cur_right_len + len(right) + 1
                else:
                        break

        print(left_string + line[index].upper() + right_string)

# function that goes through each line checks if the unique word is there
        # takes the list of every line and the list of sorted indexed words as parameters
def print_lines(every_line, index_words):

        #go through each index word
        for i_word in index_words:

                # go through each line
                for one_line in every_line:

                        # go through each word in the line
                        for every_word in one_line:


                                # checks if the indexed word matches the word in the line regardless of case
                                if  i_word.lower() == every_word.lower():


                                        line_index = one_line.index(every_word)

                                        format_line(line_index, one_line)


def main():


        all_lines = []# list to hold list of words for each line
        ex_words = [] # list for exclusion words
        sorted_index_words = [] #list to hold all of the non-exclusion indexed words, with no repetition
        ex_or_not = True #exclusion word list flag
        vers_2 = True # whether the input file is version 2 or not
        line_num = 0

        # go through each line in the input file
        for line in fileinput.input():

                line_num += 1

                # get a list of the words for each line, a list of exclusion words,
                # the flag for whether the program should be adding to exclusion word list, and the version check
                all_lines, ex_words, ex_or_not, vers_2 = get_words(all_lines, ex_words,  line, ex_or_not, line_num)
                if vers_2 == False:
                        break


        if vers_2 == False :

                print("Input is version 1, concord2.py expected version 2")
        else:
                #get the sorted list of indexed words
                sorted_index_words = get_indexed_words(ex_words, all_lines)


                #call print_lines to print out lines by which index word they contain
                print_lines(all_lines, sorted_index_words)








if __name__ == "__main__":
        main()
                                                                                                                                             205,7-14      Bot
