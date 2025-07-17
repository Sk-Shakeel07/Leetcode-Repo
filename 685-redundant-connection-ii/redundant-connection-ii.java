class Solution {
    public int[] findRedundantDirectedConnection(int[][] edges) {
    	parent = new int[edges.length+1];
 		List<Integer> parents [] = new List[edges.length+1];
 		for(int i = 0;i<parents.length;i++) parents[i] = new ArrayList<>();

 		for(int [] edge:edges) {
 			parents[edge[1]].add(edge[0]);
            if(parents[edge[1]].size() == 2) {
                for(int j = 1;j>=0;j--) {
                    int [] redundant = {parents[edge[1]].get(j), edge[1]};
                    if(isValidWithoutEdge(redundant, edges)) {
                        return redundant;
                    }
                } 
            }
 		}     

        return findAnyInvalidEdge(edges);
    }

    int parent [] ;

    int [] findAnyInvalidEdge(int [][] edges) {


 		for(int i = 0;i<parent.length;i++) parent[i] = i;

 		for(int [] edge:edges) {
 			int p1 = getParent(parent, edge[0]);
 			int p2 = getParent(parent, edge[1]);

 			if(p1 == p2 ||p2 != edge[1]) return edge;

 			parent[p2] = p1;
 		} 

 		return edges[edges.length-1];
    }

    boolean isValidWithoutEdge(int [] redundant, int [][] edges) {
    	//int parent [] = new int[edges.length+1];
    	for(int i = 0;i<parent.length;i++) parent[i] = i;

    	for(int edge[]:edges) {
    		if(edge[0] == redundant[0] && edge[1] == redundant[1]) continue;
    		int p1 = getParent(parent, edge[0]);
    		int p2 = getParent(parent, edge[1]);

    		parent[p2] = p1;
    	}

    	for(int i = 2;i<parent.length;i++) {
    		if(getParent(parent, i) != getParent(parent, i-1)) return false;
    	}
    	return true;
    }

    int getParent(int [] parent, int v) {
    	int p = parent[v];
    	while(p != parent[p]) {
    		p = parent[p];
    	}
    	return p;
    }
}