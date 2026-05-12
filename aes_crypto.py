import os
import time
from cryptography.fernet import Fernet


def run_aes_demo(work_dir: str, original_message: str) -> dict:
    """AES (Fernet) шифрлөө/дешифрлөө демонстрациясын иштетет."""
    os.makedirs(work_dir, exist_ok=True)

    symmetric_key = Fernet.generate_key()
    cipher_suite = Fernet(symmetric_key)
    message_bytes = original_message.encode("utf-8")

    start_time_aes = time.perf_counter()

    cipher_text_aes = cipher_suite.encrypt(message_bytes)

    file_path = os.path.join(work_dir, "aes_encrypted_data.txt")
    with open(file_path, "wb") as f:
        f.write(cipher_text_aes)

    with open(file_path, "rb") as f:
        encrypted_data_from_file = f.read()
    plain_text_aes = cipher_suite.decrypt(encrypted_data_from_file)

    end_time_aes = time.perf_counter()
    aes_duration = end_time_aes - start_time_aes

    return {
        "key": symmetric_key.decode("utf-8"),
        "cipher_text": cipher_text_aes,
        "decrypted_text": plain_text_aes.decode("utf-8"),
        "duration": aes_duration,
        "file_path": file_path,
    }


if __name__ == "__main__":
    print("--- СИММЕТРИЯЛЫК ШИФРЛӨӨ (AES) ---")
    default_dir = os.path.join(os.getcwd(), "crypto_output")
    default_message = "Блокчейн транзакциясынын купуя маалыматтары. 100 BTC которулду."
    result = run_aes_demo(default_dir, default_message)
    print(f"[+] Генерацияланган AES ачкычы: {result['key']}")
    print(f"\n[+] Баштапкы текст: {default_message}")
    print(f"[+] Шифрленген текст (Ciphertext): {result['cipher_text'][:50]}... (кыскартылды)")
    print(f"[+] Дешифрленген текст: {result['decrypted_text']}")
    print(f"[!] AES алгоритминин аткарылуу убактысы: {result['duration']:.6f} секунд")
