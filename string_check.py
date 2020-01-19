#!/usr/bin/env python3

def main ():
    st = input()
    beg = (st.startswith("((("))
    end = (st.endswith(")))"))
    if beg is not True:
        print("Incorrect format, try again")
        main()
    elif end is not True:
        print("Incorrect format, try again")
        main()
    elif beg and end is True:
        print("String is correct")
main()


