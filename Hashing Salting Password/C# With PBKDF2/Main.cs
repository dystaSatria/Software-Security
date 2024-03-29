using System;
using System.Security.Cryptography;
using System.Text;

public class PasswordHashing
{
    const int keySize = 64;
    const int iterations = 350000;
    static readonly HashAlgorithmName hashAlgorithm = HashAlgorithmName.SHA512;

    public static string HashPassword(string password, out byte[] salt)
    {
        salt = new byte[keySize / 8];
        using (var rng = RandomNumberGenerator.Create())
        {
            rng.GetBytes(salt);
        }

        using (var pbkdf2 = new Rfc2898DeriveBytes(password, salt, iterations, hashAlgorithm))
        {
            byte[] hash = pbkdf2.GetBytes(keySize / 8);
            return BitConverter.ToString(hash).Replace("-", "");
        }
    }

    public static bool VerifyPassword(string enteredPassword, byte[] storedHash, byte[] storedSalt)
    {
        using (var pbkdf2 = new Rfc2898DeriveBytes(enteredPassword, storedSalt, iterations, hashAlgorithm))
        {
            byte[] enteredHash = pbkdf2.GetBytes(keySize / 8);
            return CompareByteArrays(enteredHash, storedHash);
        }
    }

    static bool CompareByteArrays(byte[] array1, byte[] array2)
    {
        if (array1 == null || array2 == null || array1.Length != array2.Length)
            return false;

        for (int i = 0; i < array1.Length; i++)
        {
            if (array1[i] != array2[i])
                return false;
        }
        return true;
    }

    static void Main(string[] args)
    {
        Console.WriteLine("Enter your password:");
    string password = Console.ReadLine();

    byte[] salt;
    string hashedPassword = HashPassword(password, out salt);

    Console.WriteLine("Stored Hashed Password: " + hashedPassword);
    Console.WriteLine("Salt: " + BitConverter.ToString(salt).Replace("-", ""));

    
    Console.WriteLine("\nEnter the password to verify:");
    string enteredPassword = Console.ReadLine();
    bool passwordMatch = VerifyPassword(enteredPassword, HexStringToByteArray(hashedPassword), salt);
    Console.WriteLine("Password Match: " + passwordMatch);
    }

    static byte[] HexStringToByteArray(string hex)
    {
        int numberChars = hex.Length;
        byte[] bytes = new byte[numberChars / 2];
        for (int i = 0; i < numberChars; i += 2)
        {
            bytes[i / 2] = Convert.ToByte(hex.Substring(i, 2), 16);
        }
        return bytes;
    }
}
