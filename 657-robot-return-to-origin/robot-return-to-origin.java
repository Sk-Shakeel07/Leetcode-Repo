class Solution {
    public boolean judgeCircle(String moves) {
        int a=0,b=0;
        for(int i:moves.toCharArray()){
            switch(i){
            case 'L'-> a++;
            case 'R'-> a--;
            case 'U'-> b++;
            case 'D'-> b--;
        }
        }
        return (a==0 && b==0);
    }
}