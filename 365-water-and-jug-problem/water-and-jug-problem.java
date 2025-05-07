class Solution {
    public boolean canMeasureWater(int x, int y, int target) {
        // Input validation
        if (x < 0 || y < 0 || target < 0) return false;

        // If the total capacity is less than the target, it's impossible
        if (x + y < target) return false;

        // If any of the jugs or their sum is exactly the target
        if (x == target || y == target || x + y == target) return true;

        // Use Bézout's identity: target is measurable iff target is a multiple of GCD(x, y)
        return target % gcd(x, y) == 0;
    }

    // Private helper method to compute GCD using Euclidean algorithm
    private int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}
