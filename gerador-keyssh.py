from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

# Gerar uma chave RSA de 2048 bits
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

# Serializar a chave privada no formato OpenSSH
private_key_ssh = private_key.private_bytes(
    encoding=serialization.Encoding.OpenSSH,
    format=serialization.PrivateFormat.OpenSSH,
    encryption_algorithm=serialization.NoEncryption()
)

# Salvar a chave privada em um arquivo
with open('private_key.openssh', 'wb') as f:
    f.write(private_key_ssh)

# Obter a chave pública correspondente
public_key = private_key.public_key()
public_key_ssh = public_key.public_bytes(
    encoding=serialization.Encoding.OpenSSH,
    format=serialization.PublicFormat.OpenSSH
)

# Salvar a chave pública em um arquivo
with open('public_key.openssh', 'wb') as f:
    f.write(public_key_ssh)

print("Chaves geradas com sucesso: private_key.openssh e public_key.openssh")
