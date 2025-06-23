'''
https://www.fastprep.io/problems/amazon-get-min-subsegments
Amazon Prime Video is developing a new feature called "Segmentify." This feature applies to a video with n (even) visual frames, where each frame is represented by a binary character in the array frames. In this format, a "0" represents a black pixel, and a "1" represents a white pixel.

Due to factors like lighting and camera angles, some frames may need horizontal or vertical flips (changing "0"s to "1"s and vice versa) to create consistent visuals. The objective is to divide the video into subsegments so that all frames in a subsegment are visually identical (i.e., the frames in a subsegment are either all "0"s or all "1"s). Additionally, each subsegment should have an even length.

The goal is to accomplish this segmentation with two criteria in mind:

Minimize the number of flips required to form valid segments, let this be denoted by B.
Among all configurations requiring B flips, minimize the total number of subsegments.
Given the binary string frames, determine the minimum number of even-length subsegments that can be created while utilising the least number of flips.

Note: A subsegment is a segment that can be derived from another segment by deleting some elements without changing the order of the remaining elements.

Function Description

Complete the function getminSubsegments in the editor.

getminSubsegments has the following parameter:

string frames: the frames of the video
Returns

int: the minimum number of subsegments.

Constraints

2 ≤ n ≤ 10^5, n is of even length
It is guaranteed that string frames only consist of 0s and 1s.
Example 1:

Input: frames = "1110011000"
Output: 2
Explanation:



So, the length of all subsegments - (11111111 and 00)is even.

So again, the minimum number of subsegments that frames can be divided into to make it "Segmentify-compliant" is 2 with minimum flips of 3.

Hence answer is 2.
      
Example 2:

Input: frames = "110011"
Output: 3
Explanation:

      
Another example, frames = "110011", In this example, the string already consists of groups of "0"s and "1"s that have even lengths. Therefore, no flipping is necessary, and the string can be divided into 3 even-length subsegments without modification. Hence, the answer is 3. Recall that we need to minimize flips first and give that priority before minimizing segments.
      
      
Example 3:

Input: frames = "100110"
Output: 1
Explanation:


Flip the first 0 to 1. So, frames = "110110".
 
~~ Again flip the first 0 to 1. So, frames = "111110".
    
~~ At last, again flip the first 0 to 1. So, frames = "111111".
     
Hence, the length of the only segment formed is even. So, the minimum number of subsegments that s can be divided to make it fine is 1 with minimum flips of 3. Hence, the answer is 1.'''

# def getminSubsegments(frames: str) -> int:
#     N = len(frames)
#     last_pair_type = -1
#     segments = 0
#     for i in range(0, N, 2):
#         current_pair = frames[i:i+2]
#         if current_pair == "00" and last_pair_type != 0:
#             segments += 1
#             last_pair_type = 0
#         elif current_pair == "11" and last_pair_type != 1:
#             segments += 1
#             last_pair_type = 1
#         else: # current_pair is "01" or "10"
#             if last_pair_type == 0 or last_pair_type == 1:
#                 # flip to 00,  or flip to 11, expand the last segment, do not create a new segment
#                 pass
#             else:
#                 # This should be the first pair, What to flip, try to snap to the 3rd element
#                 if i + 2 < N and frames[i+2] == '0':
#                     segments += 1
#                     last_pair_type = 0
#                 else:
#                     segments += 1
#                     last_pair_type = 1
               
#     return segments

def getminSubsegments(frames: str) -> int:
    """
    Verilen 'frames' dizisini minimum çevirme ile geçerli, çift uzunluklu 
    alt segmentlere ayırmak için gereken minimum segment sayısını hesaplar.
    """
    n = len(frames)
    
    # Boş olmayan bir dizede her zaman en az bir segment olacaktır.
    segments = 1
    
    # Mevcut segmentin tipini ('0' veya '1') saklar.
    # Bu tip, sadece "sabit" bir çiftle ('00' veya '11') karşılaşıldığında belirlenir.
    segment_type = None
    
    # Dizeyi ikişerli çiftler halinde tara
    for i in range(0, n, 2):
        c1 = frames[i]
        c2 = frames[i+1]
        
        # Eğer çift "sabit" ise ('00' veya '11')
        if c1 == c2:
            current_pair_type = c1
            
            # Eğer henüz bir segment tipi belirlenmediyse, bu ilk sabit çift
            # segmentin tipini belirler.
            if segment_type is None:
                segment_type = current_pair_type
            
            # Eğer bu sabit çiftin tipi, mevcut segmentin tipinden farklıysa,
            # yeni bir segment başlatmak zorundayız.
            elif segment_type != current_pair_type:
                segments += 1
                segment_type = current_pair_type
        
        # Eğer çift "esnek" ise ('01' veya '10'), hiçbir şey yapmayız.
        # Çünkü bu çift, minimum çevirme hakkı kullanılarak her zaman
        # mevcut `segment_type`'ına uydurulabilir. Bu nedenle yeni bir
        # segment başlatmaya zorlamazlar.

    return segments


## TEST CASES, assertions
if __name__ == "__main__":
    assert getminSubsegments("1110011000") == 2
    assert getminSubsegments("110011") == 3
    assert getminSubsegments("100110") == 1
    assert getminSubsegments("00001111") == 2
    assert getminSubsegments("11110000") == 2
    assert getminSubsegments("10101010") == 1
    assert getminSubsegments("11000011") == 3
    assert getminSubsegments("011111") == 1
    print("\n 😎 All test cases passed!\n")  # If no assertion error, this will print