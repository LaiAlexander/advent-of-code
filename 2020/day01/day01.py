with open("input.txt", "r") as file:
    # data = []
    # for item in file.readlines():
    #     data.append(int(item))

    YEARS = [int(item) for item in file.readlines()]

def find_product1(years, my_sum, num_of_factors):
    """
    Simple solution.
    """
    for year1 in years:
        for year2 in years:
            if num_of_factors == 2:
                if year1 + year2 == my_sum:
                    print(f"{year1} + {year2} = {year1 + year2}")
                    print(f"{year1} * {year2} = {year1 * year2}")
                    return
            if num_of_factors == 3:
                for year3 in years:
                    if year1 + year2 + year3 == my_sum:
                        print(f"{year1} + {year2} + {year3} = {year1 + year2 + year3}")
                        print(f"{year1} * {year2} * {year3} = {year1 * year2 * year3}")
                        return

def find_product2(years, my_sum, num_of_factors):
    """
    A bit more efficient solution. No need to compare values that have already been compared.
    """
    for i in range(len(years)):
        for j in range(i + 1, len(years)):
            if num_of_factors == 2:
                if years[i] + years[j] == my_sum:
                    print(f"{years[i]} + {years[j]} = {years[i] + years[j]}")
                    print(f"{years[i]} * {years[j]} = {years[i] * years[j]}")
                    return
            elif num_of_factors == 3:
                for k in range(j + 1, len(years)):
                    if years[i] + years[j] + years[k] == my_sum:
                        print(f"{years[i]} + {years[j]} + {years[k]}"
                              f"= {years[i] + years[j] + years[k]}")
                        print(f"{years[i]} * {years[j]} * {years[k]}"
                              f"= {years[i] * years[j] * years[k]}")
                        return

def find_product3(years, my_sum, num_of_factors):
    """
    More concise solution, making use of generator expressions.
    """
    if num_of_factors == 2:
        product = (x * y for x in years for y in years
                   if x + y == my_sum)
    elif num_of_factors == 3:
        product = (x * y * z for x in years for y in years for z in years
                   if x + y + z == my_sum)
    print(next(product))


find_product1(YEARS, 2020, 2)
find_product1(YEARS, 2020, 3)
find_product2(YEARS, 2020, 2)
find_product2(YEARS, 2020, 3)
find_product3(YEARS, 2020, 2)
find_product3(YEARS, 2020, 3)
