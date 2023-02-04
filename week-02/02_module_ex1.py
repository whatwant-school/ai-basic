import fah_converter

if __name__ == "__main__":

    print("Enter a celcius value: "),
    celcius = float(input())
    
    fahrenheit = fah_converter.convert_c_to_f(celcius)
    print(f"That is {fahrenheit} degrees fahrenheit")
