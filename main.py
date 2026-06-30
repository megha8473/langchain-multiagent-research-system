from src.tools.tools import web_search,scrape_url

output = web_search.invoke("Recent advancements in AI research")
print(output)

# scraped_content = scrape_url.invoke({"url": "https://www.crescendo.ai/news/latest-ai-news-and-updates"})
# print(scraped_content)