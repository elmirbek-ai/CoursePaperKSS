import time
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa


def run_rsa_demo(original_message: str) -> dict:
    """RSA шифрлөө/дешифрлөө демонстрациясын иштетет."""
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()
    message_bytes = original_message.encode("utf-8")

    start_time_rsa = time.perf_counter()

    cipher_text_rsa = public_key.encrypt(
        message_bytes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )

    plain_text_rsa = private_key.decrypt(
        cipher_text_rsa,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )

    end_time_rsa = time.perf_counter()
    rsa_duration = end_time_rsa - start_time_rsa

    return {
        "cipher_text": cipher_text_rsa,
        "decrypted_text": plain_text_rsa.decode("utf-8"),
        "duration": rsa_duration,
        "cipher_length": len(cipher_text_rsa),
    }


if __name__ == "__main__":
    print("--- АСИММЕТРИЯЛЫК ШИФРЛӨӨ (RSA) ---")
    print("[*] 2048-биттик RSA ачкычтары генерацияланууда...")

    default_message = "Блокчейн транзакциясынын купуя маалыматтары. 100 BTC которулду."
    result = run_rsa_demo(default_message)

    print("[+] Ачкычтар ийгиликтүү түзүлдү.")
    print(f"\n[+] Баштапкы текст: {default_message}")
    print(f"[+] Шифрленген тексттин узундугу: {result['cipher_length']} байт")
    print(f"[+] Дешифрленген текст: {result['decrypted_text']}")
    print(f"[!] RSA алгоритминин аткарылуу убактысы: {result['duration']:.6f} секунд")
