#283.B  
with open(inname) as infile:
    with open(outname, "w") as outfile:
        for l infile:
            if "WARNING" in l:
                outfile.write(l.replace("\tWARNING", ""))
