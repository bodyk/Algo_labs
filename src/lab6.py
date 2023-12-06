def calculate_hash(s, base, prime):
    hash_value = 0
    for char in s:
        hash_value = (base * hash_value + ord(char)) % prime
    return hash_value

def recalculate_hash(old_hash, old_char, new_char, h, base, prime):
    new_hash = (base * (old_hash - ord(old_char) * h) + ord(new_char)) % prime
    if new_hash < 0:
        new_hash += prime
    return new_hash

def rabin_karp_search(text, pattern):
    if not text or not pattern or len(pattern) > len(text):
        return []

    base = 256
    prime = 101
    pattern_hash = calculate_hash(pattern, base, prime)
    window_hash = calculate_hash(text[:len(pattern)], base, prime)

    h = pow(base, len(pattern) - 1, prime)
    results = []
    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash == window_hash:
            if text[i:i + len(pattern)] == pattern:
                results.append(i)
        if i < len(text) - len(pattern):
            window_hash = recalculate_hash(window_hash, text[i], text[i + len(pattern)], h, base, prime)

    return results

# Example usage
if __name__ == "__main__":
    sample_text = "ABAAABCDABCD"
    sample_pattern = "ABC"
    print("Occurrences at indices:", rabin_karp_search(sample_text, sample_pattern))
