# ==========================================
# PHASE 2: Input Validation Logic
# FOCUS: Type Safety, Edge Cases, and Sanitization
# ==========================================

def validate_user_input(raw_input):
# 1. TYPE CHECKING
# Use isinstance() to ensure raw_input is actually a string.
# While input() in Python 3 always returns a string, explicit checks
# prevent "Type Confusion" bugs if this function is used elsewhere.


# 2. SANITIZATION (The "Trim" rule)
# Users often accidentally hit the spacebar.
# Create a variable 'clean_input' that removes leading/trailing whitespace.
# Hint: Use the .strip() method.


# 3. THE "EXISTENCE" CHECK
# Check if 'clean_input' is empty after stripping.
# An empty password is a major security bypass if not caught.
# If len is 0, return (False, "Input cannot be empty")


# 4. DATA INTEGRITY (The "No-Go" characters)
# (Optional/Advanced) Check if the input contains dangerous characters
# like null bytes (\0) which can sometimes crash underlying C libraries.


# 5. RETURN CLEAN DATA
# If all is well, return (True, clean_input)