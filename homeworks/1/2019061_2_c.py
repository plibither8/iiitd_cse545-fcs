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
    print("A. Time elapsed: " + str(elapsed))

    start = time.time()
    for i in range(100):
        otp_b.main(False)
    end = time.time()
    elapsed = end - start
    print("B. Time elapsed: " + str(elapsed))

    random_number = otp_a.get_random_number()
    start = time.time()
    otps = []
    for i in range(100):
        otp = otp_a.get_otp(random_number)
        while otp in otps:
            otp = otp_a.get_otp(random_number)
        otps.append(otp)
    end = time.time()
    elapsed = end - start
    print("C. Time elapsed: " + str(elapsed))
    for otp in otps:
        print(otp)


if __name__ == "__main__":
    main()
