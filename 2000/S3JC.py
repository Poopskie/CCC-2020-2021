import numpy as np

main = np.array([]) # stores all the arrays
temp_link = np.array([])

n = int(input("")) # number of pages

def inside_link(t):
    surfing_links = ""
    while True:
        surfing_links = str(input(""))
        if surfing_links.find("<A HREF=") != -1:
            t.append(surfing_links[surfing_links.find("<A HREF=")+8:surfing_links.find(">")+1])
        elif surfing_links.find("<HTML/>"):
            break
    return temp_link
    


for x in range(n):
    link = str(input("")) # first website link
    temp_link.append(link)
    main.stack(inside_link(temp_link))
