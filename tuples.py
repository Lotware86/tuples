# Author: Bosco Lo
# Program Description: Tuples and displaying them line by line
# Date: 20 September 2020

celebrity_tuple = ('John', 'Wayne', 'True Grit', 1969, 'Actor', '1907–1979')

# create tuples of two, two by two with no re-use (pairing correctly)
celebrity_tuple = zip(*([iter(celebrity_tuple)] * 2))


# print the paired tuples in separate lines,
# include counting each line, using updated python3.x format to add leading zeroes to line counter
def simple_print_listed_tuples(tpl):
    counter = 0
    for i, j in tpl:
        counter += 1
        print(''.join(['Line ' + f'{counter + 0:03}' + ' in sample: ']), i, j, end='\n')


simple_print_listed_tuples(celebrity_tuple)
