def is_palindrome_lat(input_str):
    uni_lat = list(range(97, 123))

    lc_lat_chars = ""

    for i in input_str:
        if ord(i) in uni_lat:
            lc_lat_chars += i

    if lc_lat_chars == lc_lat_chars[::-1]:
        return True

    return False


# def another_way(str):
#     lat_chars = "".join(char for char in str if char >= "a" and char <= "s")
#     return lat_chars == lat_chars[::-1]

input_str = "abcфафасяABCDdcba"

print(is_palindrome_lat(input_str))
