import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):

    random_list = []
    generated_id = ""
    small_letters = string.ascii_lowercase
    capital_letters = string.ascii_uppercase
    digits = string.digits

    for i in range(number_of_capital_letters):
        random_index = random.randint(0, len(capital_letters) - 1)
        random_list.append(capital_letters[random_index])

    for i in range(number_of_small_letters):
        random_index = random.randint(0, len(small_letters) - 1)
        random_list.append(small_letters[random_index])

    for i in range(number_of_digits):
        random_index = random.randint(0, len(digits) - 1)
        random_list.append(digits[random_index])

    for i in range(number_of_special_chars):
        random_index = random.randint(0, len(allowed_special_chars) - 1)
        random_list.append(allowed_special_chars[random_index])

    for i in range(len(random_list)):
        random_index = random.randint(0, len(random_list) - 1)
        generated_id += random_list[random_index]
        random_list.remove(random_list[random_index])

    return generated_id
