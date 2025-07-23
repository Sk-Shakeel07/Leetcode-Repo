import java.util.*;

class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        // Step 1: Count frequencies
        Map<String, Integer> freq = new HashMap<>();
        for (String word : words) {
            freq.put(word, freq.getOrDefault(word, 0) + 1);
        }

        // Step 2: Create a priority queue with custom comparator
        PriorityQueue<Map.Entry<String, Integer>> pq = new PriorityQueue<>(
            (a, b) -> {
                if (!a.getValue().equals(b.getValue())) {
                    return b.getValue() - a.getValue(); // Higher freq first
                } else {
                    return a.getKey().compareTo(b.getKey()); // Lexicographically smaller first
                }
            }
        );

        // Step 3: Add all entries to the priority queue
        pq.addAll(freq.entrySet());

        // Step 4: Extract top k elements
        List<String> result = new ArrayList<>();
        while (k-- > 0 && !pq.isEmpty()) {
            result.add(pq.poll().getKey());
        }

        return result;
    }
}
