# test_entropy.py
"""
Empirical entropy test for ImagineCrypto
Validates one-wayness and statistical obfuscation of symbolic encryption.
"""

import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from imaginecrypto import encrypt_letter, decrypt_letter, LETTERS
from math import log2

# --- Config ---
phi_guesses = 10000
np.random.seed(42)

def shannon_entropy(counter):
    total = sum(counter.values())
    probs = [v / total for v in counter.values()]
    return -sum(p * log2(p) for p in probs if p > 0)

def test_entropy_for_letter(letter, true_phi):
    counts = Counter()
    ciphertext = encrypt_letter(letter, true_phi)

    for _ in range(phi_guesses):
        guess_phi = np.random.uniform(0, 2 * np.pi)
        guessed = decrypt_letter(ciphertext, guess_phi)
        counts[guessed] += 1

    entropy = shannon_entropy(counts)
    correct_count = counts[letter]
    max_other = max(v for k, v in counts.items() if k != letter)

    return letter, correct_count, max_other, entropy, counts


def main():
    print("🔐 Symmetry-Collapse Cipher Entropy Test")
    print(f"Running {phi_guesses} brute-force attempts per letter...\n")

    true_phi = np.random.uniform(0, 2 * np.pi)
    summary = []

    for letter in LETTERS:
        result = test_entropy_for_letter(letter, true_phi)
        summary.append(result)
        l, correct, other, ent, _ = result
        print(f"[{l}] Correct: {correct}, Max Other: {other}, Entropy: {ent:.4f}")

    # Print table summary
    print("\n🔍 Summary:")
    print(f"{'Letter':<6} {'Correct':<8} {'MaxOther':<10} {'Entropy (bits)'}")
    for l, c, m, e, _ in summary:
        print(f"{l:<6} {c:<8} {m:<10} {e:.4f}")

    # Optional plot: Frequency guess for one letter
    focus = 'H'
    focus_data = next(r for r in summary if r[0] == focus)
    _, _, _, _, focus_counts = focus_data

    plt.bar(focus_counts.keys(), focus_counts.values(), color='skyblue')
    plt.title(f"Letter guess frequency for ciphertext of '{focus}'")
    plt.xlabel("Guessed Letter")
    plt.ylabel("Frequency")
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.show()


if __name__ == "__main__":
    main()
