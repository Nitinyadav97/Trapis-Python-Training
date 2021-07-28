import instaloader as il
import os
import stdiomask

os.system('color a')
prompt='InstaBot'
mod = il.Instaloader()

def get_post():

    username = str(input('Enter the Username of required profile:'))
    state = True
    confirm = str(input('Do you want to download all post(y/n) : '))

    if confirm =='y':
        state = True

    mod.download_profile(username,profile_pic_only=state)

while True:

    print("type 'get posts' for retrieve all the posts or type 'q' for quit")
    cmd=str(input(prompt))
    if cmd == 'get posts':
        get_post()
    elif cmd == 'q':
        break