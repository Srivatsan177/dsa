if __name__ == "__main__":
    s = "abcabcbb"
    char_index = {}
    max_len = 0
    start_index, end_index = 0, 0
    for idx,char in enumerate(s):
        if char not in char_index:
            char_index[char] = idx
            max_len = max(max_len, idx - start_index + 1)
            end_index = idx
        else:
            start_index = char_index[char] + 1
            char_index[char] = idx
    print(max(max_len, end_index - start_index))