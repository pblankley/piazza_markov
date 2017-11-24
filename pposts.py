
import piazza_api as pa

# Network id corresponding to the AC209a course at Harvard Fall 2017
network_id = 'j6qqcqfmotn3ox'
user = 'your-harvard-email'
password = 'your-piazza-password'

pi = pa.piazza.Piazza()
pi.user_login(user,password)
ac209 = pi.network(network_id)

ac209_stats = ac209.get_statistics()

posts_itr = ac209.iter_all_posts()

text=''
for i,post in enumerate(posts_itr):
    #print('post %s'%i,post)
    if 'instructor-note' not in post['tags']:
        text+=post['history'][0]['content']

print("####################################################")
print(text)
with open("piazza_posts.txt", "w") as text_file:
    text_file.write(text)



