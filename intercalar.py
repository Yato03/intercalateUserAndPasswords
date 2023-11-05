def load_pass():
    with open('pass.txt','r') as f:
        passwords = f.read().split("\n")
        return passwords

if __name__ == '__main__':
    my_user = "wiener"
    my_pass = "peter"

    victim_user = "carlos"

    passwords = load_pass()

    new_users = []
    new_pass = []

    for i in range(0,len(passwords)*2):
        if i%2==0:
            new_users.append(victim_user)
            new_pass.append(passwords[i//2])
        else:
            new_users.append(my_user)
            new_pass.append(my_pass)
    
    with open('new_users.txt','w') as f:
        for u in new_users:
            f.write(u + "\n")

    with open('new_pass.txt','w') as f:
        for p in new_pass:
            f.write(p + "\n")
