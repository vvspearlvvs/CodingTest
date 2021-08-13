import re

def solution(files):

    def key_function(fn):
        head,number,tail = re.match(r'([a-z-. ]+)(\d{,5})(.*)',fn).groups()
        return [head,int(number)]

    return sorted(files, key = lambda x: key_function(x.lower()))

def test(files):
    head,number,tail = re.match(r'([a-z-. ]+)(\d{,5})(.*)',files)
    print(head,number,tail)

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(test(files))
