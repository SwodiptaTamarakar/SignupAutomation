import imaplib
import email
import re
import time
from email.header import decode_header


class GmailReader:

    def __init__(self, gmail_user, app_password):
        self.gmail_user = gmail_user
        self.app_password = app_password

    def _clean(self, text):
        if not text:
            return ""
        return text.lower().replace(" ", "")

    def _decode(self, value):
        if not value:
            return ""
        parts = decode_header(value)
        decoded = ""
        for part, enc in parts:
            if isinstance(part, bytes):
                decoded += part.decode(enc or "utf-8", errors="ignore")
            else:
                decoded += part
        return decoded

    def get_otp(self, target_email, timeout=120): 

        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(self.gmail_user, self.app_password)
        mail.select("inbox")

        target_email = self._clean(target_email)
        start_time = time.time()

        while time.time() - start_time < timeout:

            result, data = mail.search(None, "ALL")
            if result != "OK":
                time.sleep(2)
                continue

            email_ids = data[0].split()
            if not email_ids:
                time.sleep(2)
                continue

            for email_id in reversed(email_ids):

                result, msg_data = mail.fetch(email_id, "(RFC822)")
                if result != "OK":
                    continue

                msg = email.message_from_bytes(msg_data[0][1])

                to_field = self._clean(msg.get("To", ""))
                subject = self._decode(msg.get("Subject", ""))

                print("TO:", to_field)
                print("SUBJECT:", subject)

                if target_email not in to_field:
                    continue

                body = ""

                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() in ["text/plain", "text/html"]:
                            payload = part.get_payload(decode=True)
                            if payload:
                                body += payload.decode(errors="ignore")
                else:
                    payload = msg.get_payload(decode=True)
                    if payload:
                        body = payload.decode(errors="ignore")

                otp_match = re.search(r"\b\d{6}\b", body)

                if otp_match:
                    print("OTP FOUND:", otp_match.group())
                    return otp_match.group()

            time.sleep(3)

        raise Exception("OTP not received in time")