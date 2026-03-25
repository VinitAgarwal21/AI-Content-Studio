
def validate_post(post, platform):
    if platform == "twitter" and len(post) > 280:
        return False, "Too long for Twitter"

    return True, "OK"