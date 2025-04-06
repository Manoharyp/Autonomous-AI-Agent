def format_headlines(headlines):
    formatted = []
    for idx, headline in enumerate(headlines, 1):
        formatted.append(f"{idx}. {headline}")
    return formatted
