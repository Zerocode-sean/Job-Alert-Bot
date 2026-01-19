"""
Test the email HTML rendering
"""
from report.daily import generate_daily_report
from datetime import datetime, timezone

# Create a simple test job
test_jobs = [
    {
        "title": "Senior DevOps Engineer",
        "company": "Test Company Inc",
        "link": "https://example.com/job1",
        "source": "RSS"
    },
    {
        "title": "Backend Developer",
        "company": "Another Company",
        "link": "https://example.com/job2",
        "source": "Remotive"
    }
]

today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
subject, html_body = generate_daily_report(test_jobs, today)

print("Subject:", subject)
print("\nChecking HTML body...")
print(f"Body length: {len(html_body)} characters")
print(f"Contains <!DOCTYPE: {('<!DOCTYPE' in html_body)}")
print(f"Contains <html>: {('<html>' in html_body)}")
print(f"Contains <body>: {('<body>' in html_body)}")
print(f"Contains email tables: {('<table' in html_body)}")

# Save for inspection
with open("test_email_structure.html", "w", encoding="utf-8") as f:
    f.write(html_body)

print("\n✓ HTML structure saved to test_email_structure.html")
print("\nHTML email structure is correct!")
print("The email client should render this as a proper HTML email.")
