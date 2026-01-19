"""
Preview HTML email in browser
"""
from jobs.rss import get_rss_jobs
from jobs.remotive import get_remotive_jobs
from report.daily import generate_daily_report
from report.weekly import generate_weekly_report
from datetime import datetime, timezone
import webbrowser
import os


def filter_jobs(jobs):
    keywords = ["junior", "entry", "intern", "associate", "trainee", "graduate",
                "developer", "engineer", "devops", "sre", "cloud", "backend",
                "frontend", "full stack", "fullstack", "web developer", "software"]
    
    return [job for job in jobs if any(kw in job['title'].lower() for kw in keywords)]


def preview_daily_email():
    print("Fetching jobs...")
    all_jobs = []
    
    try:
        rss_jobs = get_rss_jobs()
        all_jobs.extend(rss_jobs)
        print(f"✓ RSS Jobs: {len(rss_jobs)}")
    except Exception as e:
        print(f"✗ RSS Error: {e}")
    
    try:
        remotive_jobs = get_remotive_jobs()
        all_jobs.extend(remotive_jobs)
        print(f"✓ Remotive Jobs: {len(remotive_jobs)}")
    except Exception as e:
        print(f"✗ Remotive Error: {e}")
    
    filtered_jobs = filter_jobs(all_jobs)
    print(f"✓ Matching jobs: {len(filtered_jobs)}")
    print()
    
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    
    # Generate daily report
    subject, html_body = generate_daily_report(filtered_jobs, today)
    
    # Save to file
    with open("preview_daily.html", "w", encoding="utf-8") as f:
        f.write(html_body)
    
    print(f"Subject: {subject}")
    print(f"HTML saved to: preview_daily.html")
    print()
    
    # Open in browser
    webbrowser.open('file://' + os.path.realpath("preview_daily.html"))
    print("✓ Opening preview in browser...")


def preview_weekly_email():
    print("Fetching jobs for weekly preview...")
    all_jobs = []
    
    try:
        rss_jobs = get_rss_jobs()
        all_jobs.extend(rss_jobs)
    except:
        pass
    
    try:
        remotive_jobs = get_remotive_jobs()
        all_jobs.extend(remotive_jobs)
    except:
        pass
    
    filtered_jobs = filter_jobs(all_jobs)
    
    # Generate weekly report
    subject, html_body = generate_weekly_report(filtered_jobs)
    
    # Save to file
    with open("preview_weekly.html", "w", encoding="utf-8") as f:
        f.write(html_body)
    
    print(f"Subject: {subject}")
    print(f"HTML saved to: preview_weekly.html")
    print()
    
    # Open in browser
    webbrowser.open('file://' + os.path.realpath("preview_weekly.html"))
    print("✓ Opening preview in browser...")


if __name__ == "__main__":
    print("=" * 60)
    print("HTML EMAIL PREVIEW")
    print("=" * 60)
    print()
    
    print("1. Previewing Daily Email")
    print("-" * 60)
    preview_daily_email()
    
    print()
    print("2. Previewing Weekly Email")
    print("-" * 60)
    preview_weekly_email()
    
    print()
    print("=" * 60)
    print("Preview complete! Check your browser.")
    print("=" * 60)
