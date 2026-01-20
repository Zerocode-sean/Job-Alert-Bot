import feedparser


RSS_FEEDS = [
    # WeWorkRemotely
    "https://weworkremotely.com/categories/remote-devops-sysadmin-jobs.rss",
    "https://weworkremotely.com/categories/remote-programming-jobs.rss",
    "https://weworkremotely.com/categories/remote-back-end-programming-jobs.rss",
    "https://weworkremotely.com/categories/remote-front-end-programming-jobs.rss",
    "https://weworkremotely.com/categories/remote-full-stack-programming-jobs.rss",
    
    # RemoteOK (alternative RSS source)
    "https://remoteok.com/remote-dev-jobs.rss",
    "https://remoteok.com/remote-devops-jobs.rss",
    "https://remoteok.com/remote-python-jobs.rss",
    "https://remoteok.com/remote-javascript-jobs.rss",
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
