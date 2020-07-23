from instapy import InstaPy

# Bot Login
bot = InstaPy(username="your username", password="your password")
bot.login()

# Sending Likes To Posts
hastags = ["python", "python3"] #You Could Change/Add Hashtags According To Your Niche/Category 
bot.like_by_tags(hastags, amount=4)

# Following The Posts That Bot Likes
bot.set_do_follow(True, percentage=50)

# Commenting On Posts
bot.set_do_comment(True, percentage=100)
comments = ["Awesome Post", "Great Content, Do Check Page"]
bot.set_comment(comments)

bot.end()
