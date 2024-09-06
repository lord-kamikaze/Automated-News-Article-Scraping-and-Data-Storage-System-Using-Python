import os
import newspaper
import feedparser

# Function to scrape news from an RSS feed URL
def scrape_news_from_feed(feed_url):
    articles = []
    feed = feedparser.parse(feed_url)
    for entry in feed.entries:
        # Create a newspaper article object
        article = newspaper.Article(entry.link)
        # Download and parse the article
        article.download()
        article.parse()
        # Extract relevant information
        articles.append({
            'title': article.title,
            'author': article.authors,
            'publish_date': article.publish_date,
            'content': article.text
        })
    return articles

# Specify a valid RSS feed URL from Times of India (Top Stories)
feed_url = 'https://timesofindia.indiatimes.com/rssfeedstopstories.cms'
articles = scrape_news_from_feed(feed_url)

# Create a new folder named 'scraped_articles' if it doesn't exist
folder_name = 'scraped_articles'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Save each article to a separate text file in the new folder
for i, article in enumerate(articles):
    # Create a file name based on the article's index and title
    file_name = f"{folder_name}/article_{i+1}.txt"
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(f"Title: {article['title']}\n")
        file.write(f"Author: {', '.join(article['author'])}\n")
        file.write(f"Publish Date: {article['publish_date']}\n")
        file.write(f"Content:\n{article['content']}\n")

print(f"Articles have been successfully saved in the '{folder_name}' folder.")
