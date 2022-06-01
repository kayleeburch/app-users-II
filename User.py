from unicodedata import name
import uuid

class User:
    
    stored_posts = {}
    
    def __init__(self, name):
        self.name = name
        self.all_posts = []
    
        
    def add_post(self, post):
        random_num = uuid.uuid1()
        self.all_posts.append(post)
        User.stored_posts[int(random_num)] = post
        
    def delete_post(self, post):
        pass
                     
        
def main():
    emily = User('Emily')
    emily.add_post('hello, my name is emily!')
    emily.add_post('I am 23 years old')
    emily.add_post('I enjoy long walks on the beach')
    jack = User('Jack')
    jack.add_post('Hey guys, im jack')
    jack.add_post('this is another unique post')
    print(emily.all_posts)
    print(jack.all_posts)
    for key, value in emily.stored_posts.items():
        print(key,' : ', value)
    
if __name__ == '__main__':
    main()