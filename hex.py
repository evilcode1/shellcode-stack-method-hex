import sys

print(" _____________________________________________")
print("|            C0d3d By : [ Evilcode1 ]         |") 
print("|                                             |")
print("|      5tr!n9 t0 r3v3r53[H3X] C0nv3rt3r       |")      
print("|                                             |") 
print("|             |evilcode1@mail.ru|             |")
print("|_____________________________________________|")

arg1 = sys.argv[1]
if len(arg1) % 2 == 0 and len(arg1) == 4 or len(arg1) == 8 or len(arg1) == 16 or len(arg1) == 24 or len(arg1) == 32:
    rev_string = arg1[::-1]

    print("[+] Orginal String : " + arg1 + "\n")
    print("[+] Reverse String : " + rev_string + "\n")
    print("[+] String Length  : " + str(len(arg1)) + "\n")
    print("[+] String in H3X  : " + arg1.encode("hex") + "\n")
    dev = arg1[::-1].encode("hex")
    print("[+] Reverse H3X    : " + dev + "\n") 
    #print(" _____________________________\n")
    print("[+] For shellcode  : \n")

    for i in range(0,len(dev),8):
        print ("==> push 0x" +dev[i:i+8] + "  || " + dev[i:i+8].decode("hex"))

    print("\n")
    print("[+] Done")
else:
    
    print("\n[-] String length is : " + str(len(arg1)) + " try to use 8 or 16 or 24 or 32 ...... etc ")
    