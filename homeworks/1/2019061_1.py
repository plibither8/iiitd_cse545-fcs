# Mihir Chaturvedi
# Roll number: 2019061

import random

# Convert string to leet speak
def leet_speak(string):
    # Define leet_speak_dict
    leet_speak_dict = {
        "a": ["@", "4"],
        "b": ["8", "13"],
        "c": ["(", "{"],
        "d": ["|)", "|]"],
        "e": ["3"],
        "g": ["6"],
        "h": ["#"],
        "i": ["1", "!"],
        "k": ["|<", "|{"],
        "l": ["1", "|"],
        "o": ["0"],
        "s": ["5", "$"],
        "t": ["7"],
        "v": ["\\/", "\\/"],
        "x": ["*"],
        "z": ["2"],
        "0": ["o"],
        "1": ["l"],
        "2": ["z"],
        "3": ["e"],
        "4": ["a"],
        "5": ["s"],
        "6": ["g"],
        "7": ["t"],
        "8": ["b"],
        "9": ["g"],
    }

    leet_speak_string = ""

    for char in string:
        lower_char = char.lower()
        leet_speak_string += (
            random.choice(leet_speak_dict[lower_char] + [char])
            if lower_char in leet_speak_dict
            else char
        )

    return leet_speak_string


def main():
    input_string = input("Plaintext: ")

    # Check if string is longer than 100 characters
    if len(input_string) > 100:
        print("String is too long")
        return

    leet_string = leet_speak(input_string)

    print("Password: " + leet_string)


if __name__ == "__main__":
    main()
