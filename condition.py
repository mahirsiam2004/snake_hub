# Condition using and, or, and not

age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (yes/no): ").lower()
banned = input("Are you banned from entry? (yes/no): ").lower()

if age >= 18 and has_id == "yes" and not banned == "yes":
    print("✅ You can enter.")
elif age < 18 or has_id == "no" or banned == "yes":
    print("❌ You cannot enter.")



age = int(input("Enter your age: "))

# Conditional expression
message = "Adult" if age >= 18 else "Minor"

print(message)
