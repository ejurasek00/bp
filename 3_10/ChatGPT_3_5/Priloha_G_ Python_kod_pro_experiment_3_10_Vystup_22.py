from collections import Counter

def parse_transactions(data):
    transactions = []
    for line in data.split('\n')[1:]:
        items = line.strip().split(',')
        transactions.append(items)
    return transactions

def find_frequent_itemsets(transactions, min_support):
    # Spočítání počtu výskytů jednotlivých položek
    item_counts = Counter(item for transaction in transactions for item in transaction)
    
    # Filtrace častých itemsetů
    frequent_itemsets = {item: count for item, count in item_counts.items() if count >= min_support}
    
    return frequent_itemsets

# Zadaná data
data = """354C31,DBCEEF,6CE255,199D26,D59553,331981,869F50
B2895C,B0FAAD,9ED0E8,D11884,269963,ADC8A2,999999
1520D1,49E95E,A6463C,D11884,269963,ADC8A2,999999
0BEA8D,B0FAAD,A6463C,D11884,269963,ADC8A2,999999
7EA60D,B0FAAD,C5B9CC,D11884,269963,420666,999999"""

# Převedení dat
transactions = parse_transactions(data)

# Nalezení častých itemsetů délky 1 s minimální podporou 2
min_support = 2
frequent_itemsets = find_frequent_itemsets(transactions, min_support)

# Výstup
print("Časté itemsety délky 1 s minimální podporou 2:")
for item, support in frequent_itemsets.items():
    print(f"{item}: {support}")
