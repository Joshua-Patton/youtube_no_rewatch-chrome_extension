from browser_history.browsers import Edge


def get_youtube_history():
    e = Edge()
    outputs = e.fetch_history()
    # his is a list of (datetime.datetime, url) tuples
    return [url[1] for url in outputs.histories if "www.youtube.com" in url[1]]

print(get_youtube_history())

