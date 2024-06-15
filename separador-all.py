import os

def search_passwords(output_file):
    separator = "Separator Logins CloudLogs by Destroyer"
    current_directory = os.getcwd()
    with open(output_file, 'w', encoding='utf-8') as output:
        output.write(separator + "\n")
    print(separator)

    try:
        # Percorre o diretório e suas subpastas
        for entry in os.scandir(current_directory):
            if entry.is_dir():
                for root, dirs, files in os.walk(entry.path):
                    for file in files:
                        if file == "Passwords.txt":
                            file_path = os.path.join(root, file)
                            try:
                                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                                    lines = f.readlines()
                                    for i, line in enumerate(lines):
                                        if "Username: " in line:
                                            username = line.split("Username: ")[1].strip()
                                            if "@" in username:
                                                password = lines[i+1].split("Password: ")[1].strip()
                                                login_info = f"{username}|{password}\n"
                                                with open(output_file, 'a', encoding='utf-8') as output:
                                                    output.write(login_info)
                                                print(f"\033[92m[+]\033[0m Login encontrado e salvo: {login_info.strip()}")
                                        else:
                                            print(f"\033[91m[-]\033[0m Não foi possível encontrar login no arquivo: {file_path}")
                            except Exception as e:
                                print(f"\033[91m[-]\033[0m Erro ao processar o arquivo {file_path}: {e}")

    except Exception as e:
        print(f"\033[91m[-]\033[0m Erro ao percorrer o diretório: {e}")

if __name__ == "__main__":
    output_file = input("Digite o caminho para o arquivo de saída: ")
    search_passwords(output_file)
