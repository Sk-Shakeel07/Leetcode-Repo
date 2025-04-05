import java.util.TreeSet;

class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int indexDiff, int valueDiff) {
        TreeSet<Long> set = new TreeSet<>();

        for (int i = 0; i < nums.length; i++) {
            // Get the smallest number >= nums[i] - valueDiff
            Long ceil = set.ceiling((long) nums[i] - valueDiff);
            
            // Check if that number is within valueDiff of nums[i]
            if (ceil != null && Math.abs(ceil - nums[i]) <= valueDiff) {
                return true;
            }

            set.add((long) nums[i]);

            // Maintain sliding window of size indexDiff
            if (i >= indexDiff) {
                set.remove((long) nums[i - indexDiff]);
            }
        }

        return false;
    }
}
