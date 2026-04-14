# password_generator
This is a command-line interface (CLI) application written in Python that generates strong, random passwords based on user preferences. It offers three difficulty levels to balance security and complexity. The script validates input to ensure the password is at least 8 characters long, providing a basic layer of security. 

How it works:

Difficulty Selection: The user chooses from "Easy" (letters only), "Medium" (letters and numbers), or "Hard" (letters, numbers, and symbols).

Length Definition: The user inputs the desired password length (minimum 8 characters).

Generation: The program uses the random.choice() function to randomly select characters from the predefined character sets.

Output: The generated password is printed to the console. 


