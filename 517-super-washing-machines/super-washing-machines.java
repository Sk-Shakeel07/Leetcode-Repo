class Solution {
    public int findMinMoves(int[] machines) {
        int sum = 0;
        for (int i : machines)
            sum+=i;
        if (sum%machines.length!=0)return -1;
        int goal = sum/machines.length; // goal = average dresses per machine
        
        int res = 0, psum=0;
        for (int i = 0; i < machines.length; i++) {
		    // psum is the partial sum of dresses in machines [0, i]
            psum+=machines[i];
			
			// the machines on the left (indexes [0,i]) have too many dresses or need more dresses
            res = Math.max(res, Math.abs(psum - (i+1)*goal));
			
			// machine [i] has X too many dresses
            res = Math.max(res, machines[i] - goal);
        }
        return res;
    }
}