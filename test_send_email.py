"""
Test email sending with actual credentials (for local testing with env vars)
Set environment variables first:
  $env:SMTP_EMAIL="your-email@gmail.com"
  $env:SMTP_PASSWORD="your-app-password"
Then run: python test_send_email.py
"""
import os
from emailer.gmail import send_email

def test_send():
    print("Testing email sending...")
    print()
    
    # Check credentials
    if not os.getenv("SMTP_EMAIL") or not os.getenv("SMTP_PASSWORD"):
        print("❌ Environment variables not set!")
        print()
        print("To test locally, first set:")
        print('  $env:SMTP_EMAIL="your-email@gmail.com"')
        print('  $env:SMTP_PASSWORD="your-16-char-app-password"')
        print()
        print("Then run this script again.")
        return
    
    # Send test email
    subject = "Job Alert Bot - Test Email"
    body = """This is a test email from your Job Alert Bot.

If you receive this, your email configuration is working correctly!

The bot will send you daily job alerts at 8:00 AM Kenya Time.

Test completed successfully.
"""
    
    try:
        send_email(subject, body)
        print()
        print("✅ Test email sent successfully!")
        print("📧 Check your inbox (and spam folder just in case)")
    except Exception as e:
        print()
        print(f"❌ Failed to send email: {e}")

if __name__ == "__main__":
    test_send()
