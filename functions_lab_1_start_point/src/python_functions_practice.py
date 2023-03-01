def return_10():
    return 10

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def length_of_string(string):
    return len(string)

def join_string(string1, string2):
    return string1 + string2

def add_string_as_number(string1, string2):
    return int(string1) + int(string2)

def number_to_full_month_name(month_number):
    months = ["January", "February", "March",
        "April", "May", "June", "July", "August",
        "September", "October", "November",
        "December"]
    
    return months[month_number - 1]

def number_to_short_month_name(month_number):
    return number_to_full_month_name(month_number)[:3]

def get_cube_volume(side_length):
    return side_length ** 3

def reverse_string(string):
    new_string = ""
    for char in string:
        new_string = char + new_string
    return new_string

def fahrenheit_to_celsius(fahrenheit_temp):
    return (fahrenheit_temp - 32) / 1.8