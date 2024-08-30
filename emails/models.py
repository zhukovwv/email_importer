from django.db import models


class EmailAccount(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    provider = models.CharField(max_length=50, choices=[('yandex', 'Yandex'), ('gmail', 'Gmail'), ('mailru', 'Mail.ru')])


class EmailMessage(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=255)
    sent_date = models.DateTimeField()
    received_date = models.DateTimeField()
    description = models.TextField()
    email_account = models.ForeignKey(EmailAccount, on_delete=models.CASCADE, related_name='messages')


class Attachment(models.Model):
    email_message = models.ForeignKey(EmailMessage, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='attachments/')
    content_type = models.CharField(max_length=100)
    size = models.PositiveIntegerField()

    def __str__(self):
        return self.file.name
