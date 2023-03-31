# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from scapy.all import *
packets = rdpcap('C:/Users/dell/Desktop/capture.pcapng')
print(packets[26].load[-6])
newmap = {
2: "PostFail",
4: "a",
5: "b",
6: "c",
7: "d",
8: "e",
9: "f",
10: "g",
11: "h",
12: "i",
13: "j",
14: "k",
15: "l",
16: "m",
17: "n",
18: "o",
19: "p",
20: "q",
21: "r",
22: "s",
23: "t",
24: "u",
25: "v",
26: "w",
27: "x",
28: "y",
29: "z",
30: "1",
31: "2",
32: "3",
33: "4",
34: "5",
35: "6",
36: "7",
37: "8",
38: "9",
39: "0",
40: "Enter",
41: "esc",
42: "del",
43: "tab",
44: " ",
45: "_",
47: "{",
48: "}",
56: "/",
57: "CapsLock",
79: "RightArrow",
80: "LetfArrow"
}

ans = []
for i in range(26, len(packets), 2):
    try:
        shit = newmap[packets[i].load[-6]]
        if shit == 'del' and ans != []:
            ans.pop()
        else:
            ans.append(shit)
    except:
        pass
print(''.join(ans))

# usb keyboard character mapping in wireshark
# https://ctftime.org/writeup/17233
# accessdenied{p4ck3t_c4ptur3_f0r_usb}