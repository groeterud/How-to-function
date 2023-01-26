'''
Potential improvements:
make the function more generic by checking if there are lines left in the file after the last post 
and if so, add them to the list of posts.
Other things? 
--------------------------------------------------------------------------------------------------
'''
def addLines(lines, linesPerPost:int) -> list:
    posts = []
    post = []
    postCount = 0
    for line in lines:
        post.append(line.rstrip('\n'))
        postCount += 1
        if postCount == linesPerPost:
            posts.append(post)
            post = []
            postCount = 0
    return posts


def readLineSeperatedFile_proper(filename:str, linesperPost:int) -> list:
    try:
        with open(filename, 'r') as f:
            posts = addLines(f, linesperPost)
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
        postCount = 0
        for line in f:
            post.append(line.rstrip('\n'))
            postCount += 1
            if postCount == linesperPost:
                posts.append(post)
                post = []
                postCount = 0
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
        postCount = 0
        for line in f:
            post.append(line.rstrip('\n'))
            postCount += 1
            if postCount == 4:
                posts.append(post)
                post = []
                postCount = 0
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
        postCount = 0
        for line in f:
            post.append(line.rstrip('\n'))
            postCount += 1
            if postCount == 4:
                posts.append(post)
                post = []
                postCount = 0

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
        postCount = 0
        for line in f:
            post.append(line.rstrip('\n'))
            postCount += 1
            if postCount == 4:
                posts.append(post)
                post = []
                postCount = 0

print(posts)