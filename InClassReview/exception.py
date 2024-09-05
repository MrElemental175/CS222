def main():
    midterm = [70,92,100]
    try:
        print(midterm)
    except:
        print("Something went wrong")
    x = 0
    try:
        z = 10/x
    except ZeroDivisionError:
        print("You're diving by zero")
    except NameError:
        print("Name error")
    else:
        print("ALL GOOOOOOD")

main()