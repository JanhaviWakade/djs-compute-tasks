if __name__ == '__main__':
    N = int(input())

n=[]

for i in range(N):
    command = input()
    word=command.split()
    
    if word[0]=="insert":
        n.insert(int(word[1]),int(word[2]))
    if word[0]=="print":   
        print(n)
    if word[0]=="remove": 
        n.remove(int(word[1]))
    if word[0]=="append":
        n.append(int(word[1]))
    if word[0]=="sort": 
        n.sort()
    if word[0]=="pop":
        n.pop()
    if word[0]=="reverse":
        n.reverse()  