def countstrings(stringlist):
    count = 0
    for string in stringlist:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count

words = ["aba", "xyz", "timothy", "jayden", "madam", "aaa", "xyx"]
print(f"Numbers of string are: {countstrings(words)}")
