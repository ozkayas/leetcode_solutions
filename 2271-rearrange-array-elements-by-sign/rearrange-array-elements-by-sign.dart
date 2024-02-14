class Solution {
  List<int> rearrangeArray(List<int> nums) {
        var pos = [];
        var negs = [];
        int w = 0;
        int r = 0;
        int p = 0;
        int n = 0;

        while (r < nums.length){
            (nums[r]>0)?
                pos.add(nums[r]):
                negs.add(nums[r]);            
            r++;
        }

        while (w < nums.length){
            if(w.isEven){ //cift sayi ise, pos listesinden yaz
                nums[w] = pos[p];
                p++;            
            }else{                
                nums[w] = negs[n];
                n++;
            }
            w++;
        }

    return nums;

}
}



