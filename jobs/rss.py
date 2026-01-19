import feedparser


RSS_FEEDS = [
    "https://weworkremotely.com/categories/remote-devops-sysadmin-jobs.rss",
    "https://weworkremotely.com/categories/remote-programming-jobs.rss"
]


def get_rss_jobs():
    jobs = []

    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)

        for entry in feed.entries:
            title = entry.get("title", "")
            link = entry.get("link", "")
            
            # Extract company and job title from the format "Company: Job Title"
            if ":" in title:
                parts = title.split(":", 1)
                company = parts[0].strip()
                job_title = parts[1].strip()
            else:
                company = entry.get("author", "Unknown")
                job_title = title

            jobs.append({
                "title": job_title,
                "company": company,
                "link": link,
                "source": "RSS"
            })

    return jobs
