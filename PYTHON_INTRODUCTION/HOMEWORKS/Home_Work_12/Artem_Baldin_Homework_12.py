import string
import random
import zipfile
import datetime


def extract_archive(file_to_open, password):
    try:
        file_to_open.extractall(pwd=password.encode())
        return True
    except Exception:  # as e:
        #   print(e)
        return False


def hack_archive(file_name):
    file_to_open = zipfile.ZipFile(file_name)
    wrong_passwords = set()
    tries = 0
    print("Looking for the digits combination.\n")
    start_time = datetime.datetime.now()
    while True:
        password = "".join(random.choices(string.digits, k=PASSWORD_LENGTH))

        if password in wrong_passwords:
            continue
        elif extract_archive(file_to_open, password) is True:
            end_time = datetime.datetime.now()
            print(f"File: {file_name} is extracted by default path.\n")
            print(f'Archive {file_name} is hacked. Password - {password}')
            print(f'Password was found after {tries} tries')
            print(f"Elapsed time: {end_time - start_time}")
            break
        if tries > 0 and tries % 2000 == 0:
            print("Still working.\n")
        wrong_passwords.add(password)
        tries += 1


PASSWORD_LENGTH = 4
filename = 'archive.zip'

hack_archive(filename)
