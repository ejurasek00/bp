from itertools import combinations
from collections import defaultdict

# Přeformátování dat
data = [
    "354C31,DBCEEF,6CE255,199D26,D59553,331981,869F50",
    "B2895C,B0FAAD,9ED0E8,D11884,269963,ADC8A2,999999",
    "1520D1,49E95E,A6463C,D11884,269963,ADC8A2,999999",
    "0BEA8D,B0FAAD,A6463C,D11884,269963,ADC8A2,999999",
    "7EA60D,B0FAAD,C5B9CC,D11884,269963,420666,999999"
]

transactions = [line.split(",") for line in data]


# Apriori algoritmus
min_support = 2
item_counts = defaultdict(int)

# Výpočet podpory pro jednotlivé položky
for transaction in transactions:
    for item in transaction:
        item_counts[item] += 1

# Filtrování položek podle minimální podpory
frequent_items = {item for item, count in item_counts.items() if count >= min_support}

# Výpočet častých itemsetů
frequent_itemsets = []
for size in range(2, len(frequent_items) + 1):
    for itemset in combinations(frequent_items, size):
        support = sum(all(item in transaction for item in itemset) for transaction in transactions)
        if support >= min_support:
            frequent_itemsets.append((itemset, support))

# Výpis výsledků
for itemset, support in frequent_itemsets:
    print("Frequent Itemset:", ", ".join(itemset), "Support:", support)
