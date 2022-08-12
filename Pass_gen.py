# generate password which is tough to  break it

import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "@#$%&*/\?"

use_for = lower_case + upper_case + number + symbol
length_for_pass = 9
password = ''.join(random.sample(use_for,length_for_pass))

print("Your Password Is :-- ", password)

