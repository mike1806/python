'''try:
    f = open('testfile', 'r')
    f.write('Write a test line')
except TypeError:
    print("there was an error")
except OSError:
    print("OSE error")
finally:
    print("I always run")
'''

def ask_for_int():
    while True:
        try:
            result = int(input("Please provide a number: "))
        except:
            print("this is a number!!!")
            continue
        else:
            print("Yes, go away thats a integer!")
            break
        finally:
            print("End of try/except/finally!")



ask_for_int()
