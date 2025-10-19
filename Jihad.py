import string
import secrets

def evaluate_password(pw):
    """Return 'Strong' or 'Weak'."""
    length_ok = len(pw) >= 8
    has_lower = any(c.islower() for c in pw)
    has_upper = any(c.isupper() for c in pw)
    has_digit = any(c.isdigit() for c in pw)
    has_symbol = any(c in string.punctuation for c in pw)

    score = sum([length_ok, has_lower, has_upper, has_digit, has_symbol])
    return "Strong" if score >= 4 else "Weak"

def suggest_password(length=12):
    """Return a suggested strong password."""
    if length < 8:
        length = 8
    alphabet = string.ascii_letters + string.digits + string.punctuation
    # ensure categories present
    pw = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation),
    ]
    while len(pw) < length:
        pw.append(secrets.choice(alphabet))
    secrets.SystemRandom().shuffle(pw)
    return "".join(pw)

if name == "main":
    pw = input("Enter password: ").strip()
    result = evaluate_password(pw)
    print("Result:", result)
    if result == "Weak":
        print("Suggested stronger password:", suggest_password(14))
