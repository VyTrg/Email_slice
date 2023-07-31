from Email_process import EmailProcess, printMsg

def main():
    emails = ["demmel@verizon.net", "jguyer@optonline.net"]
    for email in emails:
        email_username, email_domain = EmailProcess(email)
        printMsg(email_username, email_domain)

if __name__ == "__main__":
    main()