import csv


# Funkce pro načtení dat ze souboru CSV 

def load_data(file_path):
    with open(file_path, newline='') as csvfile:
        data = list(csv.reader(csvfile))
    return data

    # Funkce pro nalezení vzorů 


def find_patterns(data):
    header = data[0]
    patterns = []

    # Projdeme každý sloupec kromě prvního, který obsahuje názvy sloupců 
    for col_idx in range(0, len(header)):
        column_values = [row[col_idx] for row in data[1:]]  # Hodnoty ve sloupci 
        total_count = len(column_values)
        unique_values = set(column_values)

        # Pro každou jedinečnou hodnotu ve sloupci 
        for value in unique_values:
            value_count = column_values.count(value)

            # Pokud podíl výskytů této hodnoty ve sloupci přesahuje 60% 
            if value_count / total_count >= 0.6:
                pattern = {
                    "column_name": header[col_idx],
                    "value": value,
                    "percentage": value_count / total_count
                }
                patterns.append(pattern)

    return patterns

    # Hlavní program 


if __name__ == "__main__":
    file_path = "data.csv"
    data = load_data(file_path)
    patterns = find_patterns(data)

    # Výpis nalezených vzorů 
    print("Nalezené vzory:")
    for pattern in patterns:
        print(f"Sloupec: {pattern['column_name']}, Hodnota: {pattern['value']}, Podíl: {pattern['percentage'] * 100}%")
