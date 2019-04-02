#!/usr/bin/env python


def is_anagram(s1, s2):
    if sorted(s1) == sorted(s2):
        return True
    return False


def all_anagrams(s, p):
    """
    Given a string s and a non-empty string p, find all the start indices of p's anagrams in s
    Reference: http://bookshadow.com/weblog/2016/10/23/leetcode-find-all-anagrams-in-a-string/
    """
    import collections
    ls, lp = len(s), len(p)
    cp = collections.Counter(p)
    count = 0
    result = []
    for i in range(ls):
        if cp[s[i]] >= 1:
            count += 1
        cp[s[i]] -= 1
        if i >= lp:
            if cp[s[i-lp]] >= 0:
                count -= 1
            cp[s[i-lp]] += 1
        if count == lp:
            result.append(i-lp+1)
    return result


def all_anagrams_v1(s, p):
    result = []
    for i in range(len(s)-len(p)+1):
        s1 = s[i:i+len(p)]
        if is_anagram(s1,p):
            result.append(i)
    return result


def anagrams(strs):
    """
    Given an array of strings, return all groups of strings that are anagrams.
    """
    pass

if __name__ == "__main__":
    a = "abc"
    b = "cba"
    assert is_anagram(a, b) == True
    c = "abc"
    d = "ac"
    assert is_anagram(c, d) == False
    s = "cbaebabacd"
    p = "abc"
    result = all_anagrams(s, p)
    print(result)
    assert result == [0, 6]
    s = "abab"
    p = "ab"
    result = all_anagrams(s, p)
    print(result)
    assert result == [0, 1, 2]
