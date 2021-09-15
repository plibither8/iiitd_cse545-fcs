# Mihir Chaturvedi
# Roll number: 2019061

import importlib
import time

otp_a = importlib.import_module("2019061_2_a")
otp_b = importlib.import_module("2019061_2_b")


def main():
    start = time.time()
    for i in range(100):
        otp_a.main(False)
    end = time.time()
    elapsed = end - start
    print("Time elapsed: " + str(elapsed))

    start = time.time()
    for i in range(100):
        otp_b.main(False)
    end = time.time()
    elapsed = end - start
    print("Time elapsed: " + str(elapsed))

    random_number = otp_a.get_random_number()
    start = time.time()
    for i in range(100):
        print(otp_a.get_otp(random_number))
    end = time.time()
    elapsed = end - start
    print("Time elapsed: " + str(elapsed))


if __name__ == "__main__":
    main()
