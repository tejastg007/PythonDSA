# https://leetcode.com/problems/defanging-an-ip-address/

# method 1- using prebuilt method
def defang(ip):
    return ip.replace('.', '[.]')

# method 2 - without prebuilt method


def defang2(ip):
    ans = ""
    for c in ip:
        if c == '.':
            ans += '[.]'
        else:
            ans += c
    return ans


print(defang('1.1.1.1'))
print(defang2('1.1.1.1'))
