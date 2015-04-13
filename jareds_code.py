__author__ = 'mosassy'
import time
import sys

SEPARATOR = "\n" + "*-"*20 + "*" + "\n"


def main_menu():
    print '\n'*10
    print SEPARATOR + \
          " EXERCISE 4 - MENU ".center(41, "*")\
          + SEPARATOR + "* 1. Write input to file\n* 2. Write input to screen" \
          "\n* 3. Quit" + SEPARATOR


def main():
    main_menu()
    choice = None
    while choice is None:
        user_input = raw_input("Enter your choice [1-3]: ")
        if user_input in ["1", "2", "3"]:
            choice = user_input
        else:
            print SEPARATOR + "* That doesn't seen to be valid input.  *" + SEPARATOR
            time.sleep(3)
            main_menu()

    if choice in ["1", "2"]:
        user_input = raw_input("Enter a phrase: ")
        if choice == "1":
            with open("output.txt", "a") as f:
                f.write("\n" + user_input)
            if not f.closed:
                print SEPARATOR + "* Done." + "\n* File will close on exit." + SEPARATOR
            else:
                print SEPARATOR + "* Done." + SEPARATOR
            time.sleep(5)
            main()

        else:
            user_input = user_input.replace('\n', '\n*')
            print SEPARATOR + "* You entered: '" + user_input + "'" + SEPARATOR
            time.sleep(5)
            main()
    else:
        print SEPARATOR + "* Exiting..." + SEPARATOR
        time.sleep(3)
        sys.exit(0)

if __name__ == '__main__': main()