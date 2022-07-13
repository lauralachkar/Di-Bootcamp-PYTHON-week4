#Encryption

shift = 3 # defining the shift count

text = "HELLO WORLD"

encryption = ""

for c in text:

    # check if character is an uppercase letter
    if c.isupper():

        # find the position in 0-25
        c_unicode = ord(c)

        c_index = ord(c) - ord("A")

        # perform the shift
        new_index = (c_index + shift) % 26

        # convert to new character
        new_unicode = new_index + ord("A")

        new_character = chr(new_unicode)

        # append to encrypted string
        encryption = encryption + new_character

    else:

        # since character is not uppercase, leave it as it is
        encryption += c
        
print("Plain text:",text)

print("Encrypted text:",encryption)


# Now that we understand the two fundamental methods we’ll use, let’s implement the encryption technique for capital letters in Python. We shall encrypt only the uppercase characters in the text and will leave the remaining ones unchanged. Let’s first look at the step-by-step process of encrypting the capital letters:

# 1. Define the shift value i.e., the number of positions we want to shift from each character.
# 2. Iterate over each character of the plain text:
#     1. If the character is upper-case:
#         1. Calculate the position/index of the character in the 0-25 range.
#         2. Perform the positive shift using the modulo operation.
#         3. Find the character at the new position.
#         4. Replace the current capital letter by this new character.
#     2. Else, If the character is not upper-case, keep it with no change.
# Let us now look at the code:


# As we can see, the encrypted text for “HELLO WORLD” is “KHOOR ZRUOG”, and it matches the one we arrived at manually in the Introduction section.
#Also, this method doesn’t encrypt the space character, and it continues to be a space in the encrypted version.


#Decryption

shift = 3 # defining the shift count

encrypted_text = "KHOOR ZRUOG"

plain_text = ""

for c in encrypted_text:

    # check if character is an uppercase letter
    if c.isupper():

        # find the position in 0-25
        c_unicode = ord(c)

        c_index = ord(c) - ord("A")

        # perform the negative shift
        new_index = (c_index - shift) % 26

        # convert to new character
        new_unicode = new_index + ord("A")

        new_character = chr(new_unicode)

        # append to plain string
        plain_text = plain_text + new_character

    else:

        # since character is not uppercase, leave it as it is
        plain_text += c

print("Encrypted text:",encrypted_text)

print("Decrypted text:",plain_text)

# Now that we’ve figured out the encryption for plain text capital letters using Ceaser Cipher let’s look at how we will decrypt the ciphertext into plain text.
# Earlier, we looked at the mathematic formulation of the encryption process. Let’s now check out the same for the decryption process.

# Let us look at the step-by-step implementation of the decryption process, which will be more or less the reverse of the encryption:
# * Define the number of shifts
# * Iterate over each character in the encrypted text:
#     * If the character is an uppercase letter:
#         1. Calculate the position/index of the character in the 0-25 range.
#         2. Perform the negative shift using the modulo operation.
#         3. Find the character at the new position.
#         4. Replace the current encrypted letter by this new character (which will also be an uppercase letter).
#         5. Else, if the character is not capital, keep it unchanged.


