import hashlib
import sys

def md5(password):           #  普通md5
    password = password.encode(encoding="gb2312")
    m = hashlib.md5(password)
    m = m.hexdigest()
    print(m)


def salt_md5(password,salt):             #加盐md5
    password = password.encode(encoding="gb2312")
    salt = salt.encode(encoding="gb2312")
    m = password+salt
    m = hashlib.md5(m)
    m = m.hexdigest()
    print(m)

def sha1(password):
    password = password.encode(encoding="gb2312")
    m = hashlib.sha1(password)
    m = m.hexdigest()
    print(m)

def salt_sha1(password,salt):
    password = password.encode(encoding="gb2312")
    salt = salt.encode(encoding="gb2312")
    m = password+salt
    m = hashlib.sha1(m)
    m = m.hexdigest()
    print(m)


def main():
    chose = input('1 md5加密 \n2 sha1加密 \n')
    chose = int(chose)
    if chose == 1:
        password = input('输入加密的md5 \n')
        salt = input('输入要加密的盐值 \n')
        if salt == '':
            value = md5(password=password)
        else:
            value = salt_md5(password=password,salt=salt)
    elif chose == 2:
        password = input('输入加密的sha1 \n')
        salt = input('输入要加密的盐值 \n')
        if salt == '':
            value = sha1(password=password)
        else:
            value = salt_sha1(password=password,salt=salt)


if __name__ == '__main__':
    q = 1
    while q != 'q':
        main()
        q = input('输入 q 退出 任意字符继续')
