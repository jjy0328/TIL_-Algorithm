class Solution {
    fun solution(numbers: IntArray): Double {
        var answer: Double = 0.0
        var length = numbers.size
        
        for (num in numbers){
            answer += num
        }
        return answer.toDouble() / length.toDouble()
    }
}