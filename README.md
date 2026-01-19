# 🚀 Job Alert Bot

[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-Automated-blue)](https://github.com/Zerocode-sean/Job-Alert-Bot/actions)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An automated job alert system that scrapes IT and DevOps job listings from multiple sources and sends beautiful HTML email notifications daily.

## ✨ Features

- 🔄 **Automated Daily Scraping** - Runs automatically every day at 8:00 AM EAT (Kenya Time)
- 📧 **Beautiful HTML Emails** - Professional, mobile-responsive email templates
- 🎯 **Smart Filtering** - Keywords-based filtering for relevant IT/DevOps positions
- 📊 **Weekly Summaries** - Comprehensive weekly reports every Monday
- 🌐 **Multiple Sources** - Aggregates jobs from:
  - RSS Feeds (WeWorkRemotely)
  - Remotive API
- 🔔 **Always Notified** - Sends updates even when no jobs match criteria
- 🎨 **Modern Design** - Gradient headers, card layouts, and color-coded badges

## 📋 Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Customization](#customization)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## 🛠️ Prerequisites

- Python 3.11 or higher
- Gmail account with App Password enabled
- GitHub account (for automated runs)

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Zerocode-sean/Job-Alert-Bot.git
   cd Job-Alert-Bot
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   ```bash
   # For local testing
   export SMTP_EMAIL="your-email@gmail.com"
   export SMTP_PASSWORD="your-app-password"
   ```

## ⚙️ Configuration

### Gmail App Password Setup

1. Enable 2-Factor Authentication on your Google Account
2. Go to [Google App Passwords](https://myaccount.google.com/apppasswords)
3. Generate a new app password for "Mail"
4. Copy the 16-character password (remove spaces)

### GitHub Secrets Setup

For automated runs via GitHub Actions:

1. Go to your repository → **Settings** → **Secrets and variables** → **Actions**
2. Add the following secrets:
   - `SMTP_EMAIL` - Your Gmail address
   - `SMTP_PASSWORD` - Your Gmail App Password (16 characters, no spaces)

## 🚀 Usage

### Local Testing

```bash
# Run the bot locally
python main.py

# Preview HTML emails in browser
python preview_html.py

# Test specific components
python test_local.py
python check_jobs.py
```

### Automated Runs (GitHub Actions)

The bot runs automatically via GitHub Actions:
- **Daily**: Every day at 5:00 AM UTC (8:00 AM EAT)
- **Manual**: Trigger from Actions tab → "Job Alert Automation" → "Run workflow"

## 📁 Project Structure

```
Job-Alert-Bot/
├── .github/
│   └── workflows/
│       └── job-alert.yml       # GitHub Actions workflow
├── emailer/
│   ├── __init__.py
│   └── gmail.py                # Email sending functionality
├── jobs/
│   ├── __init__.py
│   ├── remotive.py             # Remotive API scraper
│   └── rss.py                  # RSS feed scraper
├── report/
│   ├── __init__.py
│   ├── daily.py                # Daily report generator
│   ├── weekly.py               # Weekly report generator
│   └── html_template.py        # HTML email templates
├── main.py                     # Main application entry point
├── requirements.txt            # Python dependencies
├── preview_html.py             # HTML email preview tool
├── test_local.py               # Local testing script
├── check_jobs.py               # Job filtering test
├── README.md                   # This file
├── LICENSE                     # MIT License
└── CHANGELOG.md                # Version history
```

## 🎨 Customization

### Modify Job Keywords

Edit `main.py` to change the keywords used for filtering:

```python
def filter_entry_level_jobs(jobs):
    keywords = [
        "junior", "entry", "intern",
        "developer", "engineer", "devops",
        # Add your custom keywords here
    ]
```

### Add More Job Sources

Create a new scraper in the `jobs/` directory:

```python
# jobs/your_source.py
def get_your_source_jobs() -> list[dict[str, str]]:
    # Your scraping logic here
    return jobs
```

Then import and use it in `main.py`:

```python
from jobs.your_source import get_your_source_jobs

# In fetch_all_jobs()
your_jobs = get_your_source_jobs()
jobs.extend(your_jobs)
```

### Customize Email Design

Modify `report/html_template.py` to change:
- Colors (PRIMARY_COLOR, SECONDARY_COLOR, etc.)
- Layout and styling
- Content structure

### Change Schedule

Edit `.github/workflows/job-alert.yml`:

```yaml
schedule:
  - cron: "0 5 * * *"  # Change to your preferred time (UTC)
```

## 🧪 Testing

### Preview Emails Locally

```bash
# Generate and open HTML emails in browser
python preview_html.py
```

### Test Job Scraping

```bash
# Test fetching and filtering jobs
python check_jobs.py
```

### Test Full Flow

```bash
# Run the complete bot (without sending email if no env vars)
python test_local.py
```

## 🐛 Troubleshooting

### No Email Received

1. **Check GitHub Secrets** - Ensure SMTP_EMAIL and SMTP_PASSWORD are correctly set
2. **Verify App Password** - Must be 16 characters, no spaces
3. **Check Spam Folder** - Gmail might filter automated emails
4. **Review Workflow Logs** - Check GitHub Actions logs for errors

### No Jobs Found

- **Remotive API Down** - The bot continues with RSS feeds
- **Keywords Too Restrictive** - Modify filter keywords in `main.py`
- **Check Sources** - Verify RSS feeds are accessible

### Workflow Not Running

1. **Check Actions Tab** - Ensure workflows are enabled in repository settings
2. **Trigger Manually** - Use "Run workflow" button for immediate testing
3. **Check Permissions** - Ensure Actions have necessary permissions

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Ideas for Contributions

- Add more job sources (LinkedIn, Indeed, etc.)
- Implement job filtering by location
- Add database storage for job history
- Create a web dashboard
- Add Telegram/Discord notifications
- Implement salary range filtering

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Remotive](https://remotive.io/) - Remote job listings API
- [WeWorkRemotely](https://weworkremotely.com/) - RSS job feeds
- [GitHub Actions](https://github.com/features/actions) - Free automation platform

## 📧 Contact

**Sean** - [@Zerocode-sean](https://github.com/Zerocode-sean)

Project Link: [https://github.com/Zerocode-sean/Job-Alert-Bot](https://github.com/Zerocode-sean/Job-Alert-Bot)

---

<div align="center">
  <strong>⭐ Star this repository if you find it helpful!</strong>
  <br>
  <sub>Built with ❤️ by Sean | Keep pushing – your next opportunity is coming!</sub>
</div>
