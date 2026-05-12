import time
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

print("--- АСИММЕТРИЯЛЫК ШИФРЛӨӨ (RSA) ---")

# 1. RSA Ачкычтар жубун генерациялоо (Жабык жана Ачык ачкыч)
print("[*] 2048-биттик RSA ачкычтары генерацияланууда...")
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)
public_key = private_key.public_key()
print("[+] Ачкычтар ийгиликтүү түзүлдү.")

original_message = "Блокчейн транзакциясынын купуя маалыматтары. 100 BTC которулду."
message_bytes = original_message.encode('utf-8')

# Убакытты өлчөөнү баштоо
start_time_rsa = time.perf_counter()

# 2. Ачык ачкыч (Public Key) менен шифрлөө
cipher_text_rsa = public_key.encrypt(
    message_bytes,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# 3. Жабык ачкыч (Private Key) менен дешифрлөө
plain_text_rsa = private_key.decrypt(
    cipher_text_rsa,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Убакытты токтотуу
end_time_rsa = time.perf_counter()
rsa_duration = end_time_rsa - start_time_rsa

print(f"\n[+] Баштапкы текст: {original_message}")
print(f"[+] Шифрленген тексттин узундугу: {len(cipher_text_rsa)} байт")
print(f"[+] Дешифрленген текст: {plain_text_rsa.decode('utf-8')}")
print(f"[!] RSA алгоритминин аткарылуу убактысы: {rsa_duration:.6f} секунд")