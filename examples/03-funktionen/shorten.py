def shorten(long_str):
    if len(long_str) > 2:  # only useful for strings with at least 3 characters
        # return the first, last character and in between the number of left out characters
        rv = f"{long_str[0]}{len(long_str) - 2}{long_str[-1]}"
    else:
        rv = long_str
    return rv