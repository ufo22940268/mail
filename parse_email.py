from gmail import Gmail

# Print body of all emails.
#
# Usage

# - git clone git://github.com/charlierguo/gmail.git
# - cd gmail && python setup.py install
# - cd .. && python parse_email.py

g = Gmail()
g.login('aabbccni@gmail.com', 'a12345678')
for mail in g.inbox().mail():
    mail.fetch()
    print mail.body
g.logout()
