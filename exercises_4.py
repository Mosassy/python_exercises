__author__ = 'mosassy'

print 'Menu'
print '************************'
print "1. Write input to file"
print '2. Write input to screen'
print '3. Quit'
print '************************'

menu_choice = 0
while menu_choice not in [1, 2, 3]:
    menu_choice = int(raw_input("Enter choice from the menu(1-3):"))

if menu_choice == 1:
    f = open("felicia_file.txt", 'a+')
    user_input = raw_input("Enter your favorite phrase: ")
    f.write(user_input)
    f.close()

elif menu_choice == 2:
    user_input = raw_input("Enter your favorite phrase:")
    print user_input

elif menu_choice == 3:
    print 'file will close now'
    sys.exit()





