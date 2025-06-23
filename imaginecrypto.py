# imaginecrypto.py

import cmath
import numpy as np

# Constants
LETTERS = [chr(i) for i in range(65, 91)]  # 'A' to 'Z'
ANGLE_STEP = 2 * np.pi / 26
ANGLE_MAP = {letter: i * ANGLE_STEP for i, letter in enumerate(LETTERS)}

def encrypt_letter(letter: str, phi: float) -> complex:
    """
    Encrypt a single capital letter using the symmetry-collapse cipher.
    
    Args:
        letter (str): A single capital letter A-Z
        phi (float): Secret phase key (radians)
    
    Returns:
        complex: Encrypted complex number
    """
    theta = ANGLE_MAP[letter.upper()]
    z = cmath.exp(1j * theta)
    c = -z**2 * cmath.exp(1j * phi)
    return c


def decrypt_letter(cipher: complex, phi: float) -> str:
    """
    Decrypt a single complex value assuming known phase key.
    May return ambiguous results due to ± root symmetry.

    Args:
        cipher (complex): Ciphertext value
        phi (float): Secret phase key (radians)

    Returns:
        str: Most likely original letter (based on angle matching)
    """
    # Reverse the collapse: z² = -cipher * e^(-iφ)
    z_squared = -cipher * cmath.exp(-1j * phi)
    candidates = [
        cmath.sqrt(z_squared),
        -cmath.sqrt(z_squared)
    ]

    # Find which candidate angle matches closest to known letters
    best_match = None
    min_diff = float('inf')

    for candidate in candidates:
        angle = np.angle(candidate) % (2 * np.pi)
        for letter, target_angle in ANGLE_MAP.items():
            diff = min(abs(angle - target_angle), 2 * np.pi - abs(angle - target_angle))
            if diff < min_diff:
                min_diff = diff
                best_match = letter

    return best_match


def encrypt_message(message: str, phi: float) -> list:
    """
    Encrypt a string message.

    Args:
        message (str): All capital letters
        phi (float): Shared phase key

    Returns:
        list of complex: Ciphertext values
    """
    return [encrypt_letter(c, phi) for c in message if c.upper() in ANGLE_MAP]


def decrypt_message(ciphertext: list, phi: float) -> str:
    """
    Decrypt a list of complex numbers.

    Args:
        ciphertext (list of complex): Ciphertext values
        phi (float): Shared phase key

    Returns:
        str: Decrypted message
    """
    return ''.join(decrypt_letter(c, phi) for c in ciphertext)
