
def format_post(post, platform):
    if platform == "linkedin":
        return post.replace(". ", ".\n\n")

    return post