import random
import string

# default settings of script
settings = {
    "lower": True,
    "upper": True,
    "symbol": True,
    "number": True,
    "space": True,
    "length": 8,
}

PASS_MIN_LENGTH = 6
PASS_MAX_LENGTH = 60


# get length of password from user
def get_user_password_length(option, default, pass_min_length=PASS_MIN_LENGTH, pass_max_length=PASS_MAX_LENGTH):
    while True:
        user_input = input(f"Enter password length. (default is {default}) : ")
        if user_input == '':
            return default

        if user_input.isdigit():
            user_input_length = int(user_input)
            if pass_min_length <= user_input_length <= pass_max_length:
                return int(user_input)
            print("Invalid input.")
            print("Password length should be between 6 and 50.")
        else:
            print("Invalid input. You have to enter a positive number.")
        print("Please try again.")


# get settings from user
def get_yes_or_no_for_settings(option, default):
    while True:
        user_input = input(f"Include {option}?"
                           f"(Default is {default}) (y: yes, n: no) :")

        if user_input == "":
            return default
        if user_input in ["y", "n"]:
            return user_input == "y"
        print("Invalid input. Please try again.")


# this function give get_yes_or_no_for_settings and get get_user_password_length and replace them to settings.
def get_settings_from_user(setting):
    for option, default in setting.items():
        if option != "length":
            user_choice = get_yes_or_no_for_settings(option, default)
            setting[option] = user_choice
        elif option == "length":
            user_password_length = get_user_password_length(option, default)
            setting["length"] = user_password_length


def ask_if_change_settings(setting):
    while True:
        user_answer = input("Do you want change default settings? (y, n or click enter)")

        if user_answer in ["y", "n", ""]:
            if user_answer in ["y", ""]:
                print("-"*5, "Change Settings", "-"*5, sep="")
                get_settings_from_user(settings)
            break
        else:
            print("Invalid input.")
            print("Please try again.")


def generate_upper_case():
    return random.choice(string.ascii_uppercase)


def generate_lower_case():
    return random.choice(string.ascii_lowercase)


def generate_number_char():
    return random.choice(string.digits)


def generate_symbol_char():
    return random.choice(string.punctuation)


def generate_random_char(setting_choices):
    choice = random.choice(setting_choices)

    if choice == "upper":
        return generate_upper_case()
    elif choice == "lower":
        return generate_lower_case()
    elif choice == "symbol":
        return generate_symbol_char()
    elif choice == "number":
        return generate_number_char()
    elif choice == "space":
        return " "


def password_generator(setting):
    final_password = ""
    password_length = settings["length"]

    setting_choices = list(filter(lambda x: setting[x], ["upper", "lower", "symbol", "number", "space"]))

    for i in range(password_length):
        final_password += generate_random_char(setting_choices)

    return final_password


def password_generator_loop(setting):
    while True:
        print("-" * 20)
        print(f"Generated Password: {password_generator(settings)}")
        while True:
            another_password = input("Do you want another password? ")
            if another_password in ["y", "n", ""]:
                if another_password == "n":
                    return
                break
            else:
                print("Invalid input. Please choose from (y, n or enter).")
                print("Please try again.")


def run():
    ask_if_change_settings(settings)
    password_generator_loop(settings)
    print("Thanks for using scripts.")


run()
