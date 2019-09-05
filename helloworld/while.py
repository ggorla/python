guess_limit =1
while guess_limit<=5:
    print('*' * guess_limit)
    guess_limit= guess_limit + 1
print("DOne")
secret_number = 9
guess_limit=0

while guess_limit<3:
    guess = int(input('guess :'))
    guess_limit +=1
    if(guess==secret_number):
        print("you won")
        break
else:
    print("wrong guess")