Ch8
===
8.2.4 利用第三方服務郵寄電子郵件
---
在此處使用 [django-anymail](https://github.com/anymail/django-anymail)

1. Install Anymail from PyPI:
```
$ pip install "django-anymail[mailgun]"
```

2. Edit your project's `settings.py`:
```
INSTALLED_APPS = [
    # ...
    "anymail",
    # ...
]

ANYMAIL = {
    # (exact settings here depend on your ESP...)
    "MAILGUN_API_KEY": "<your Mailgun key>",
    "MAILGUN_SENDER_DOMAIN": 'mg.example.com',  # your Mailgun domain, if needed
}
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"  # or sendgrid.EmailBackend, or...
DEFAULT_FROM_EMAIL = "you@example.com"  # if you don't already have this in settings
SERVER_EMAIL = "your-server@example.com"  # ditto (default from-email for Django errors)
```
3. Now the regular Django email functions will send through your chosen ESP:
```
from django.core.mail import send_mail

send_mail("It works!", "This will get sent through Mailgun",
          "Anymail Sender <from@example.com>", ["to@example.com"])
```
You could send an HTML message, complete with an inline image, custom tags and metadata:
```
from django.core.mail import EmailMultiAlternatives
from anymail.message import attach_inline_image_file

msg = EmailMultiAlternatives(
    subject="Please activate your account",
    body="Click to activate your account: https://example.com/activate",
    from_email="Example <admin@example.com>",
    to=["New User <user1@example.com>", "account.manager@example.com"],
    reply_to=["Helpdesk <support@example.com>"])

# Include an inline image in the html:
logo_cid = attach_inline_image_file(msg, "/path/to/logo.jpg")
html = """<img alt="Logo" src="cid:{logo_cid}">
          <p>Please <a href="https://example.com/activate">activate</a>
          your account</p>""".format(logo_cid=logo_cid)
msg.attach_alternative(html, "text/html")

# Optional Anymail extensions:
msg.metadata = {"user_id": "8675309", "experiment_variation": 1}
msg.tags = ["activation", "onboarding"]
msg.track_clicks = True

# Send it:
msg.send()
```
