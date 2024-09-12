'''
https://www.fastprep.io/problems/amazon-ordered-configuration
A barcode scanner can be configured by scanning a series of barcodes in the correct order. 
Barcode configurations are encoded into a single string and stored as a blob in the backend system. 
The client requests the configuration from the backend configuration service, 
and then needs to present the configurations in the correct order. 
The encoded configuration string is a series of <ordinal-index>/<configuration> pairs separated by '|'. 
The ordinal index value is a 4 digit numeric prefix within zeros. 
For example, the first configuration will be represented as 0001.

The goals are to 
1) validate the configuration string and 
2) provide the configuration client the configuration values in the order required to successfully 
configure the barcode scanner.

Validation conditions

All configurations must be separated by a '|' character.
Configurations cannot skip a number in the ordering; if there are three configuration strings, there must be a 1, 2, and 3 index.
Configuration values are alphanumeric and may contain no other characters.
Ordinal indices may not repeat; for example there cannot be two occurrences of the number "11".
Each configuration value is unique, configurations do not repeat.
The configuration ordinal index configurations cannot skip a value.
If a configuration string is not valid, return ["Invalid configuration"].

Function Description

Complete the function orderedConfiguration in the editor.

orderedConfiguration has the following parameters:

str configuration: the encoded configuration string
Returns

str configuration[]: an array of configurations in the correct order
Example 1:

Input:  configuration = "0001LAJ5KBX9H8|0003UKURNK403F|0002MO6K1Z9WFA|0004OWRXZFMS2C"
Output: ["LAJ5KBX9H8", "MO6K1Z9WFA", "UKURNK403F", "OWRXZFMS2C"] 
Explanation:

The value "LAJ5KBX9H8" is prefixed with an order value of "0001", so it is listed first.

Even though "MO6K1Z9WFA" appears third in the string, it is prefixed with "0002" so it is rereturned second.

"UKURNK403F" appears second in the configuration string, but is prefixed with "0003" so is listed third.

Lastly, "OWRXZFMS2C" is prefixed with 0004 so is listed fourth.
      
Example 2:

Input:  configuration = "000533B8XLD2EZ|0001DJ2M2JBZZR|0002Y9YK0A7MYO|0004IKDJCAPG5Q|0003IBHMH59SBO"
Output: ["DJ2M2JBZZR", "Y9YK0A7MYO", "IBHMH59SBO", "IKDJCAPG5Q", "33B8XLD2EZ"] 
Explanation:

No explanation for now
      
Example 3:

Input:  configuration = "0002f7c22e7904|000176a3a4d214|000305d29f4a4b"
Output: ["76a3a4d214", "f7c22e7904", "05d29f4a4b"] 
Explanation:

Based on the 'order' value, the expected output is:

[
  "76a3a4d214", #0001
  "f7c22e7904", #0002
  "05d29f4a4b"  #0003
]
      
Example 4:

Input:  configuration = "0002f7c22e7904|000176a3a4d214|000205d29f4a4b"
Output: ["Invalid configuration"] 
Explanation:

configuration string constains two indices for "0002", so the expected output is ["Invalid configuration"].
      
Constraints:
1 ≤ orders ≤ 9999
1 ≤ orders(configuration) ≤ 9999
Order values may not be unique or complete
Configuration values are not always unique, the same configuration may appear in multiple configuration steps

'''
from typing import List

errorString = ["Invalid configuration"]
separator = "|"

def orderedConfiguration(configuration:str) -> List[str]:
    maxIndexSoFar = 0
    # map to store, k,v as index:config
    indexConfig = dict()

    # Grab configs from rawData in a while loop using 2 pointers
    s, e = 0, 0
    while e <= len(configuration):

        # found the end of a possible config data
        if e == len(configuration) or configuration[e] == separator:
            possibleConfig = configuration[s:e]
            
            if possibleConfig.isalnum():
                index = int(possibleConfig[:4])

                # check validity conditions
                if index in indexConfig or (e-s) != 14 or index < 1:
                    return errorString
                
                maxIndexSoFar = max(maxIndexSoFar, index)
                indexConfig[index] = possibleConfig[4:e]

                s = e+1 # shift s to the beginning of the next config
        e +=1

    ans = []
    for i in range(maxIndexSoFar +1):
        if i in indexConfig:
            ans.append(indexConfig[i])

    return ans

print(orderedConfiguration("0001LAJ5KBX9H8|0003UKURNK403F|0002MO6K1Z9WFA|0004OWRXZFMS2C"))
print(orderedConfiguration("000533B8XLD2EZ|0001DJ2M2JBZZR|0002Y9YK0A7MYO|0004IKDJCAPG5Q|0003IBHMH59SBO"))
print(orderedConfiguration("0002f7c22e7904|000176a3a4d214|000305d29f4a4b"))
print(orderedConfiguration("0002f7c22e7904|000176a3a4d214|000205d29f4a4b"))

#
#
# ### a solution from LeetCode discussion
# import re
# def ordered_configuration(configuration: str) -> list[str]:
#     validator = re.compile(r'(\d{4})(\w{10})')
#     split_configs = sorted(configuration.split("|"))
#     result = {}
#     last_val = None
#     for val in split_configs:
#         x = validator.fullmatch(val)
#         if x and len(x.groups()) == 2:
#             id, config = x.group(1), x.group(2)
#             if last_val == None:
#                 last_val = int(id)
#             elif id in result or last_val != int(id) - 1:
#                 return False
#             last_val = int(id)
#             result[id] = config
#         else:
#             print(f"Failed, {x}")
#             return False
#     return list(result.values())
#
# print(ordered_configuration("1002f7c22e7904|000176a3a4d212|000305d29f4a4b"))