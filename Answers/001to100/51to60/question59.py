"""
Question 59:
Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using p059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.
"""

CIPHER_FILE = "../../../resources/cipher.txt"

with open(CIPHER_FILE, "r") as f:
    CIPHER_TEXT = [int(n) for n in f.readlines()[0].strip().split(",")]


def score(plain):
    result = 0
    for c in plain:
        if 65 <= c <= 90:
            result += 1
        elif 97 <= c <= 122:
            result += 2
        elif c < 0x20 or c == 0x7F:
            result -= 10
    return result


def decrypt(cipher, key):
    return [(c ^ key[i % len(key)]) for (i, c) in enumerate(cipher)]


def answer():
    key = max(((i, j, k) for i in range(97, 123) for j in range(97, 123) for k in range(97, 123)),
              key=lambda x: score(decrypt(CIPHER_TEXT, x)))
    return sum(decrypt(CIPHER_TEXT, key))


if __name__ == '__main__':
    print("Answer is:", answer())



