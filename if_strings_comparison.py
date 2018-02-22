
a = input("Enter a word.")
b = input("Enter another word.")

if len(str(a)) == len(str(b)):
    print('1')
elif len(str(a)) > len(str(b)):
    print('2')

if len(str(a)) < len(str(b)):
    if b == "learn":
        print('3')
    else:
    	print('2.5')