# Crypto-Encrypter

**COMPANY** : CODTECH IT SOLUTIONS

**NAME** : DAMANDEEP KUMAR

**INTERN ID** : CT6MTNGN

**DOMAIN** : CYBER SECURITY

**DURATION** : 6 MONTHS

**MENTOR** : NEELA SANTOSH

# DESCRIPTION
Crypto Encrypter is a Python-based encryption application that allows users to secure their sensitive files using advanced encryption algorithms. The application provides a user-friendly interface with buttons for encrypting and decrypting files.

# Key Features:

* User-friendly interface with a file browser and buttons for encryption and decryption.
* Uses the Fernet module from the cryptography library for secure encryption and decryption of files.
* Generates a unique encryption key for each session and stores it securely in a file named "secret.key".
* Provides a way to encrypt and decrypt files using the generated key.
* Displays informative messages to the user about the encryption and decryption process.
* The application is built using Python's Tkinter library for creating the user interface. It allows users to select files, encrypt them using the Fernet algorithm, and decrypt them back to their original form.

The encryption key is generated using the Fernet.generate_key() method and stored in a file named "secret.key". This key is used for encrypting and decrypting files.

To ensure security, the application should be distributed with a key file that is not included in the source code. The "secret.key" file should be kept secure and not shared with unauthorized individuals.

Please note that this application is a basic implementation and may require additional features and security measures for a production-ready encryption tool.

# USAGE
1. Save the Python code provided in a file named "crypto_encrypter.py".

2. Install the required dependencies by running the following command in your terminal or command prompt:

         pip install cryptography

3. **In windows**
 * Run the application by executing the following command in your terminal or command prompt:

         python crypto_encrypter.py
 4. **In Linux**  
   * Run the application by executing the following command in your terminal or command prompt:

         python3 crypto_encrypter.py
         
5. A window will open with the application interface.

6. Click the "Browse Files" button to select the file you want to encrypt or decrypt.

5. Enter the file path in the text field provided.

6. Click the "Encrypt" button to encrypt the selected file. The encrypted file will be saved with the same name as the original file.

7. To decrypt a file, click the "Decrypt" button. The decrypted file will be saved with the original file name.

8. The application will display informative messages to indicate the success or failure of the encryption or decryption process.

9. The encryption key is stored in a file named "secret.key". Make sure to keep this file secure and not share it with unauthorized individuals.

# Output

Here's an example output of the Crypto Encrypter application when running the script:

```
Generating key...
Key generated successfully.
```

This message indicates that the encryption key has been generated and saved in the "secret.key" file.

```
Encrypting file...
File encrypted successfully.
```

This message appears when the user clicks the "Encrypt" button and the selected file has been successfully encrypted.

```
Decrypting file...
File decrypted successfully.
```

This message appears when the user clicks the "Decrypt" button and the selected file has been successfully decrypted.

The application also displays informative messages to the user about the encryption and decryption process, such as "File encrypted successfully" and "File decrypted successfully".

Please note that the actual output may vary based on the specific file you select and the actions you perform.

Remember to keep the "secret.key" file secure and not share it with unauthorized individuals.

For advanced usage, you can create executable files or scripts to run the application on different platforms without the need for Python installation.


