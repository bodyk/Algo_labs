def rabin_karp_search(haystack, needle):
    if haystack == "" or needle == "" or len(needle) > len(haystack):
        return []

    base = 256  # Number of characters in the input alphabet
    prime = 101  # A prime number
    m, n = len(needle), len(haystack)

    # Hash value for pattern and text
    p = t = 0
    h = 1
    result = []

    # The value of h would be "pow(d, M-1)%q"
    for i in range(m-1):
        h = (h * base) % prime

    # Calculate the hash value of pattern and first window of text
    for i in range(m):
        p = (base * p + ord(needle[i])) % prime
        t = (base * t + ord(haystack[i])) % prime

    # Slide the pattern over text one by one
    for i in range(n - m + 1):
        # Check the hash values of current window of text and pattern
        # If the hash values match then only check for characters one by one
        if p == t:
            # Check for characters one by one
            if haystack[i:i+m] == needle:
                result.append(i)

        # Calculate hash value for next window of text: Remove leading digit,
        # add trailing digit
        if i < n - m:
            t = (base * (t - ord(haystack[i]) * h) + ord(haystack[i + m])) % prime

            # We might get negative value of t, converting it to positive
            if t < 0:
                t = t + prime

    return result

# Example usage
haystack = "ABABDABACDABABCABAB"
needle = "ABABCABAB"
result = rabin_karp_search(haystack, needle)
print(result)