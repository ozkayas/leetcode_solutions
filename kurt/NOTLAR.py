* String i şu şekilde terse çeviriyoruz

	original_string = "Hello, World!"
    reversed_string = original_string[::-1]
	
	-1 yerine -2 ya da 2 vs kullanınca her 2 karakterde birini basıyor, "Hlo Wrd" gibi

CHATGPT:
s = "abcdefgh"

# Slicing with start, end, and step values
sliced1 = s[1:6:2]  # Output: "bdf"
sliced2 = s[::3]    # Output: "adg"
sliced3 = s[:4]     # Output: "abcd"
sliced4 = s[2:]     # Output: "cdefgh"    


* Kalan işlemi şu şekilde
  remainder = 123 % 10 # sonuç 3

* Aşağıya yuvarlama:
  round_down = 17 // 5 # sonuç 3

* for i in range(5) # 0 1 2 3 4
  for i in range (5,-1,-1) # 5 4 3 2 1 0

* s = 'deneme'
    print(s[1:3]) # en  

*   import re
    s = re.sub(r'[^a-z0-9]', '', s)  #  The expression [^a-z0-9] matches any character that is not a lowercase letter or a digit.  
    # The r before the pattern string indicates a "raw string," which is used to treat the backslashes (\) as literal characters rather than escape characters.
    print(re.sub(r'[.]', '[.]', "111.000.255")) # "111[.]000[.]255" döndürüyor, soru zaten bunu istiyordu.
    
* ord(character) - 64# 'A' için 1, B için 2 verir ama küçük harf için 64 olmaz. Daha güzeli
  ord(character) - ord('A') + 1 # istersen ord('a') yaparsın. 
  chr(ord('a')) # bu ekrana 'a' basar, loop içinde chr(ord('a') + i) diye dönerek, tüm alfabeyi bir listeye aldırabilirsin ya da dictionary key yapabilirsin.

* s = "deneme"
  s.index("e") # 1 basar çünkü ilk e harfi 1. indexde
  s.index("e",2) # 3 basar çünkü 2. indexten sonraki ilk e harfi 3. index te
  for idx in s:
    print(s.index(idx)) #0 1 2 1 4 3 basıyor.
  # 205. Isomorphic Strings sorusunda kullanılıyor. Kelime içinde her harfe unique sayı atamayı sağlıyor. e harfi 10 kere de bulunsa, ilk e harfinin değerini hashmap(dictionary) e atıyorsun.
  
* my_dict = {"a": 1, "b": 2, "c": 3}

    if "d" not in my_dict:
        print("'d' is not a key in the dictionary.")
    else:
        print("'d' is a key in the dictionary.")

* # Return etmen gereken şey string ise ve bu stringi loop içinde karakter by karakter dolduruyorsan şunu yaparsın
str = []
str.append('a')
str.append(source[i])

return ''.join(str)

* #1678. Goal Parser Interpretation sorusunu tek satırda şöyle çözmüşler:
return command.replace('()','o').replace('(al)','al')

*   str = "deneme"
    str[0] = 'f'
    print(str[0])
    # this gives error because Strings in Python are immutable, meaning you cannot modify individual characters in-place.
    modified_str = list(str) # bunu yaptıktan sonra artık modified_str[0] = 'm' vs yapabilirsin.
    #En sonda string return edeceksen de şöyle oluyor:
    return ''.join(modified_str)

* # List comprehension diye bir olay var, şu syntax ile çalışıyor:

numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers]
# Result: [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5]
even_numbers = [x for x in numbers if x % 2 == 0]
# Result: [2, 4]

text = "Hello, World!"
uppercase_letters = [char for char in text if char.isupper()]
# Result: ['H', 'W']

numbers = [1, 2, 3, 4, 5]
result = ["even" if num % 2 == 0 else "odd" for num in numbers]
# Result: ['odd', 'even', 'odd', 'even', 'odd']

names = ["Alice", "Bob", "Charlie"]
name_lengths = {name: len(name) for name in names}
# Result: {'Alice': 5, 'Bob': 3, 'Charlie': 7}  

# List i alıyor, dictionary yapıyor ya da hashset  

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for sublist in nested_list for num in sublist]
# Result: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Sanki içiçe 2 loop  yapıyor ve değerini bir liste olarak yazdırıyor.
# Burda kilit olan "for i in some_list" kısmı, sonrası akla gelir


* ret.append(char_map.get(chr, chr)) 
# Burda şunu yapıyo, char_map dictionary de eğer aradığı key i bulamazsa, aradığı değeri aynen append ediyor. nvl() gibi sql deki

* # dict, chr gibi built-in isimleri kullanma 

* if rev[i] in '123456789':  # Karakter bir sayı mı bu şekilde bakılabilir.



        
        
        
        
        
        