"""helpers"""

def remove_non_duplicates(dic: dict) -> dict:
    """Remove non-duplicate values and return a new dict sorted by key."""
    if not isinstance(dic, dict):
        raise TypeError("Input must be a dictionary")
    filtered = {k: v for k, v in dic.items() if len(v) >= 2}
    return dict(sorted(filtered.items()))

def get_unique_pairs(li: list) -> dict:
    """return possible pairs"""

    sum_pairs: dict = {}
    n: int = len(li)

    for i in range(n):
        for j in range(i + 1, n):
            pair_sum: int = li[i] + li[j]
            if pair_sum not in sum_pairs:
                sum_pairs[pair_sum] = []
            sum_pairs[pair_sum].append((li[i], li[j]))

    # Remove pairs with only one occurrence and sort ascending
    sum_pairs: dict = remove_non_duplicates(sum_pairs)
    return sum_pairs

def print_equal_sums(sum_pairs: dict):
    """output pairs with equal sums"""
    if not sum_pairs:
        print("No pairs with equal sums found.")
        return
    for pair_sum, pairs in sum_pairs.items():
        print("Pairs : ", end="")
        for i, pair in enumerate(pairs):
            print(f"( {pair[0]}, {pair[1]})", end="")
            if i < len(pairs) - 1:
                print(" ", end="")
        print(f" have sum : {pair_sum}")
    