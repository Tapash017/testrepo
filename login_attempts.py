class User:
    def __init__(self, first_name, last_name, age):
        """Initialize user attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0
    
    def describe_user(self):
        """Prints a summary of the user’s information."""
        print(f"User: {self.first_name} {self.last_name}, Age: {self.age}")
    
    def greet_user(self):
        """Prints a personalized greeting to the user."""
        print(f"Hello, {self.first_name} {self.last_name}!")
    
    def increment_login_attempts(self):
        """Increments the login attempts by 1."""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Resets the login attempts to 0."""
        self.login_attempts = 0

        
# Create an instance of User
user = User("John", "Doe", 30)

# Call increment_login_attempts multiple times
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login attempts: {user.login_attempts}")

# Reset login attempts
user.reset_login_attempts()
print(f"Login attempts after reset: {user.login_attempts}")