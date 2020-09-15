# Change your preferred configuration here.
#        |  |
#        |  |
#        |  |
#      \      /
#       \    /
#        \  /
#         \/

# ===== PERSONAL INFORMATION =====
STUDENT_ID = '630510xxx'
NAME = 'Steve Jobs'
SECTION = '00x'

# ===== CODE PREFERENCES =====
TAB_WIDTH = 4            # How many spaces per tab you want in your code.
INCLUDE_MAIN = True      # If you don't need `main()` function, set to False.

# Note: If you set `INCLUDE_MAIN` to False, setting `TAB_WIDTH` is unnecessary.

###############################################################################
# So now, just sit and let the program run for you. However, the program will
# ask you a little more detail about the files. So if you don't wish to answer,
# you can always change later.
###############################################################################

# Read the week number of the lab files (e.g. read '08' in Lab08).
# Then assign to `LAB_NO`.
LAB_NO = input('Input the Lab no. (e.g. 08, 11)\n===> ')

# Read the number of files (assignments) users prefer.
# Then assign to `NO_OF_FILES`.
NO_OF_FILES = int(input('Input the amount of assignments\n===> '))

# Read the assignment number prefix (if any).
# If none, just left blank.
# Then assign to `LAB_NO_PREFIX`.
LAB_NO_PREFIX = input('Input the Lab no. prefix (e.g. EX in EX1).\nIf none, just leave it blank:\n===>')

# Prepare the lines of the top information that appears to every assignment
# files.
# Assign to `to_be_written_1`
to_be_written_1 = [
        '# ' + STUDENT_ID + '\n',
        '# ' + NAME + '\n',
        '# ' + SECTION + '\n',
        '# Lab%s_%sx\n' % (LAB_NO, LAB_NO_PREFIX),
        '\n',
        '\n',
        '\n'      # In case of any functions might be needed.
];

# Prepare the lines of the main part of the program that appears to most of the
# assignment files.
# Assign to `to_be_written_2`.
to_be_written_2 = [
        '# Driver Code\n',
        'def main():\n',
        ' '*TAB_WIDTH + '\n',
        '\n',
        '# File Execution\n',
        'if __name__ == \'__main__\': \n',
        ' '*TAB_WIDTH + 'main()'
];

# Repeat for every integer `n` in the range of [1, `NO_OF_FILES`].
for n in range(1, NO_OF_FILES + 1):

    # Create a file instance of the current `n`-th file, with a write mode, and
    # encode in UTF-8, the universal, commonly used worldwide encoding format.
    # given the name `file_ins`, using with statement.
    with open('Lab%s_%s%d_%s.py' % (
             LAB_NO,
             LAB_NO_PREFIX,
             n,
             STUDENT_ID), 'w', encoding='utf8') as file_ins:

        # Add the lab file information to `to_be_written_1`.
        to_be_written_1[3] = '# Lab%s_%s%d\n' % (LAB_NO, LAB_NO_PREFIX, n)

        # Write the `n`-th file.
        file_ins.writelines(to_be_written_1)
        if INCLUDE_MAIN:        # In case you want the main function.
            file_ins.writelines(to_be_written_2)


