class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove the spaces and punctuation from string
        string = ""
        for char in s:
            if char.isalnum():
                string += char.lower()
        # print(string)
        # print(string[::-1])
        return string == string[::-1]

        