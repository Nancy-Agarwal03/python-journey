try:
    x = int(input("enter x: "))
    ans = 10/x

except ZeroDivisionError:
    print(f"divide by 0 not allowed")

except ValueError:
    print(f"invalid input")

else:
    print(f"ans = {ans}")

finally:
    print ("end of program")
    