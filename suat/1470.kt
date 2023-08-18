fun main() {

    fun shuffle(nums: IntArray, n: Int): IntArray {
        var ans: IntArray = intArrayOf()
        for(i in 0 until n){
            ans += nums[i]
            ans += nums[i+n]
        }
        return ans
    }


    shuffle(intArrayOf(2,5,1,3,4,7), 3)
}
