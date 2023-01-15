class Solution {
    fun solution(n: Int): Int {
        var answer: Int = 0
        
        for (num in 0 .. n step 2){
            answer += num
        }
        return answer
    }
}