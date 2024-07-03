
import random

def validate_national_code(code):
    if not code.isdigit() or len(code) != 10:
        return False
    
    check_digit = int(code[-1])
    sum_digits = sum([int(code[x]) * (10 - x) for x in range(9)])
    remainder = sum_digits % 11
    
    if remainder < 2 and check_digit == remainder:
        return True
    elif remainder >= 2 and check_digit == 11 - remainder:
        return True
    else:
        return False

def generate_valid_national_code(city_code, generated_codes):
    code = city_code + ''.join([str(random.randint(0, 9)) for _ in range(6)])
    sum_digits = sum([int(code[x]) * (10 - x) for x in range(9)])
    remainder = sum_digits % 11
    if remainder < 2:
        check_digit = remainder
    else:
        check_digit = 11 - remainder
    code += str(check_digit)
    if validate_national_code(code) and code not in generated_codes:
        generated_codes.add(code)
        return code
    else:
        return generate_valid_national_code(city_code, generated_codes)

def generate_codes_for_city(city_code, num_codes, generated_codes):
    valid_codes = []
    while len(valid_codes) < num_codes:
        valid_code = generate_valid_national_code(city_code, generated_codes)
        if valid_code:
            valid_codes.append(valid_code)
    return valid_codes

def get_user_inputs():
    generated_codes = set()
    
    city_code = input('Enter the city code: ')
    while True:
        try:
            num_codes = int(input('How many national codes do you need?? '))
            break
        except ValueError:
            print('Please enter a valid number.')
    
    valid_codes = generate_codes_for_city(city_code, num_codes, generated_codes)
    print(f'Valid national codes for city code {city_code}:')
    for code in valid_codes:
        print(code)

    file_name = f"{city_code}_{num_codes}_codes.txt"
    with open(file_name, 'w') as file:
        for code in valid_codes:
            file.write(f"{code}\n")
    print(f'National codes have been saved to {file_name}')

if __name__ == "__main__":
    get_user_inputs()
