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
total = 0


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
    if dict.get(x) > 5:
        tc = TopCommenter(x, dict.get(x))
        totalPosts += 1
        total = total + tc.score
        topList.append(tc)


topList.sort(key=lambda y: y.score, reverse=True)

topCommenter = 1
for y in topList:
    print(topCommenter, ") /u/", y.user, " has posted ", y.score, " posts in the top ", total, " posts of all time. ",
          "{:.1f}".format(100*(y.score/total)), "% of all top posts  \n", sep='')
    topCommenter += 1


# print("Total Users: ", totalPosts)
# print("Total Posts: ", total)


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
