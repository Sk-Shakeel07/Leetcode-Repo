class Solution {
    public int hammingDistance(int x, int y) {
        int count = 0;
        int max = x>y ? x : y;
        while(max != 0){
            max = max/2;
            count++;
        }
        int arr1[] = new int[count];
         int arr2[] = new int[count];
        for(int i= arr1.length-1; i>=0 ; i--){
            arr1[i] = x % 2;
            x = x/2;
        }
        for(int i= arr2.length-1; i>=0 ; i--){
            arr2[i] = y % 2;
            y = y/2;
        }
        count = 0;
        for(int i= 0; i<arr1.length; i++){
            if(arr1[i] != arr2[i]){
                count++;
            }
        }
        return count;
    }
}