def divide(dividend, divisor):
    return dividend / divisor


print("my_module.py:", __name__)

# -- importing from a folder --

import libs.my_lib

print("my_module.py:", __name__)