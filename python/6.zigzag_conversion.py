# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

class Solution:
    # @return a string

    def locationGenerator(self, nRows):
        while True:
            for i in range(nRows):
                yield i
            
            for i in range(nRows - 2, 0, -1):
                yield i


    def convert(self, s, nRows):
        output = [''] * nRows
        locationGenerator = self.locationGenerator(nRows)

        for char in s:
            n = locationGenerator.next()
            output[n] += char
        
        return ''.join(output)

s = Solution()
print s.convert('PAYPALISHIRING', 3)
