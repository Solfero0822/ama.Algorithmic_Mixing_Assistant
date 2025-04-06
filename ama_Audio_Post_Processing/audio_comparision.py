
def compare_lufs(
        lufs1: float,
        lufs2: float
    ):

    if lufs1 > lufs2:
        diff = lufs1 - lufs2
        print(diff)
        if 6.0 < diff < 12.0:
            result = "Audio 1 is significantly louder than Audio 2, consider normalizing or"
        elif 3.0 < diff < 6.0: 
            result = "Audio 1 is slightly louder than Audio 2"
        elif 1.0 < diff < 3.0: 
            result = "Audio 1 is ever so slightly louder than Audio 2"
        elif 0.0 < diff < 1.0: 
            result = "Both audio are almost at the same level"
        else:
            result = "Audio 1 is louder than Audio 2"
        print(f"Comparison of LUFS: {result}")
    elif lufs1 < lufs2:
        diff = lufs2 - lufs1
        print(diff)
        if 6.0 < diff < 12.0:
            result = "Audio 2 is significantly louder than Audio 1"
        elif 3.0 < diff < 6.0: 
            result = "Audio 2 is slightly louder than Audio 1"
        elif 1.0 < diff < 3.0: 
            result = "Audio 2 is slightly louder than Audio 1"
        elif 0.0 < diff < 1.0: 
            result = "Both audio are almost at the same level"
        else:
            result = "Audio 2 is louder than Audio 1"
        print(f"Comparison of LUFS: {result}")
    else:
        print("Both audio tracks have a very similar loudness level")

# compare_lufs(-12.46, -12.66)



def compare_dynRange(
        dynRange1: float,
        dynRange2: float
    ):

    if dynRange1 > dynRange2:
        diff = dynRange1 - dynRange2
        print(diff)
        if 6.0 < diff < 12.0:
            result = "Audio 1 is significantly dynamic than Audio 2, consider normalizing"
        elif 3.0 < diff < 6.0: 
            result = "Audio 1 is slightly dynamic than Audio 2"
        elif 1.0 < diff < 3.0: 
            result = "Audio 1 is ever so slightly dynamic than Audio 2"
        elif 0.0 < diff < 1.0: 
            result = "Both audio have very similar dynamic range"
        else:
            result = "Audio 1 has similar dynamic than Audio 2"
        print(f"Comparison of Dynamic Range: {result}")
    elif dynRange1 < dynRange2:
        diff = dynRange2 - dynRange1
        print(diff)
        if 6.0 < diff < 12.0:
            result = "Audio 2 is significantly dynamic than Audio 1"
        elif 3.0 < diff < 6.0: 
            result = "Audio 2 is slightly dynamic than Audio 1"
        elif 1.0 < diff < 3.0: 
            result = "Audio 2 is ever so slightly dynamic than Audio 1"
        elif 0.0 < diff < 1.0: 
            result = "Both audio have very similar dynamic range"
        else:
            result = "Audio 1 has similar dynamic than Audio 2"
        print(f"Comparison of Dynamic Range: {result}")
    else:
        print("Both audio tracks have identical dynamic range")

# compare_dynRange(14.16, 11.52)

def compare_panning(
        panning1: float,
        panning2: float
    ):

    if panning1 > panning2:
        diff = panning1 - panning2
        print(diff)
        if -0.1 < diff < 0.1:
            result = "Audio 1 is significantly dynamic than Audio 2, consider normalizing"
        elif -0.3 < diff < -0.1 or 0.1 < diff < 0.3: 
            result = "Audio 1 is slightly dynamic than Audio 2"
        elif -0.3 < diff < -0.1 or 0.1 < diff < 0.3: 
            result = "Audio 1 is ever so slightly dynamic than Audio 2"
        elif 0.0 < diff < 1.0: 
            result = "Both audio have very similar dynamic range"
        else:
            result = "Audio 1 has similar panning to Audio 2"
        print(f"Comparison of Panning: {result}")
    elif panning1 < panning2:
        diff = panning2 - panning1
        print(diff)
        if 6.0 < diff < 12.0:
            result = "Audio 2 is significantly dynamic than Audio 1"
        elif 3.0 < diff < 6.0: 
            result = "Audio 2 is slightly dynamic than Audio 1"
        elif 1.0 < diff < 3.0: 
            result = "Audio 2 is ever so slightly dynamic than Audio 1"
        elif 0.0 < diff < 1.0: 
            result = "Both audio have very similar dynamic range"
        else:
            result = "Audio 1 has similar panning to Audio 2"
        print(f"Comparison of Panning: {result}")
    else:
        print("Both audio tracks have identical dynamic range")

# compare_panning(0.5, 0.3)