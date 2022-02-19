import string as st
stlow=st.ascii_lowercase
zip_stlow=tuple(zip(stlow[0::2],stlow[1::2]))
with open("writehere.txt","w") as f:
    for i,j in zip_stlow:
        #print(i,j)
        f.write(i + j +"\n")
    f.close()