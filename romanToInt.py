# https://leetcode.com/problems/roman-to-integer/
def romanToInteger(romanString):
    romanString = romanString.upper()
    romanToIntMap = {'I': 1, 'V': 5, 'X': 10,
                     'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ans = romanToIntMap.get(romanString[-1:])
    for i in range(len(romanString)-2, -1, -1):
        if romanToIntMap.get(romanString[i]) >= romanToIntMap.get(romanString[i+1]):
            ans += romanToIntMap.get(romanString[i])
        else:
            ans -= romanToIntMap.get(romanString[i])
    print(ans)


# second method, easy
# convert the original roman to our roman.
# for eg. convert IV -> IIII, IX-> VIIII
# but only convert which have smaller roman letter at left side, eg, 4,9,40,90,400,900
def romanTonewRoman(romanString: str):
    romanIntMap = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    romanString = romanString.replace('IV', 'IIII').replace(
        'IX', 'VIIII').replace('XL', 'XXXX').replace('XC', 'LXXXX').replace('CD', 'CCCC').replace('CM', 'DCCCC')
    ans = 0
    for i in romanString:
        ans += romanIntMap.get(i)
    return ans


romanToInteger('XIIV')
romanTonewRoman('XIIV')
