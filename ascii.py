#coding utf-8

from PIL import Image

def get_char(r,g,b,alpha=256):
    if alpha == 0:
	return " "
    gray=(2126*r+7152*g+722*b)/10000
    ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
    return ascii_char[int((gray / alpha + 1.0) * len(ascii_char))]

def write_file (out_file_name,content):
    with open(out_file_name,"w") as f:
	f.write(content)

def main (file_name="zifuhua.jpg", width=100, height=80,
	out_file_name="out_file"):
    content=" "
    im=Image.open(file_name)
    im=im.resize((width,height),Image.NEAREST)
    for i in xrange(width):
	for j in xrange(height):
	    content = get_char(*im.getpixel((i,j)))
	content += '\n'
    print content
    write_file(out_file_name,content)

if __name__=='__main__':
   main(file_name="ascii_dora.png")


