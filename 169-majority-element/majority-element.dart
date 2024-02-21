class Solution {
  int majorityElement(List<int> nums) {
      int k = 0, s =0;
      for(int n in nums){
          if(s == 0){
              s++;
              k = n;
          }
          else{
              if(k == n){
                  s++;
              }else{
                  s--;
              }

          }
      }

    return k;




    // kazanan= 2
    // sayac= 3


    // [,,,2,2,2]  == > 11 eleman 6 adet 2  
    //                      |

/// sayac 0 ise , sayac ++ , kazanan = current
/// else kaann = cur, sayaca ++
/// cur != kazanan, sayaca --

    //   var map = {};
    //   int res = 0;

    //   for(int n in nums){
    //       map[n] = 1 + (map[n] ?? 0);

    //         if(map[n] > nums.length/2){
    //             res = n;
    //             break;
    //         }

    //   }
    
    // return res;
  }
}