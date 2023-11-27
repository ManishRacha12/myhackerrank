def substring_game(string):
    s = string
    length = len(s)
    alice_score, bob_score = 0, 0

    for i in range(length):
        for j in range(i + 1, length + 1):
            substring = s[i:j]
            if len(substring) % 2 == 0:
                alice_score += 1
            else:
                bob_score += 1

    if alice_score > bob_score:
        return f"Alice_score {alice_score}"
    elif bob_score > alice_score:
        return f"Bob_score {bob_score}"
    else:
        return "Draw"

# Example usage:
result = substring_game("hello")
print(result)
