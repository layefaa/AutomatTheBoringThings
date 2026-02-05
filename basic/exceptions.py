try:
    f = open('just.txt')
except FileNotFoundError:
     print("Something went wrong!")
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("This always runs.")