import datetime

def encode_message(message):
    odd_day_encoding = {chr(i + 64): f"{i:02d}" for i in range(1, 27)}
    even_day_encoding = {chr(i + 64): f"{i + 500:03d}" for i in range(1, 27)}

    today = datetime.datetime.now()
    encoding_scheme = odd_day_encoding if today.day % 2 != 0 else even_day_encoding

    encoded_message = []
    for char in message.upper():
        if char.isalpha():
            encoded_message.append(encoding_scheme[char])
        elif char == " ":
            encoded_message.append(" ")  # Retain spaces in the message
        else:
            encoded_message.append(char)  # Retain any non-alphabetic characters as they are

    return ''.join(encoded_message)
