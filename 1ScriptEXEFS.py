import numpy
import sys

with open("exefs_texts.txt", 'r', encoding="UTF-8") as f:
    Offsets = [line.split("\t", -1)[0] for line in f]
    f.seek(0,0)
    Texts = [line.split("\t", -1)[1] for line in f]
    f.seek(0,0)
    TextsCheck = [line.strip("\r\n").strip("\n").split("\t", -1)[2] for line in f]

print("Validating texts...")

for i in range(0, len(Offsets)):
    if (len(bytes(Texts[i].encode("UTF-8"))) > len(bytes(TextsCheck[i].encode("UTF-8")))):
        print("Incorrect size. Line: %d, Max allowed: %d B, detected: %d B" % (i+1, len(bytes(TextsCheck[i].encode("UTF-8"))), len(bytes(Texts[i].encode("UTF-8")))))
        input("Press Enter to continue...")
        sys.exit()

pointer1_start = 0x1BE230
pointer1_diff = 0x20
pointer2_start = 0xFBB10
pointer2_diff = 0x18
text_start = 0x138F14

with open("exefs_fragments.txt", 'r', encoding="UTF-8") as f:
    Texts2 = [line.split("\t", -1)[0] for line in f]
    f.seek(0,0)
    Texts2Check = [line.strip("\r\n").strip("\n").split("\t", -1)[1] for line in f]

print("Validating fragments...")

sizeENG = 0
sizeJAP = 0

for x in range(0, len(Texts)):
    sizeENG = sizeENG + len(Texts2[x].encode("UTF-8"))
    sizeJAP = sizeJAP + len(Texts2Check[x].encode("UTF-8"))
if (sizeENG > sizeJAP):
    print("Size check failed. Got: %d B, Expected: %d B" % (sizeENG, sizeJAP))
    input("Press Enter to continue...")
    sys.exit()

address = 0x139A22
shift = -3
Text = "Natsumi"

with open("exefs_natsumi.txt", 'r', encoding="UTF-8") as f:
    Offsets2 = [line.strip("\r\n").strip("\n").split("\t", -1)[0] for line in f]

print("Writing patch...")

with open("atmosphere/exefs_patches/HigurashiEN/215EEA8204AEEFCF09FD193A7EC7A070.ips", "wb") as f:
    f.write(b"IPS32")
    for i in range(0, len(Offsets)):
        f.write(numpy.uint32(int(Offsets[i], 16)+0x100).byteswap())
        f.write(numpy.uint16(len(Texts[i].encode("UTF-8"))+1).byteswap())
        f.write(bytes(Texts[i].encode("UTF-8")))
        f.write(numpy.uint8(0))
    for i in range(0, len(Texts2)):
        f.write(numpy.uint32(pointer1_start+0x100).byteswap())
        f.write(numpy.uint16(4).byteswap())
        f.write(numpy.uint32(text_start))
        f.write(numpy.uint32(pointer2_start+0x100).byteswap())
        f.write(numpy.uint16(4).byteswap())
        f.write(numpy.uint32(text_start))
        f.write(numpy.uint32(text_start+0x100).byteswap())
        f.write(numpy.uint16(len(Texts2[i].encode("UTF-8"))+1).byteswap())
        f.write(bytes(Texts2[i].encode("UTF-8")))
        f.write(numpy.uint8(0))
        text_start = text_start + len(Texts2[i].encode("UTF-8")) + 1
        pointer1_start = pointer1_start + pointer1_diff
        pointer2_start = pointer2_start + pointer2_diff
    for i in range(0, len(Offsets2)):
        f.write(numpy.uint32(int(Offsets2[i], 16)+0x100).byteswap())
        f.write(numpy.uint16(4).byteswap())
        f.write(numpy.uint32(address+shift))
    f.write(numpy.uint32(address+shift+0x100).byteswap())
    f.write(numpy.uint16(len(Text.encode("UTF-8"))+1).byteswap())
    f.write(bytes(Text.encode("UTF-8")))
    f.write(numpy.uint8(0))
    f.write(b"\x00\x05\x55\x24")
    f.write(b"\x00\x0c")
    f.write(b"\x04\x00\x00\x14\xE8\xA3\x00\x39\x11\x00\x00\x14")
    f.write(b"\x00\x05\x55\xD8")
    f.write(b"\x00\x10")
    f.write(b"\xE8\xA3\x40\x39\x68\x00\x08\x36\xA8\x0D\x80\x52\xD1\xFF\xFF\x17")
    f.write(b"EEOF")

print("Patch has been created.")
