import hashlib

class URL():
    def __init__(self,url):
        self.url = url

    def hash_url(self):
        salt = hashlib.sha256(self.url.encode()).hexdigest()
        res = hashlib.sha256(self.url.encode()).hexdigest()
        res = salt + res
        return res

    def write_in_DB(self):
        if not self.exist_q():
            with open('url_DB.txt', 'a') as file:
                file.write(f'{self.hash_url()}\n')
        else:
            print("url is already in DB")

    def exist_q(self):
        index = 0
        with open('url_DB.txt','r') as file:
            for line in file:
                if self.hash_url() + '\n' == line:
                    index += 1
                    return True
                else:
                    pass
        if index == 0:
            return False

a = URL("gb.com")
a.write_in_DB()
print(a.exist_q())