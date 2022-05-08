# !/usr/bin/env python3
# Created by: Jedidiah
# Created on: May 05 2022

def temp_calc():
    try:
        temptc = int(input("enter the temperture in celsius: "))
        temptf = (9/5)*temptc+32
        print(" {}°C in fairenheit is {}°F".format(temptc, temptf))
    except ValueError:
        print("invalid input")


def main():

    temp_calc()


if __name__ == "__main__":
    main()
