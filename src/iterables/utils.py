from itertools import combinations

def iterables(letters, k):
        # Total combinations
        all_combinations = list(combinations(letters, k))

        # Filter combinations that contain at least one 'a'
        favorable = [c for c in all_combinations if 'a' in c]

        # Probability = favorable / total
        probability = len(favorable) / len(all_combinations)

        # Print rounded to 4 decimal places
        return f"{probability:.4f}"
