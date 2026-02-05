try:
    open("nonexistent.txt")
except Exception:
    print("Something went wrong!")