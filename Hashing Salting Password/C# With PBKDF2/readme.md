# Hashing and Salting Passwords in C# With PBKDF2

## Summary

This C# code provides an example of securely hashing passwords using the PBKDF2 algorithm with SHA-512 hashing. It includes methods for hashing passwords and verifying them later.

## Usage

1. **Hashing a Password**
    - Call the `HashPassword` method, passing the password as a parameter.
    - The method will generate a random salt, hash the password using PBKDF2, and return the hashed password as a hexadecimal string along with the generated salt.

2. **Verifying a Password**
    - When verifying a password, you need to pass the entered password, the stored hash, and the stored salt to the `VerifyPassword` method.
    - The method will use the entered password and stored salt to hash the entered password and then compare it with the stored hash.

## Code Explanation

- The `PasswordHashing` class contains two main methods:
    - `HashPassword`: This method takes a password as input, generates a random salt, hashes the password using PBKDF2 with SHA-512, and returns the hashed password as a hexadecimal string along with the salt.
    - `VerifyPassword`: This method takes the entered password, the stored hash, and the stored salt as input, hashes the entered password using the stored salt, and compares the resulting hash with the stored hash to verify the password.

- The `HexStringToByteArray` method is used to convert a hexadecimal string to a byte array.

- The `Main` method is provided as an example usage of the hashing and verification methods. It prompts the user to enter a password, hashes it, displays the hashed password and salt, prompts the user to enter the password again for verification, and displays whether the entered password matches the stored hash.

## Requirements

- .NET Core or .NET Framework runtime environment.
