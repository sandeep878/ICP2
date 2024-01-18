heights_inches =[]
print ("Enter heights in inches. Type 'done' when finished.")
while True:
    user_input = input("Enter height in inches(or 'done' to finish): ")
    if user_input.lower() == 'done':
        break
    try:
        height_inch = float(user_input)
        heights_inches.append(height_inch)
    except ValueError:
            print("Invalid input. Please enter a valid number or 'done'.")
heights_centimeters = [height * 2.54 for height in heights_inches]
print("Heights in Inches:", heights_inches)
print("Heights in centimeters:", heights_centimeters)
