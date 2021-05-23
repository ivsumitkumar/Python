from random_password_creator import Password
import argparse


args = argparse.ArgumentParser()
args.add_argument('-c','--charset', required=True)
args.add_argument('-l','--length', default=9)
options = args.parse_args()
print(options.charset)
print(options.length)

password = Password(options.charset, int(options.length))
password.set_the_charset()
password.generate_password()
print("Password is: ",password.get_password())
