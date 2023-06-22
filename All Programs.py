import math

def check_positive_number(num):
    
    if num > 0:
        return True
    else:
        return False

def check_triangle(s1, s2, s3):
    if s1 + s2 > s3 and s2 + s3 > s1 and s3 + s1 > s2:
        return True
    else:
        return False

def check_power_even(num, power):
    result = math.pow(num, power)
    if result % 2 == 0:
        return True
    else:
        return False


def check_senior_citizen_concession(dob_year):
    if dob_year > 60:
        fare = 1020 - (1020 * 0.2)  
    else:
        fare = 1020

    return fare

def check_pythagorean_triple(n1, n2, n3):
    if n1 * n1 + n2 * n2 == n3 * n3:
        return 1
    else:
        return 0

def check_blood_donation_eligibility(age, weight):
    if age > 18 and weight > 40:
        return 1
    else:
        return 0

def calculate_bonus(salary, years_of_service):
    if years_of_service > 10:
        bonus = salary * 0.1
    elif years_of_service > 6 and years_of_service <= 10:
        bonus = salary * 0.08
    else:
        bonus = salary * 0.05

    return bonus

def calculate_wages(age, gender, days):
    if age >= 18 and age < 30:
        if gender == 'M':
            wages = 700
        elif gender == 'F':
            wages = 750
    elif age >= 30 and age <= 40:
        if gender == 'M' or gender == 'F':
            wages = 800
    else:
        wages = 0

    total_amount = wages * days
    return total_amount

def calculate_tip(food_rating, service_rating, ambience_rating, bill_amount):
    if food_rating >= 4 and service_rating >= 4 and ambience_rating >= 4:
        tip = bill_amount * 0.1
    elif food_rating <= 3 and service_rating <= 3 and ambience_rating <= 3:
        tip = bill_amount * 0.01
    else:
        tip = bill_amount * 0.05

    return tip

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# input your choice
choice = int(input("Enter the question number \n 1 for to check if a number is positive \n 2 for to check if a triangle is possible \n 3 for to check if the nth power of a number is even \n 4 for to check if a person is eligible for senior citizen fare concession \n 5 for to check if three numbers form a Pythagorean triple \n 6 for to check eligibility for blood donation \n 7 for to calculate bonus based on years of service \n 8 for to calculate wages based on age, gender, and days worked \n 9 for to calculate tip based on ratings and bill amount \n 10 for to check if a year is a leap year : "))

if choice == 1:
    num=int(input("enter the number :"))
    is_positive = check_positive_number(num)
    if is_positive:
        print("The number is positive.")
    else:
        print("The number is not positive.")

elif choice == 2:
    s1 = int(input("Enter the first side of the triangle: "))
    s2 = int(input("Enter the second side of the triangle: "))
    s3 = int(input("Enter the third side of the triangle: "))
    is_possible = check_triangle(s1, s2, s3)
    if is_possible:
        print("The triangle is possible.")
    else:
        print("The triangle is not possible.")

elif choice == 3:
    num=int(input("enter the number :"))
    power = int(input("Enter the power: "))
    is_even = check_power_even(num, power)
    if is_even:
        print("The nth power of the number is even.")
    else:
        print("The nth power of the number is not even.")

elif choice == 4:
    dob_year = int(input("Enter the year of birth: "))
    final_fare = check_senior_citizen_concession(dob_year)
    if final_fare > 0:
        print("The final traveling charge is Rs", final_fare)
    else:
        print("The original fare will be displayed.")

elif choice == 5:
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    n3 = int(input("Enter the third number: "))
    is_pythagorean_triple = check_pythagorean_triple(n1, n2, n3)
    print(is_pythagorean_triple)

elif choice == 6:
    age = int(input("Enter the age: "))
    weight = int(input("Enter the weight: "))
    is_eligible = check_blood_donation_eligibility(age, weight)
    if is_eligible:
        print("The person is eligible for blood donation.")
    else:
        print("The person is not eligible for blood donation.")

elif choice == 7:
    salary = float(input("Enter the salary: "))
    years_of_service = int(input("Enter the years of service: "))
    bonus = calculate_bonus(salary, years_of_service)
    print("The bonus is", bonus)

elif choice == 8:
    age = int(input("Enter the age: "))
    gender = input("Enter the gender (M/F): ")
    days = int(input("Enter the number of days: "))
    total_amount = calculate_wages(age, gender, days)
    print("The total amount to be paid is", total_amount)

elif choice == 9:
    food_rating = int(input("Enter the food rating (1-5): "))
    service_rating = int(input("Enter the service rating (1-5): "))
    ambience_rating = int(input("Enter the ambience rating (1-5): "))
    bill_amount = float(input("Enter the bill amount: "))
    tip = calculate_tip(food_rating, service_rating, ambience_rating, bill_amount)
    print("The tip is", tip)

elif choice == 10:
    year = int(input("Enter a year: "))
    if is_leap_year(year):
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")

else:
    print("Invalid question number. Please enter a number between 1 and 10.")
