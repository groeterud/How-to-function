'''
Potential improvements:
make the function more generic by checking if there are lines left in the file after the last post 
and if so, add them to the list of posts.
Other things? 
--------------------------------------------------------------------------------------------------
'''



def readLineSeperatedFile_proper(filename:str, linesperPost:int) -> list:
    try:
        with open(filename, 'r') as f:
            posts = []
            post = []
            for line in f:
                post.append(line.rstrip('\n'))
                if len(post) == linesperPost:
                    posts.append(post)
                    post = []
            return posts
    except FileNotFoundError:
        print("File not found")
        return []

print(readLineSeperatedFile_proper("anotherfile.txt", 120))

'''
--------------------------------------------------------------------------------------------------
'''

def readLineSeperatedFile(filename:str, linesperPost:int) -> list:
    with open(filename, 'r') as f:
        posts = []
        post = []
        for line in f:
            post.append(line.rstrip('\n'))
            if len(post) == linesperPost:
                posts.append(post)
                post = []
        return posts

posts = readLineSeperatedFile("anotherfile.txt", 8)
print(posts)



'''
--------------------------------------------------------------------------------------------------
'''

def readLineSeperatedFile_1(filename:str) -> list: 
    with open(filename, 'r') as f:
        posts = []
        post = []
        for line in f:
            for i in range(0,4):
                post.append(line.rstrip('\n'))
                if len(post) == 4:
                    posts.append(post)
                    post = []
        return posts

posts = readLineSeperatedFile_1("somefile.txt")
print(posts)

'''
--------------------------------------------------------------------------------------------------
'''

posts = []

def readLineSeperatedFile_2(filename:str) -> list: 
    with open(filename, 'r') as f:
        posts = []
        post = []
        for line in f:
            for i in range(0,4):
                post.append(line.rstrip('\n'))
                if len(post) == 4:
                    posts.append(post)
                    post = []

readLineSeperatedFile_2("somefile.txt")
print(posts)

'''
--------------------------------------------------------------------------------------------------
'''

posts = []

def readLineSeperatedFile_3() -> list:
    with open("somefile.txt", 'r') as f:
        posts = []
        post = []
        for line in f:
            for i in range(0,4):
                post.append(line.rstrip('\n'))
                if len(post) == 4:
                    posts.append(post)
                    post = []

print(posts)