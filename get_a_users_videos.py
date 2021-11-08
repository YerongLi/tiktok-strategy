from TikTokApi import TikTokApi
import sys
# Starts TikTokApi
api = TikTokApi.get_instance()

# The Number of trending TikToks you want to be displayed
results = 1000

# Returns a list of dictionaries of the trending object
userPosts = api.user_posts(
    "6722284375361356805",
    "MS4wLjABAAAAM3R2BtjzVT-uAtstkl2iugMzC6AtnpkojJbjiOdDDrdsTiTR75-8lyWJCY5VvDrZ",
    results,
)
# Loops over every tiktok
for tiktok in userPosts:
    # Prints the text of the tiktok
    print(tiktok)
    sys.exit()

print(len(userPosts))
