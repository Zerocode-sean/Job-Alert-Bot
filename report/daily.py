from report.html_template import create_html_email


def generate_daily_report(jobs, date):
    subject = f"🚀 Daily Job Alert - {date} - {len(jobs)} Jobs Found!"

    # Generate HTML email
    html_body = create_html_email(
        title=f"Daily Job Alert - {date}",
        jobs=jobs
    )

    return subject, html_body
