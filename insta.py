import instaloader
import getpass, sys

L = instaloader.Instaloader()

username = input('Enter Username: ')

if sys.stdin.isatty():
    password = getpass.getpass(prompt='Enter Password: ')
else:
   password = input('Enter Password: ')

# Login
try:
    L.login(username, password)
    print('Login Sucessful\n')
except:
    print('Login Error, Try Again')
    quit()


# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, username)

# Get list of followers and following
followers = profile.get_followers()
following = profile.get_followees()

f1 = [i for i in followers]
f2 = [i for i in following]

print(len(f1), 'followers')
print(len(f2), 'following\n')

#Print users in following who are not in followers
for i in f2:
    if i not in f1:
        print(i.username)


