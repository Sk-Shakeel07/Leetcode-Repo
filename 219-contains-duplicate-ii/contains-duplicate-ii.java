class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        HashMap<Integer, Integer> m = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            // If we've seen this number before
            if (m.containsKey(nums[i])) {
                // Check if the index difference is within k
                if (i - m.get(nums[i]) <= k) return true;
            }
            // Update the index of the current number
            m.put(nums[i], i);
        }
        
        return false;
    }
}
