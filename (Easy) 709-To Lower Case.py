"""
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"
"""

"""
Author: iscclin (Github)
Date: 2018-11-07
"""

"""
ASCII:
    A~Z -> 65~90
    a~z -> 97~122
"""
class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        result = '';
        for ch in str:
            if ord(ch)>=65 and ord(ch)<=90 :
                result += chr(ord(ch)+32);
            else:
                result += ch;
        return result
                
"""
32ms
"""
        
