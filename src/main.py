def celsius_to_fahrenheit(temp):
    return temp * 9 / 5 + 32

if __name__ == '__main__':
    temp_celsius = 10
    print(f"{temp_celsius} degrees Celsius is {celsius_to_fahrenheit(temp_celsius)} degrees Fahrenheit")