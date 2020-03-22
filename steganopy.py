import stepic
from PIL import Image
from os.path import basename 
def encode(file):
    # This Function Will Put data on picture
    img = Image.open(file)
    text = input("Text : ")
    img_stegano = stepic.encode(img,text.encode())
    name = input("Output Name : ")
    img_stegano.save(name)
def decode(file):
    # This Function Will get data from picture
    img = Image.open(file)
    decoded = stepic.decode(img)
    return decoded
file  = input("Image File : ")

print("1 - Encode")
print("2 - Decode")
mode = input(">> ")
if mode == "1":
    encode(file)
elif mode == "2":
    text = decode(file)
    print("Decoded Text : ")
    print("\t"+text)
else:
    print("Command Not Found !")
    
