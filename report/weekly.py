from collections import Counter
from datetime import datetime, timezone
from report.html_template import create_html_email


def generate_weekly_report(jobs):
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    subject = f"📊 Weekly Job Report - {today} - {len(jobs)} Jobs This Week!"

    if not jobs:
        html_body = create_html_email(
            title=f"Weekly Job Report - {today}",
            jobs=[]
        )
        return subject, html_body

    # Calculate statistics
    total_jobs = len(jobs)
    companies = [job["company"] for job in jobs]
    sources = [job["source"] for job in jobs]
    
    unique_companies = len(set(companies))
    source_count = Counter(sources)
    top_source = source_count.most_common(1)[0][0] if source_count else "N/A"

    summary_stats = {
        'total_jobs': total_jobs,
        'companies': unique_companies,
        'top_source': top_source
    }

    # Generate HTML email
    html_body = create_html_email(
        title=f"Weekly Job Report - {today}",
        jobs=jobs,
        summary_stats=summary_stats
    )

    return subject, html_body
