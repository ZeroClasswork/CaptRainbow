checklist = list()

# create
def create(item):
    checklist.append(item)

# read
def read(index):
    return checklist[index]

#update
def update(index, item):
    checklist[index] = item

#destroy
def destroy(index):
    checklist.pop(index)

def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    #destroy(1)                 #error

    print(read(0))
    print(read(1))

test()