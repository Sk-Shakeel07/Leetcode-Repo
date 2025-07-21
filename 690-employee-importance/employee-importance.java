/*
// Definition for Employee.
class Employee {
    public int id;
    public int importance;
    public List<Integer> subordinates;
};
*/

class Solution {
    // Recursive DFS to calculate total importance
    private int dfs(int id, Map<Integer, Employee> empMap) {
        Employee emp = empMap.get(id);
        int imp = emp.importance; // own importance
        for (int subId : emp.subordinates) {
            imp += dfs(subId, empMap); // add importance of subordinates
        }
        return imp;
    }

    public int getImportance(List<Employee> employees, int id) {
        Map<Integer, Employee> empMap = new HashMap<>();
        for (Employee emp : employees) {
            empMap.put(emp.id, emp); // map id to employee
        }
        return dfs(id, empMap);
    }
}
