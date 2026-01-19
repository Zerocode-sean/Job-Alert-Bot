# Changelog

All notable changes to the Job Alert Bot project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-01-19

### Added
- 🎨 Beautiful HTML email templates with modern design
  - Gradient headers with professional branding
  - Card-based layout for job listings
  - Color-coded source badges (Remotive = Blue, RSS = Amber)
  - Mobile-responsive design
  - "Apply Now" buttons with direct links
- 📊 Weekly summary statistics
  - Total jobs count
  - Top source identification
  - Unique companies count
- 🎯 Expanded keyword filtering for better job matching
  - Added: developer, engineer, devops, sre, cloud, backend, frontend, full stack, web developer, software
  - Original: junior, entry, intern, associate, trainee, graduate
- 🔔 Always-notify feature
  - Sends notification even when no matching jobs found
  - Shows total jobs scanned and keywords used
- 🧪 Testing and preview tools
  - `preview_html.py` - Preview emails in browser
  - `test_local.py` - Test job fetching without sending emails
  - `check_jobs.py` - Test job filtering logic
  - `test_send_email.py` - Test email sending with credentials
- 🐛 Debug logging for email sending
  - Shows SMTP connection status
  - Displays credential availability
  - Detailed error messages
- 📚 Professional documentation
  - Comprehensive README with badges
  - MIT License
  - Detailed CHANGELOG

### Changed
- 📧 Email format upgraded from plain text to HTML
- 🔄 Updated `datetime.utcnow()` to `datetime.now(timezone.utc)` (Python 3.11+ best practice)
- 📝 Report subjects now include emoji and job counts
  - Daily: "🚀 Daily Job Alert - {date} - {count} Jobs Found!"
  - Weekly: "📊 Weekly Job Report - {date} - {count} Jobs This Week!"

### Fixed
- ✅ Missing `__init__.py` files in package directories
- ✅ Import path errors (changed `reports.` to `report.`)
- ✅ Error handling for Remotive API failures (526 errors)
- ✅ Graceful handling when no jobs match criteria

### Technical Details
- **Python Version**: 3.11+
- **Email Protocol**: SMTP_SSL (Gmail)
- **Automation**: GitHub Actions (cron: daily at 5:00 AM UTC / 8:00 AM EAT)
- **Job Sources**: 
  - RSS Feeds (WeWorkRemotely - DevOps and Programming)
  - Remotive API (with fallback on failure)

## [0.1.0] - 2026-01-15

### Added
- 🎉 Initial release
- Basic job scraping from Remotive API
- RSS feed parsing for WeWorkRemotely
- Plain text email notifications via Gmail
- Entry-level job filtering
- GitHub Actions workflow for automation
- Daily and weekly report generation

---

## Upcoming Features (Roadmap)

### [1.1.0] - Planned
- 📍 Location-based filtering
- 💰 Salary range filtering
- 🗄️ Job history database (SQLite)
- 📱 Telegram bot integration
- 🎯 User preferences configuration file

### [1.2.0] - Planned
- 🌐 Web dashboard for job browsing
- 🔍 Advanced search and filters
- 📈 Job market analytics
- 🔗 LinkedIn job integration
- 💼 Indeed job integration

### [2.0.0] - Planned
- 👥 Multi-user support
- 🎨 Customizable email themes
- 📊 Interactive charts in weekly reports
- 🤖 AI-powered job matching
- 📲 Discord webhook integration

---

## Release Notes Format

Each release follows this structure:

- **Added**: New features
- **Changed**: Changes to existing functionality
- **Deprecated**: Soon-to-be removed features
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Security improvements

---

**Note**: Dates are in YYYY-MM-DD format. Version numbers follow [Semantic Versioning](https://semver.org/).
