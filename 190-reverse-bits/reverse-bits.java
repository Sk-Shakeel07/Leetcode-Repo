public class Solution {
    // you need to treat n as an unsigned value
    public int reverseBits(int n) {
        int result = 0;
        for (int i = 0; i < 32; i++) {
            result <<= 1; // Shift result left to make space for the next bit
            result |= (n & 1); // Extract the last bit of n and add it to result
            n >>>= 1; // Unsigned right shift n to process the next bit
        }
        return result;
    }
}
