import operator


def solve_bf(words, duplicates=False):
    answer = []
    answer_length = 0

    comparer = operator.eq if duplicates else operator.is_

    for word1 in words:
        for word2 in words:
            if comparer(word1, word2):
                continue

            min_len = answer_length
            max_len = min(len(word1), len(word2))
            for length in range(max_len, min_len, -1):
                substr = word1[:length]
                if word2.endswith(substr):
                    answer_length = length
                    answer = [word1, word2]
                    break

    if answer_length:
        return (answer, answer_length)

    return None


def solve_hash(words, duplicates=False):
    answer = []
    answer_length = 0

    prefixes = {}
    for word in words:
        for length in range(1, len(word) + 1):
            prefix = word[:length]
            if prefix not in prefixes:
                prefixes[prefix] = set()

            prefixes[prefix].add(word)

    comparer = operator.eq if duplicates else operator.is_

    for word2 in words:
        min_len = answer_length
        max_len = len(word2)
        for length in range(max_len, min_len, -1):
            substr = word2[-length:]
            substr_found = False

            if substr in prefixes:
                for word1 in prefixes[substr]:
                    if not comparer(word1, word2):
                        answer_length = length
                        answer = [word1, word2]
                        substr_found = True
                        break

            if substr_found:
                break

    if answer_length:
        return (answer, answer_length)

    return None
