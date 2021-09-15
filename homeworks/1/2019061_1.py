# Mihir Chaturvedi
# Roll number: 2019061

# Convert string to leet speak
def leet_speak(string):
    # Define leet_speak_dict
    leet_speak_dict = {
        "a": "@",
        "b": "8",
        "e": "3",
        "g": "6",
        "i": "1",
        "l": "1",
        "o": "0",
        "s": "5",
        "t": "7",
        "z": "2",
    }

    leet_speak_string = ""

    for i in range(len(string)):
        lower_case_letter = string[i].lower()
        leet_speak_string += (
            leet_speak_dict[lower_case_letter]
            if lower_case_letter in leet_speak_dict
            else string[i]
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
