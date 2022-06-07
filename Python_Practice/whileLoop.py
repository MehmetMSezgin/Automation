i = 1
while i<=50:
    print("MAMINI")
    if i%5==0:
        print("microfon show")
    if i%10==0:
        print("mimini")
    i+= 1

#####################
secret_word = "password"
guess = ""
attempt = 0
out_of_guess = False
while guess != secret_word and not (out_of_guess):
    if attempt <=3:
        guess = input("again: ")
        attempt +=1
    else:
        out_of_guess = True

if guess == secret_word:
    print("founded!!!")
else:
    print("failed!!!")