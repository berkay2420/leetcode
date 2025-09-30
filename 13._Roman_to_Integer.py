
def romanToInt(s: str) -> int:
    symbol_dict = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
    }

    total=0
    i=0
    #roman numerals written from largest to smallest (left to right)
    while i < len(s) :
        if i < len(s) - 1 and symbol_dict[s[i]] < symbol_dict[s[i+1]]:
            total += symbol_dict[s[i+1]] - symbol_dict[s[i]] 
            i+=2
            # 2 because we are working with current char and next char
        else:
            total+=symbol_dict[s[i]]
            i+=1
        
    return total

roman_string="MCMXCIV"
print(f"{roman_string} to integer is {romanToInt(roman_string)}")
        