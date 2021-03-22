import random

import module

def xor_encryption():
    """Xor transcript(encryption)"""
    message = input("Введите сообщение (Enter - чтение из файла):")
    key = input("\nВведите ключ (Enter - ключ сгенерируется автоматически):")

    if not message:
        message = module.read_from_file()

    if not key:
        key = "".join(
            random.choice(
                "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            ) 
            for i in range(random.randint(1, len(message)))  #Creating a random key
        )
        print(f"Ключ сгененрировался:\n{key}")

    result = bytearray()
    if type(message) == str:
        message = bytearray(message, "utf-8")
    key = bytearray(key, "utf-8")

    for i in range(len(message)):
        result.append(message[i] ^ key[i % len(key)])
    module.write_to_file(result)
xor_encryption()


