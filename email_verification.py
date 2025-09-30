# ===== TASK 2: Email Validator =====
# Create a custom InvalidEmailError exception
# The function should validate email format and raise InvalidEmailError if:
# - Email doesn't contain exactly one '@' symbol
# - Email doesn't contain at least one '.' after the '@'
# If input is empty, raise ValueError with message "Error: email cannot be empty"
# Keep asking until a valid email is entered


print("=== Task 2: Email Validator ===")
print("Email must contain '@' and a domain with '.'\n")

class InvalidEmailError(Exception):
    """Custom exception for invalid email format."""
    pass

def validate_email(prompt):
    while True:
        try:
            email = input(prompt).strip()
            if not email:
                raise ValueError("Error: email cannot be empty")
            
            
            if email.count('@') != 1:
                raise InvalidEmailError("Error: email must contain exactly one '@' symbol")
            
            local, domain = email.split('@')
            if '.' not in domain:
                raise InvalidEmailError("Error: email must have a domain with '.' after '@'")
            
            
            return email
        
        except ValueError as e:
            print(e)
        except InvalidEmailError as e:
            print(e)
        except Exception as e:
            print(f"Unexpected error: {e}")

email = validate_email("Enter your email: ")
print(f"Email accepted: {email}")
