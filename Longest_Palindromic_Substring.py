class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Helper function to expand from the center and return the longest palindrome found
        def expand_from_center(left: int, right: int) -> str:
            # Expand as long as the characters on both sides match and are within bounds
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1  # Move left pointer outward
                right += 1 # Move right pointer outward
            # Return the palindrome substring between the last valid pointers
            return s[left + 1:right]

        # Variable to track the longest palindromic substring found so far
        longest = ""

        # Iterate over every character in the string to consider all possible centers
        for i in range(len(s)):
            # -------------------------------------------------------
            # Case 1: Odd-length palindromes (single character center)
            # Example: For "racecar", center at 'e' => expand around same index
            odd_palindrome = expand_from_center(i, i)

            # Case 2: Even-length palindromes (center between two characters)
            # Example: For "abba", center between 'b' and 'b'
            even_palindrome = expand_from_center(i, i + 1)
            # -------------------------------------------------------

            # Compare and keep the longer palindrome of the two cases
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome
            if len(even_palindrome) > len(longest):
                longest = even_palindrome

        # Return the longest palindromic substring found
        return longest
