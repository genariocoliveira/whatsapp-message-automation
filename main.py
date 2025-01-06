import pywhatkit as kit
from datetime import datetime
import time

# Dicionário de funcionários e seus números
funcionarios = {
    "name": "+55 DDD number"
}

def validar_numero(numero):
    """Valida se o número de telefone está no formato cor
    reto"""
    numero = numero.replace(" ", "")
    if not numero.startswith("+"):
        return False
    numero = numero[1:]  # Remove o '+'
    return numero.isdigit()

def enviar_mensagem(funcionarios, mensagem):
    try:
        # Verifica se há funcionários cadastrados
        if not funcionarios:
            print("Não há funcionários cadastrados no sistema.")
            return

        # Exibe os funcionários disponíveis
        print("\nFuncionários disponíveis para receber a mensagem:")
        for i, nome in enumerate(funcionarios.keys(), 1):
            print(f"{i}. {nome} - {funcionarios[nome]}")

        # Solicita ao usuário para escolher quem vai receber a mensagem
        while True:
            escolhas = input("\nDigite os números correspondentes aos funcionários (separados por vírgula): ")
            if escolhas.strip():
                break
            print("Por favor, digite pelo menos um número.")

        escolhas = [choice.strip() for choice in escolhas.split(',')]

        # Envia a mensagem para os funcionários escolhidos
        for escolha in escolhas:
            try:
                indice = int(escolha) - 1
                if 0 <= indice < len(funcionarios):
                    nome_selecionado = list(funcionarios.keys())[indice]
                    numero_telefone = funcionarios[nome_selecionado]
                    
                    if not validar_numero(numero_telefone):
                        print(f"Erro: Número inválido para {nome_selecionado}")
                        continue

                    print(f"\nEnviando mensagem para {nome_selecionado} ({numero_telefone})...")
                    
                    # Envia a mensagem pelo WhatsApp
                    kit.sendwhatmsg_instantly(
                        numero_telefone, 
                        mensagem,
                        wait_time=10,  # Tempo de espera reduzido para 10 segundos
                        tab_close=True  # Fecha a aba após enviar
                    )
                    
                    print(f"Mensagem enviada com sucesso para {nome_selecionado}!")
                    time.sleep(2)  # Pequena pausa entre envios
                else:
                    print(f"Erro: Número {escolha} não corresponde a nenhum funcionário.")
            
            except ValueError:
                print(f"Erro: '{escolha}' não é um número válido.")
            except Exception as e:
                print(f"Erro ao enviar mensagem para funcionário {escolha}: {str(e)}")

    except Exception as e:
        print(f"Erro inesperado: {str(e)}")

def main():
    try:
        # Solicita ao usuário a mensagem que será enviada
        while True:
            mensagem = input("\nDigite a mensagem que você deseja enviar: ")
            if mensagem.strip():
                break
            print("A mensagem não pode estar vazia.")

        # Chama a função para enviar a mensagem para os funcionários selecionados
        enviar_mensagem(funcionarios, mensagem)

    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário.")
    except Exception as e:
        print(f"Erro no programa principal: {str(e)}")

if __name__ == "__main__":
    main()