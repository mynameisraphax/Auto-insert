def remove_linhas_repetidas(arquivo_entrada, arquivo_saida):
    try:
        # Abrir arquivo de entrada para leitura
        with open(arquivo_entrada, 'r') as f:
            linhas = f.readlines()

        # Remover linhas duplicadas
        linhas_sem_repeticao = list(set(linhas))

        # Abrir arquivo de saída para escrita
        with open(arquivo_saida, 'w') as f:
            f.writelines(linhas_sem_repeticao)

        print("Linhas repetidas removidas com sucesso!")
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print("Ocorreu um erro:", e)

if __name__ == "__main__":
    arquivo_entrada = input("Digite o nome do arquivo de entrada: ")
    arquivo_saida = input("Digite o nome do arquivo de saída: ")

    remove_linhas_repetidas(arquivo_entrada, arquivo_saida)
