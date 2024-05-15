import html

str = chr(32209) + "asdf"
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")
str_ascii = str.encode('ASCII','xmlcharrefreplace')
 
print(str)
 
print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)
print("ASCII 编码：", str_ascii)
 
 
print("UTF-8 解码：", str_utf8.decode('UTF-8','strict'))
print("GBK 解码：", str_gbk.decode('GBK','strict'))
# print("ASCII 解码：", str_ascii.decode('ASCII','strict'))

text = "<p>alert(1)</p>"
encoded_text = html.escape(text)

print(encoded_text)
s = ord("alert")
print(s)
#ſ