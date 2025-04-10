class Solution {
    public List<Integer> countSmaller(int[] nums) {
        int n = nums.length;
        List<Integer> result = new ArrayList<>();
        int[] counts = new int[n];
        int[][] enumNums = new int[n][2];

        for (int i = 0; i < n; i++) {
            enumNums[i][0] = nums[i];  // value
            enumNums[i][1] = i;        // original index
        }

        mergeSort(enumNums, 0, n, counts);

        for (int c : counts) {
            result.add(c);
        }
        return result;
    }

    private void mergeSort(int[][] enumNums, int left, int right, int[] counts) {
        if (right - left <= 1) return;

        int mid = (left + right) / 2;
        mergeSort(enumNums, left, mid, counts);
        mergeSort(enumNums, mid, right, counts);

        List<int[]> merged = new ArrayList<>();
        int i = left, j = mid, rightCount = 0;

        while (i < mid && j < right) {
            if (enumNums[i][0] <= enumNums[j][0]) {
                counts[enumNums[i][1]] += rightCount;
                merged.add(enumNums[i++]);
            } else {
                merged.add(enumNums[j++]);
                rightCount++;
            }
        }

        while (i < mid) {
            counts[enumNums[i][1]] += rightCount;
            merged.add(enumNums[i++]);
        }

        while (j < right) {
            merged.add(enumNums[j++]);
        }

        for (int k = left; k < right; k++) {
            enumNums[k] = merged.get(k - left);
        }
    }
}
