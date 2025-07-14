from src.email_validation.util import filter_mail

n = int(input())
emails = []
for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
# filtered_emails.sort()
print(filtered_emails)

'''
sample input
3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com

sample output
['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
'''