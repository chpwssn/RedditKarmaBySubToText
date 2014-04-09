import praw

user_agent = ("Karma breakdown to text v0.1 from /u/_Daimon_ by /u/chpwssn"
              "github.com/chpwssn/RedditKarmaBySubToText")
r = praw.Reddit(user_agent=user_agent)
thing_limit = 10000
user_name = "chpwssn"
output_filename = "output.txt"
user = r.get_redditor(user_name)
gen = user.get_submitted(limit=thing_limit)
karma_by_subreddit = {}
karma_by_subreddit_string = "Per-sub karma for "+user_name+"\n\n"
for thing in gen:
    subreddit = thing.subreddit.display_name
    karma_by_subreddit[subreddit] = (karma_by_subreddit.get(subreddit, 0)
                                     + thing.score)
for thing in karma_by_subreddit.items():
    karma_by_subreddit_string += str(thing[0])+" "+str(thing[1])+"\n"

outfile = open(output_filename, "w")
outfile.write(karma_by_subreddit_string)
outfile.close()




