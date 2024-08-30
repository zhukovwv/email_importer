import imaplib
import email
from .models import EmailMessage


def fetch_emails(email_address, password, provider):

    return [
        {
            'id': 1,
            'subject': 'Тема письма',
            'sent_date': '2023-12-31 12:00:00',
            'received_date': '2023-12-31 12:01:00',
            'description': 'Текст письма...',
            'attachments': ['file1.pdf', 'file2.png']
        }
    ]