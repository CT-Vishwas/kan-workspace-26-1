def username_extracter(email_id):
    return email_id[:email_id.find('@')]

if __name__ == '__main__':
    email = 'vishwas@cloudthat.com'
    username = username_extracter(email)

    print(f"The user name of {email} is {username}")