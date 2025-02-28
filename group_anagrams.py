# 3. Given an array of strings strs, group the anagrams together.
#    You can return the answer in any order.
#    An Anagram is a word or phrase formed by rearranging the letters
#    of a different word or phrase, typically using all the original letters exactly once.

#     Constraints:
#         - 1 <= strs.length <= 104
#         - 0 <= strs[i].length <= 100
#         - strs[i] consists of lowercase English letters.

#     Example 1:
#         - Input: strs = ["eat","tea","tan","ate","nat","bat"]
#         - Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

#     Example 2:
#         - Input: strs = [""]
#         - Output: [[""]]

#     Example 3:
#         - Input: strs = ["a"]
#         - Output: [["a"]]


from collections import defaultdict
from typing import List

def group_anagram (strings :List[str]) -> List[List[str]]:
    """
    Groups a list of strings into anagrams.

    Parameters:
    strings (List[str]): A list of strings.

    Returns:
    List[List[str]]: A list of lists, where each list contains words that are anagrams of each other.
    """

    # Using a defaultdict to avoid the key value error and automatically initialize a list if a new key is encountered.
    dict = defaultdict(list)

    for word in strings:

        # Sort the word and use the tuple as the key
        sorted_word = sorted(word)
        key = tuple(sorted_word)

        # Grouping the anagrams based on their sorted value
        dict[key].append(word)

     # Return the grouped anagrams
    return list(dict.values())

test_case = ["eat","tea","tan","ate","nat","bat"]
print(f"Given below is a example Test case: \nInput : {test_case}")
print("Output:", group_anagram(test_case))

def main():

    n = int(input("To enter a custom input, Please enter the number of words you want to add: "))
    words = []
    for i in range(n):
        word = input(f"Enter the word {i+1}: ")
        words.append(word)

    print(group_anagram(words))

if __name__ == '__main__':
    main()