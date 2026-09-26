class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check to see if lengths of strings are equal
        if len(s) != len(t):
            return False
        
        # dictionaries for both s & t counts
        s_counts, t_counts = {}, {}

        # since the string lengths are equal, you can iterate over just s
        for i in range(len(s)):
            # index the dict with key (s[i]), get values with (.get())
            # the 0 is the default value if there's no value associated with key already
            s_counts[s[i]] = s_counts.get(s[i], 0) + 1

            # same thing for t
            t_counts[t[i]] = t_counts.get(t[i], 0) + 1
        
        return s_counts == t_counts



        