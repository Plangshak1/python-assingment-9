# ===== TASK 2: Email Validator =====
# Create a custom InvalidEmailError exception
# The function should validate email format and raise InvalidEmailError if:
# - Email doesn't contain exactly one '@' symbol
# - Email doesn't contain at least one '.' after the '@'
# If input is empty, raise ValueError with message "Error: email cannot be empty"
# Keep asking until a valid email is entered

print("=== Task 2: Email Validator ===")
print("Email must contain '@' and a domain with '.'\n")

def validate_email(prompt):
    #
    # Write your code here.
    # Define InvalidEmailError class
    # Validate email format
    # Handle exceptions and keep prompting
    #
    pass

email = validate_email("Enter your email: ")
print(f"Email accepted: {email}")
print()
