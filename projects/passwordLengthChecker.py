# ==========================================
# PROJECT: Secure Password Length Checker
# FOCUS: Control Flow, Input Validation, and Logic
# ==========================================

# 1. DEFINE CONSTANTS
# Set a variable for MIN_LENGTH (e.g., 8) and MAX_LENGTH (e.g., 64).
# Using constants makes your code "clean" and easy to update later.


# 2. DEFINE THE VALIDATION FUNCTION
# Create a function (e.g., check_password_strength) that takes a 'password' string.
# REQUIREMENT: This function should return TWO values (a boolean and a message).
# This mimics the "multiple return" pattern common in security tools.
def check_password_strength(password):
    # STEP A: Check if the password is too short.
    # If so, return (False, "Error: Password is too short.")

    # STEP B: Check if the password is too long.
    # If so, return (False, "Error: Password is too long.")

    # STEP C: (Optional) Check if the password is just a string of spaces.
    # Hint: look up the .strip() or .isspace() methods.

    # STEP D: If it passes all checks, return (True, "Success: Password length is valid.")
    pass


# 3. MAIN EXECUTION BLOCK
# This is where your program actually starts running.
if __name__ == "__main__":
# STEP A: Capture user input using the input() function.

# STEP B: WRAP IN TRY/EXCEPT
# Even though input() usually returns a string, get in the habit of
# wrapping user-facing logic in a try/except block to catch unexpected issues.

# STEP C: CALL THE FUNCTION
# Unpack the two return values into variables (e.g., is_valid, message).

# STEP D: FINAL CONTROL FLOW
# Use an if/else statement to print the 'message'.
# If is_valid is True, maybe print a success green-check emoji!

# STEP E: REFLECTION / CLEANUP
# Print a final "Validation Complete" message that runs regardless of the result.