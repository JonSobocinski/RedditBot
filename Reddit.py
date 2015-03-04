__author__ = 'TexasLonghorns'
import praw
from TopCommenter import TopCommenter

r = praw.Reddit(user_agent='Testing My First Reddit Bot by /u/HelioOne v.01')
submissions = r.get_subreddit('Longhornnation').get_hot(limit=5)
user_name = "HelioOne"
user = r.get_redditor(user_name)
thing_limit = 1000

# cast an item as a vars to see everything it has in it

sub = r.get_subreddit('LonghornNation').get_top_from_all(limit=thing_limit)

dict = {}
totalPosts = 0


for posts in sub:
    try:
        author = posts.author.name
        count = dict.get(author)
        if count is None:
            dict[author] = 1
        else:
            newCount = count + 1
            dict[author] = newCount
    except AttributeError:
        pass

totalPosts = 0
topList = list()
for x in dict:
    tc = TopCommenter(x, dict.get(x))
    totalPosts += 1
    topList.append(tc)


topList.sort(key=lambda y: y.score)

for y in topList:
    print("User: ", y.user," Posts: ", y.score)


print("Total Posts: ", totalPosts)


# gen = user.get_submitted(limit=thing_limit)
# comments = user.get_comments(limit=thing_limit)
# count = 1



#
# for com in comments:
#     print(count)
#     print("Comment: ", com.body)
#     print("Uppvotes: ", com.score)
#     print("Date: ", com.created_utc)
#     print("Link URL: ", com.link_url)
#     print("\n")
#     count += 1

# for thing in gen:
#     print(thing)
#
# for submission in submissions:
#     print(submission)
