# ===== TASK 1: Password Validator =====
# Create a custom WeakPasswordError exception
# The function should validate password strength and raise WeakPasswordError if:
# - Password is less than 8 characters
# - Password doesn't contain at least one digit
# If input is empty, raise ValueError with message "Error: password cannot be empty"
# Keep asking until a valid password is entered

print("=== Task 1: Password Validator ===")
print("Password must be at least 8 characters and contain at least one digit\n")

class PasswordError(Exception):
    """Custom exception for invalid password."""
    pass

def validate_password(prompt):
    while True:
        try:
            value = input(prompt).strip()
            
            if not value:
                raise ValueError("Error: invalid password (cannot be empty)")
            
            if len(value) < 8:
                raise PasswordError("Error: password must be at least 8 characters long")
            
            if not any(ch.isdigit() for ch in value):
                raise PasswordError("Error: password must contain at least one digit")
            
            return value
        
        except ValueError as e:
            print(e)
        except PasswordError as e:
            print(e)
        except Exception as e:
            print(f"Unexpected error: {e}")

password = validate_password("Enter your password: ")
print(f"Password accepted: {'*' * len(password)}")
