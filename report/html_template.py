"""
HTML email templates for job alerts
"""


def create_html_email(title, jobs, summary_stats=None):
    """
    Create a beautiful HTML email for job alerts
    
    Args:
        title: Email title (e.g., "Daily Job Alert - 2026-01-19")
        jobs: List of job dictionaries
        summary_stats: Optional dict with statistics for weekly reports
    """
    
    # Color scheme
    PRIMARY_COLOR = "#2563eb"  # Blue
    SECONDARY_COLOR = "#f59e0b"  # Amber
    BG_COLOR = "#f8fafc"  # Light gray
    CARD_BG = "#ffffff"  # White
    TEXT_COLOR = "#1e293b"  # Dark slate
    TEXT_MUTED = "#64748b"  # Slate gray
    
    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
</head>
<body style="margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; background-color: {BG_COLOR};">
    
    <!-- Container -->
    <table width="100%" cellpadding="0" cellspacing="0" style="background-color: {BG_COLOR}; padding: 20px 0;">
        <tr>
            <td align="center">
                
                <!-- Main Content -->
                <table width="600" cellpadding="0" cellspacing="0" style="background-color: {CARD_BG}; border-radius: 12px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); overflow: hidden;">
                    
                    <!-- Header -->
                    <tr>
                        <td style="background: linear-gradient(135deg, {PRIMARY_COLOR} 0%, #1e40af 100%); padding: 40px 30px; text-align: center;">
                            <h1 style="margin: 0; color: white; font-size: 28px; font-weight: 700;">
                                🚀 Job Alert Bot
                            </h1>
                            <p style="margin: 10px 0 0 0; color: rgba(255, 255, 255, 0.9); font-size: 16px;">
                                {title}
                            </p>
                        </td>
                    </tr>
"""
    
    # Summary stats for weekly reports
    if summary_stats:
        html += f"""
                    <!-- Summary Stats -->
                    <tr>
                        <td style="padding: 30px;">
                            <h2 style="margin: 0 0 20px 0; color: {TEXT_COLOR}; font-size: 20px;">
                                📊 Weekly Summary
                            </h2>
                            <table width="100%" cellpadding="10" cellspacing="0">
                                <tr>
                                    <td style="background-color: {BG_COLOR}; border-radius: 8px; padding: 15px; text-align: center; width: 33%;">
                                        <div style="font-size: 32px; font-weight: 700; color: {PRIMARY_COLOR};">
                                            {summary_stats.get('total_jobs', 0)}
                                        </div>
                                        <div style="font-size: 14px; color: {TEXT_MUTED}; margin-top: 5px;">
                                            Total Jobs
                                        </div>
                                    </td>
                                    <td width="10"></td>
                                    <td style="background-color: {BG_COLOR}; border-radius: 8px; padding: 15px; text-align: center; width: 33%;">
                                        <div style="font-size: 32px; font-weight: 700; color: {SECONDARY_COLOR};">
                                            {summary_stats.get('top_source', 'N/A')}
                                        </div>
                                        <div style="font-size: 14px; color: {TEXT_MUTED}; margin-top: 5px;">
                                            Top Source
                                        </div>
                                    </td>
                                    <td width="10"></td>
                                    <td style="background-color: {BG_COLOR}; border-radius: 8px; padding: 15px; text-align: center; width: 33%;">
                                        <div style="font-size: 32px; font-weight: 700; color: #10b981;">
                                            {summary_stats.get('companies', 0)}
                                        </div>
                                        <div style="font-size: 14px; color: {TEXT_MUTED}; margin-top: 5px;">
                                            Companies
                                        </div>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
"""
    
    # Jobs section
    if jobs:
        html += f"""
                    <!-- Jobs List -->
                    <tr>
                        <td style="padding: 0 30px 30px 30px;">
                            <h2 style="margin: 0 0 20px 0; color: {TEXT_COLOR}; font-size: 20px;">
                                💼 Available Positions ({len(jobs)})
                            </h2>
"""
        
        # Job cards
        for i, job in enumerate(jobs, 1):
            # Determine source badge color
            source = job.get('source', 'Unknown')
            badge_color = PRIMARY_COLOR if source == 'Remotive' else SECONDARY_COLOR
            
            html += f"""
                            <!-- Job Card {i} -->
                            <table width="100%" cellpadding="0" cellspacing="0" style="margin-bottom: 15px; border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden;">
                                <tr>
                                    <td style="padding: 20px;">
                                        <table width="100%" cellpadding="0" cellspacing="0">
                                            <tr>
                                                <td>
                                                    <h3 style="margin: 0 0 8px 0; color: {TEXT_COLOR}; font-size: 18px; font-weight: 600;">
                                                        {job.get('title', 'N/A')}
                                                    </h3>
                                                    <p style="margin: 0 0 12px 0; color: {TEXT_MUTED}; font-size: 14px;">
                                                        🏢 {job.get('company', 'Unknown Company')}
                                                    </p>
                                                </td>
                                                <td align="right" valign="top">
                                                    <span style="background-color: {badge_color}; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px; font-weight: 600; white-space: nowrap;">
                                                        {source}
                                                    </span>
                                                </td>
                                            </tr>
                                        </table>
                                        
                                        <!-- Apply Button -->
                                        <a href="{job.get('link', '#')}" style="display: inline-block; margin-top: 12px; padding: 10px 20px; background-color: {PRIMARY_COLOR}; color: white; text-decoration: none; border-radius: 6px; font-size: 14px; font-weight: 600;">
                                            Apply Now →
                                        </a>
                                    </td>
                                </tr>
                            </table>
"""
    else:
        html += f"""
                    <!-- No Jobs Message -->
                    <tr>
                        <td style="padding: 40px 30px; text-align: center;">
                            <div style="font-size: 48px; margin-bottom: 20px;">😔</div>
                            <h2 style="margin: 0 0 10px 0; color: {TEXT_COLOR}; font-size: 20px;">
                                No Jobs Found Today
                            </h2>
                            <p style="margin: 0; color: {TEXT_MUTED}; font-size: 16px;">
                                Don't worry! We'll keep looking and notify you tomorrow.
                            </p>
                        </td>
                    </tr>
"""
    
    # Footer
    html += f"""
                        </td>
                    </tr>
                    
                    <!-- Footer -->
                    <tr>
                        <td style="background-color: {BG_COLOR}; padding: 30px; text-align: center; border-top: 1px solid #e2e8f0;">
                            <p style="margin: 0 0 10px 0; color: {TEXT_MUTED}; font-size: 14px;">
                                This email was automatically generated by your Job Alert Bot
                            </p>
                            <p style="margin: 0; color: {TEXT_MUTED}; font-size: 12px;">
                                Running daily at 8:00 AM EAT (Kenya Time)
                            </p>
                            <p style="margin: 15px 0 0 0; color: {TEXT_MUTED}; font-size: 12px;">
                                💪 Keep pushing – your next opportunity is coming!
                            </p>
                        </td>
                    </tr>
                    
                </table>
                
            </td>
        </tr>
    </table>
    
</body>
</html>
"""
    
    return html
