class Solution {
                
    public int reversePairs(int[] nums) {
        if (nums == null || nums.length <= 1) return 0;
        int n = nums.length;
        int[] BIT = new int[n + 1];
        int[] copy = nums.clone();
        Arrays.sort(copy);
        
        int res = 0;
        
        for (int i = n - 1; i >= 0; i--) {
            //find the first position in the array, where copy[index] >= num / 2, then any rand before index will contribute to the result
            int num = nums[i];
            res += search(BIT, index(copy, 1.0 * num / 2));
            insert(BIT, index(copy, num));
        } 
        return res;
    }
    
    private int search(int[] BIT, int i) {
        int cnt = 0;
        while (i > 0) {
            cnt += BIT[i];
            i -= (i & -i);
        }
        return cnt;
    }
    
    private void insert(int[] BIT, int i){
        i = i + 1;
        while (i < BIT.length) {
            BIT[i]++;
            i += (i & -i);
        }
    }          
    
    //first position that has num >= val
    private int index(int[] arr, double val) {
        int lo = 0, hi = arr.length;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] >= val) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }             
}