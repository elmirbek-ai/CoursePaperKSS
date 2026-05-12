import os
import time
from cryptography.fernet import Fernet

# Жумушчу каталогду аныктоо (Мисалы, локалдык долбоор папкасы)
work_dir = r"C:\Users\Элмирбек\CryptoProject"
if not os.path.exists(work_dir):
    os.makedirs(work_dir)

print("--- СИММЕТРИЯЛЫК ШИФРЛӨӨ (AES) ---")

# 1. AES үчүн ачкыч генерациялоо
symmetric_key = Fernet.generate_key()
cipher_suite = Fernet(symmetric_key)
print(f"[+] Генерацияланган AES ачкычы: {symmetric_key.decode('utf-8')}")

# Шифрлене турган баштапкы текст
original_message = "Блокчейн транзакциясынын купуя маалыматтары. 100 BTC которулду."
message_bytes = original_message.encode('utf-8')

# Убакытты өлчөөнү баштоо
start_time_aes = time.perf_counter()

# 2. Маалыматты шифрлөө
cipher_text_aes = cipher_suite.encrypt(message_bytes)

# Шифрленген маалыматты файлга сактоо (имитация)
file_path = os.path.join(work_dir, "aes_encrypted_data.txt")
with open(file_path, "wb") as f:
    f.write(cipher_text_aes)

# 3. Маалыматты файлдан окуп дешифрлөө
with open(file_path, "rb") as f:
    encrypted_data_from_file = f.read()
plain_text_aes = cipher_suite.decrypt(encrypted_data_from_file)

# Убакытты токтотуу
end_time_aes = time.perf_counter()
aes_duration = end_time_aes - start_time_aes

print(f"\n[+] Баштапкы текст: {original_message}")
print(f"[+] Шифрленген текст (Ciphertext): {cipher_text_aes[:50]}... (кыскартылды)")
print(f"[+] Дешифрленген текст: {plain_text_aes.decode('utf-8')}")
print(f"[!] AES алгоритминин аткарылуу убактысы: {aes_duration:.6f} секунд")