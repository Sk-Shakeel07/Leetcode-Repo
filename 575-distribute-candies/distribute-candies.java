class Solution {
    public int distributeCandies(int[] candyType) {
        int max = candyType.length / 2;
        boolean[] typeCheck = new boolean[200001];
        int res = 0;

        for (int i = 0; i < candyType.length; i++) {
            int type = candyType[i] + 100000;
            if (!typeCheck[type]) {
                res++;
                if (res == max) {
                    return max;
                }
                typeCheck[type] = true;
            }
        }

        return res;
    }
}
