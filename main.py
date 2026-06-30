from src.tools.tools import web_search,scrape_url
from src.pipelines.pipeline import run_research_pipeline

# output = web_search.invoke("Recent advancements in AI research")
# print(output)
topic = "The impact of AI on the job market in 2026"
run_research_pipeline(topic)
# scraped_content = scrape_url.invoke({"url": "https://www.crescendo.ai/news/latest-ai-news-and-updates"})
# print(scraped_content)