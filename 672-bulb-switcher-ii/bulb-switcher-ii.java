import java.util.*;

class Solution {
    static final int M = 1083;

    static class Node {
        int m;
        Node next;

        Node(int m) {
            this.m = m;
            this.next = null;
        }
    }

    Node[] hashtable = new Node[M];

    void initialize() {
        Arrays.fill(hashtable, null);
    }

    int hash_func(int m) {
        return m * 97 % M;
    }

    boolean find(int m) {
        int hash = hash_func(m);
        Node temp = hashtable[hash];
        while (temp != null) {
            if (temp.m == m) {
                return true;
            }
            temp = temp.next;
        }
        return false;
    }

    void insert(int m) {
        int hash = hash_func(m);
        Node newNode = new Node(m);
        newNode.next = hashtable[hash];
        hashtable[hash] = newNode;
    }

    void clear() {
        Arrays.fill(hashtable, null); // Java garbage collector handles deallocation
    }

    int min(int a, int b) {
        return Math.min(a, b);
    }

    public int flipLights(int n, int presses) {
        int cnt = 0;
        initialize();

        for (int mask = 0; mask < 16; mask++) {
            int b1 = (mask >> 0) & 1;
            int b2 = (mask >> 1) & 1;
            int b3 = (mask >> 2) & 1;
            int b4 = (mask >> 3) & 1;

            int total = b1 + b2 + b3 + b4;

            if (total % 2 != presses % 2 || total > presses) {
                continue;
            }

            int state = 0;

            for (int i = 0; i < min(n, 3); i++) {
                int l = 1;
                if (b1 == 1) {
                    l ^= 1;
                }
                if (b2 == 1 && i % 2 == 1) {
                    l ^= 1;
                }
                if (b3 == 1 && i % 2 == 0) {
                    l ^= 1;
                }
                if (b4 == 1 && i % 3 == 0) {
                    l ^= 1;
                }

                state <<= 1;
                state += l;
            }

            if (!find(state)) {
                insert(state);
                cnt++;
            }
        }

        clear();
        return cnt;
    }
}
