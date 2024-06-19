import random


def generate_password(n, len_pass):
    password = ''
    count = 0
    while count != n:
        for _ in range(len_pass):
            password += random.choice(chars)
        print(password)
        password = ''
        count += 1


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
chars = ''
n = int(input('Количество паролей для генерации '))
len_pass = int(input('Длина пароля '))
is_digits = input('Включать ли цифры 0123456789? ').lower()
is_uppercase_letters = input(
    'Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ ').lower()
is_lowercase_letters = input(
    'Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? ').lower()
is_punctuation = input(
    'Включать ли символы !#$%&*+-=?@^_? ').lower()
is_symbols = input('Включить ли неоднозначные символы il1Lo0O? ').lower()

if is_punctuation == 'да':
    chars += punctuation
if is_digits == 'да':
    chars += digits
if is_lowercase_letters == 'да':
    chars += lowercase_letters
if is_uppercase_letters == 'да':
    chars += uppercase_letters
if is_symbols == 'да':
    chars += 'il1Lo0O'

generate_password(n, len_pass)
