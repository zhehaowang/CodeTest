"""
Minglish lesson
===============

Welcome to the lab, minion. Henceforth you shall do the bidding of Professor Boolean. Some say he's mad, trying to develop a zombie serum and all... but we think he's brilliant! 

First things first - Minions don't speak English, we speak Minglish. Use the Minglish dictionary to learn! The first thing you'll learn is how to use the dictionary.

Open the dictionary. Read the page numbers, figure out which pages come before others. You recognize the same letters used in English, but the order of letters is completely different in Minglish than English (a < b < c < ...).

Given a sorted list of dictionary words (you know they are sorted because you can read the page numbers), can you find the alphabetical order of the Minglish alphabet? For example, if the words were ["z", "yx", "yz"] the alphabetical order would be "xzy," which means x < z < y. The first two words tell you that z < y, and the last two words tell you that x < z.

Write a function answer(words) which, given a list of words sorted alphabetically in the Minglish alphabet, outputs a string that contains each letter present in the list of words exactly once; the order of the letters in the output must follow the order of letters in the Minglish alphabet. 

The list will contain at least 1 and no more than 50 words, and each word will consist of at least 1 and no more than 50 lowercase letters [a-z]. It is guaranteed that a total ordering can be developed from the input provided (i.e. given any two distinct letters, you can tell which is greater), and so the answer will exist and be unique.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (string list) words = ["y", "z", "xy"]
Output:
    (string) "yzx"

Inputs:
    (string list) words = ["ba", "ab", "cb"]
Output:
    (string) "bac"
"""

# The idea seems correct but the implementation seems more cumbersome than needed; and may have not 
def answer(words):
    # your code here
    if len(words) == 1:
        return words[0]
    adj_list = dict()
    
    def helper(words):
        size = len(words)
        if size < 2:
            return
        next_words = []
        current_begin = words[0][0]
        if len(words[0]) > 1 and len(words[1]) > 1 and words[0][0] == words[1][0]:
            next_words = [words[0][1:]]
        for i in range(1, size):
            if current_begin != words[i][0]:
                if not (current_begin in adj_list):
                    adj_list[current_begin] = {"next": [words[i][0]], "degree": 0}
                    if words[i][0] in adj_list:
                        adj_list[words[i][0]]["degree"] += 1
                    else:
                        adj_list[words[i][0]] = {"next": [], "degree": 1}
                elif not (words[i][0] in adj_list[current_begin]["next"]):
                    adj_list[current_begin]["next"].append(words[i][0])
                    if words[i][0] in adj_list:
                        adj_list[words[i][0]]["degree"] += 1
                    else:
                        adj_list[words[i][0]] = {"next": [], "degree": 1}
                current_begin = words[i][0]
                helper(next_words)
                if len(words[i]) > 1 and len(words) > i + 1 and len(words[i + 1]) > 1 and words[i][0] == words[i + 1][0]:
                    next_words = [words[i][1:]]
                else:
                    next_words = []
            else:
                if len(words[i]) > 1:
                    next_words.append(words[i][1:])
        helper(next_words)
        next_words = []
    
    helper(words)
    
    start = None
    for key in adj_list:
        if adj_list[key]["degree"] == 0:
            start = key
    stack = [start]
    result = ""
    while len(stack) > 0:
        key = stack.pop()
        result += key
        for item in adj_list[key]["next"]:
            adj_list[item]["degree"] -= 1
            if adj_list[item]["degree"] == 0:
                stack.append(item)
        del adj_list[key]
    return result

if __name__ == "__main__":
    # print answer(["ab", "ba"])
    # print answer(["ac", "b", "bb"])
    # print answer(["ac", "ab"])
    
    # print answer(["y", "xy"])
    # print answer(["y", "z", "xy"])
    # print answer(["ba", "ab", "cb"])
    
    # print answer(["bc", "d", "db"])
    # print answer(["abc", "ad", "adb", "cd", "b", "d"])
    print answer(["aaa", "aad", "bab", "bad"])