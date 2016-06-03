from gmail import Gmail


# Print body of all emails.
#
# Usage

# - git clone git://github.com/charlierguo/gmail.git
# - cd gmail && python setup.py install
# - cd .. && python parse_email.py

def find_test(g):
    for mail in g.inbox().mail():
        mail.fetch()
        if 'test' in mail.subject and 'test' in mail.body:
            return True
    return False

if __name__ == '__main__':
    g = Gmail()
    g.login('aabbccni@gmail.com', 'a12345678')
    print 'Test can be found in body and title' if find_test(g) else 'Test not found in body and title'
    g.logout()
