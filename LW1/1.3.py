def is_palindrome_lat(str):
    uni_lat = list(range(97, 123))

    lc_lat_chars = ""

    for i in str:
        if ord(i) in uni_lat:
            lc_lat_chars += i

    if lc_lat_chars == lc_lat_chars[::-1]:
        return True

    return False


# def another_way(str):
#     lat_chars = "".join(char for char in str if char >= "a" and char <= "s")
#     return lat_chars == lat_chars[::-1]

str = "abcфафасяABCDdcba"

print(is_palindrome_lat(str))
