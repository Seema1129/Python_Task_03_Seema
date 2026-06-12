# Username Generator

first_name = input("Enter first name: ").lower()
last_name = input("Enter last name: ").lower()
birth_year = input("Enter birth year: ")

print("\nUsername Suggestions:")
print(first_name + last_name + birth_year)
print(first_name[0] + "." + last_name + birth_year[-2:])
print(last_name + "_" + first_name)
print(first_name + "_" + birth_year)
print(last_name + first_name[0] + birth_year)