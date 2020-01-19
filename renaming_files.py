# This script changes the name of the files of a directory in numerical order

#! python3

import os


def check_path(user_request):
    if os.path.isdir(user_request):
        return True
    else:
        return False


def main():
    print("Please introduce the path, if you run the script on the path itself just press ENTER")
    user_request = input()
    if user_request == "":
        user_request = os.getcwd()
        file_change(user_request)
    else:
        check_path(user_request)
        if check_path(user_request) is False:
            print("Invalid path, try again")
            main()
        file_change(user_request)


def file_change(user_request):
    i = 1
    files = os.listdir(user_request)
    for file in files:
        os.rename(os.path.join(user_request, file), os.path.join(user_request, str(i)))
        i = i+1


main()
