from datetime import datetime, timezone

from jobs.remotive import get_remotive_jobs
from jobs.rss import get_rss_jobs
from emailer.gmail import send_email
from report.daily import generate_daily_report
from report.weekly import generate_weekly_report


def fetch_all_jobs():
    jobs = []

    try:
        remotive_jobs = get_remotive_jobs()
        jobs.extend(remotive_jobs)
    except Exception as e:
        print(f"Error fetching Remotive jobs: {e}")

    try:
        rss_jobs = get_rss_jobs()
        jobs.extend(rss_jobs)
    except Exception as e:
        print(f"Error fetching RSS jobs: {e}")

    return jobs


def filter_entry_level_jobs(jobs):
    keywords = [
        "junior",
        "entry",
        "intern",
        "associate",
        "trainee",
        "graduate"
    ]

    filtered = []

    for job in jobs:
        title = job["title"].lower()

        if any(keyword in title for keyword in keywords):
            filtered.append(job)

    return filtered


def is_monday():
    return datetime.now(timezone.utc).weekday() == 0


def run():
    print("Starting Job Alert Bot...")

    jobs = fetch_all_jobs()

    if not jobs:
        print("No jobs retrieved from sources.")
        return

    entry_level_jobs = filter_entry_level_jobs(jobs)

    if not entry_level_jobs:
        print("No entry level jobs found today.")
        return

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    if is_monday():
        print("Generating weekly report...")
        subject, body = generate_weekly_report(entry_level_jobs)
    else:
        print("Generating daily report...")
        subject, body = generate_daily_report(entry_level_jobs, today)

    print("Sending email...")
    send_email(subject, body)

    print("Process completed successfully.")


if __name__ == "__main__":
    run()
