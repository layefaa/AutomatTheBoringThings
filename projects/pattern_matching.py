# ==========================================
# PHASE 3: Content-Based Validation
# FOCUS: Loops, Character Sets, and Boolean Flags
# ==========================================

# 1. DEFINE SPECIAL CHARACTER SET
# Create a string containing all allowed special characters.
# Example: SPECIAL_CHARS = "!@#$%^&*()-_=+"


def check_password_complexity(password):
    # STEP A: INITIALIZE FLAGS
    # Start with 'has_digit' and 'has_special' set to False.
    has_digit = False
    has_special = False

    # STEP B: THE INSPECTION LOOP
    # Use a 'for char in password:' loop to look at every single character.
    for char in password:
    # 1. Check if the current char is a digit (.isdigit())
    # 2. Check if the current char is in your SPECIAL_CHARS string

    # STEP C: LOGIC EVALUATION
    # After the loop finishes, evaluate the results.
    # Return (True, "Strong") only if BOTH flags are True.
    # Otherwise, return (False, "Missing digit or special character")
    pass


# 2. REVISITING THE MAIN BLOCK (Refactoring)
if __name__ == "__main__":
    # Integration Task:
    # 1. Get input
    # 2. Run your Phase 1 & 2 checks (Length & Empty strings)
    # 3. If those pass, run this Phase 3 check.

    # 💡 ADVANCED GOAL:
    # Use 'try/except' to catch a KeyboardInterrupt.
    # This happens if the user hits Ctrl+C to try and crash your tool.
    try:
        # Your logic here
        pass
    except KeyboardInterrupt:
        print("\n[!] Process terminated by user. Exiting safely.")