'''
    This function takes the list of string or an array and
    determines if the characters in the string s can be
    permuted to form a palindrome in O(N) algorithm
'''


def isPalindomicPermutation(s):
    '''new dictionary'''
    new_dict = {}

    '''if the list has only one or no characters then
    it is palindrome'''
    if len(s) < 2:
        return True

    '''iterating through the list'''
    for i in s:
        '''pushing if the key is unique or else popping'''
        if i not in new_dict:
            new_dict.update({i: 1})
        else:
            new_dict.pop(i)
    '''if everything is popped out or only one is left, 
    returning true or else false'''
    if len(new_dict) > 1:
        return False
    else:
        return True

