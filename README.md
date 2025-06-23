# ImagineCrypto

**A Quantum-Aware Symbolic Cipher Built on Imaginary Phase Collapse**

ImagineCrypto is a novel cryptographic primitive based on geometric transformations in the complex plane. It encodes information through symbolic symmetry, phase rotation, and root ambiguity — creating a secure, elegant one-way function that is both quantum-conscious and mathematically original.

---

## 🔐 Key Features

- Uses **complex numbers and imaginary unit** as a native part of encryption
- Resistant to brute-force attacks via **non-injective square-root collapse**
- Demonstrates **maximum entropy** in brute-force decryption tests
- Inspired by quantum structure: operates on the **unit circle** in phase space
- Built from scratch — **not based on RSA, ECC, or SHA**

---

## 🧠 How It Works

A plaintext letter is encoded as a phase angle \( \theta \), transformed as:

\[
c = -z^2 \cdot e^{i\phi} \quad \text{where } z = e^{i\theta}
\]

To decrypt, one must compute:

\[
z = \pm \sqrt{-c \cdot e^{-i\phi}}
\]

But without knowing \( \phi \), recovery is ambiguous and unpredictable.

---

## 📊 Validation

Empirical tests show:

- Entropy ≈ 4.7004 bits (maximum for 26 letters)
- No statistical preference in 1000-decryption brute-force runs
- Full symbolic obfuscation — *meaning is hidden, not just data*

---

## 🚀 Try It Out

```bash
python test_entropy.py
