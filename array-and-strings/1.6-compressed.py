def compress(s):
    S = len(s)

    result = []
    count = 1

    for i in xrange(1, S):
        if s[i-1] != s[i]:
            result.append(s[i-1])
            result.append(count)
            count = 1
        else:
            count += 1

        if i == S-1:
            result.append(s[i])
            result.append(count)

    if len(result) < S:
        return "".join(map(str, result))

    return s


if __name__ == "__main__":
    for val in ["abbccccccd", "abbbb", "aab", "aaaaab"]:
        print compress(val)
