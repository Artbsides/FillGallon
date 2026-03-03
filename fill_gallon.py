from itertools import combinations


def fill_gallon(gallon: str, bottles: str) -> list | None:
    gallon = float(gallon)
    bottles = list(map(float, bottles.split(",")))

    results = []

    #
    # Gera todas as combinações de garrafas possíveis e
    # calcula o volume total para cada uma delas
    #

    for i in range(1, len(bottles) + 1):
        for combination in combinations(bottles, i):
            calc = sum(combination)

            if calc >= gallon:
                results.append(
                    (calc - gallon, len(combination), combination)  # Sobra, quantidade de garrafas e combinação (garrafas utilizadas)
                )

    if results:
        (
            rest,
            used_bottles_len,
            used_bottles
        ) = min(results)  # Seleciona a combinação com menor sobra ou menor quantidade de garrafas

        return list(used_bottles), rest

    return None
