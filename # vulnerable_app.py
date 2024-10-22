# vulnerable_app.py

# Example of a vulnerable code
def insecure_function(user_input):
    # Simulating a code injection vulnerability
    eval(user_input)  # This is unsafe! Don't do this in production.

if __name__ == "__main__":
    user_input = "print('Vulnerable to code injection!')"
    insecure_function(user_input)
