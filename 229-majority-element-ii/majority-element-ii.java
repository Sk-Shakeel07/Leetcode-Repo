import java.util.*;

class Solution {
    public List<Integer> majorityElement(int[] nums) {
        int n = nums.length;
        Integer candidate1 = null, candidate2 = null;
        int count1 = 0, count2 = 0;

        // Step 1: Find potential candidates
        for (int i = 0; i < n; i++) {
            int num = nums[i];

            if (candidate1 != null && num == candidate1) {
                count1++;
            } else if (candidate2 != null && num == candidate2) {
                count2++;
            } else if (count1 == 0) {
                candidate1 = num;
                count1 = 1;
            } else if (count2 == 0) {
                candidate2 = num;
                count2 = 1;
            } else {
                count1--;
                count2--;
            }
        }

        // Step 2: Verify the candidates
        count1 = 0;
        count2 = 0;
        for (int i = 0; i < n; i++) {
            if (candidate1 != null && nums[i] == candidate1) {
                count1++;
            } else if (candidate2 != null && nums[i] == candidate2) {
                count2++;
            }
        }

        // Step 3: Prepare the result
        List<Integer> result = new ArrayList<>();
        if (count1 > n / 3) result.add(candidate1);
        if (count2 > n / 3) result.add(candidate2);

        return result;
    }
}
