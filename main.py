#!/usr/bin/env python3
"""
ASCII Table - ASCII character table viewer
"""
for i in range(128):
    char = chr(i)
    if i < 32:
        name = {
            0: "NUL", 7: "BEL", 8: "BS", 9: "TAB", 10: "LF",
            13: "CR", 27: "ESC", 127: "DEL"
        }.get(i, f"Ctrl-{chr(i+64)}")
    elif i == 32:
        name = "SPACE"
    elif 33 <= i <= 47:
        names = "!\"#$%&'()*+,-./"
        name = f"SYM-{names[i-33]}"
    elif 48 <= i <= 57:
        name = f"DIGIT-{i-48}"
    elif 58 <= i <= 64:
        names = ":;<=>?@"
        name = f"SYM-{names[i-58]}"
    elif 65 <= i <= 90:
        name = f"LET-{chr(i)}"
    elif 91 <= i <= 96:
        names = "[\\]^_`"
        name = f"SYM-{names[i-91]}"
    elif 97 <= i <= 122:
        name = f"let-{chr(i)}"
    else:
        name = f"SYM-{chr(i)}"
    
    print(f"{i:3d} {i:02X}h {i:03o} {char!r:3} {name}")
