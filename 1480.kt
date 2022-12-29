fun main() {

    fun runningSum(nums: IntArray): IntArray {
        var sum:Int = 0
        val result = arrayListOf<Int>()

        for(number in nums){
            sum += number
            result.add(sum)
        }
        return result.toIntArray()
    }


    runningSum(intArrayOf(1, 2, 3, 4))
}
