from shutil import get_terminal_size
from fill_gallon import fill_gallon


def main():
    hyphens = "-" * get_terminal_size().columns


    print(f"\n{hyphens}")
    print("Digite o volume do galão e das garrafas para encontrar a melhor combinação de preenchimento.")
    print(f"{hyphens}\n")


    gallon  = input("Litros do galão: ")
    bottles = input("Litros das garrafas (por vírgula): ")


    if not (gallon and bottles):
        print(f"\n{hyphens}")
        print("Valores inválidos! Forneça o galão e as garrafas.")
        print(f"{hyphens}")

        exit()


    response = fill_gallon(gallon, bottles)


    if response:
        print(f"\n{hyphens}")
        print(f"Garrafas: {response[0]}, Sobra: {response[1]}")
        print(f"{hyphens}")
    else:
        print(f"\n{hyphens}")
        print("Não foi possível preencher o volume em litros para o galão e garrafas fornecidas.")
        print(f"{hyphens}")


if __name__ == "__main__":
    main()
