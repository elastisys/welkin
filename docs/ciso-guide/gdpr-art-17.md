---
tags:
  - GDPR Art. 17 Right to erasure ("right to be forgotten")
  - ISO 27001 Annex A 8.10 Information Deletion
---

<!-- markdownlint-disable-file first-line-h1 -->

{%
   include-markdown './controls/_common.include'
   start='<!--legal-disclaimer-start-->'
   end='<!--legal-disclaimer-end-->'
%}

# How do I comply with GDPR Art. 17 Right to erasure ("right to be forgotten")?

Here is how we recommend to comply with GDPR Art. 17 if you host your application on Welkin.

Note that, this page assumes you have no other sub-processors than your Welkin supplier.

## Preparation

Prepare as follows:

1. **Map out** where you store personal data. Besides production database and production PersistentVolumes, this may include backups, audit logs and application logs.
1. **Check the retention period** of backups and logs. By default, there are 30 days in Welkin, but can be changed if needed.
1. **Devise a process to remember to re-delete forgotten data** after disaster recovery. For example, you might want to review all GDPR Art. 17 requests received within the last 30 days after restoring data from backups.

## When receiving a request from a data subject

Once you have these in place, we recommend you proceed as follows when receiving a request from a data subject.

1. **Track** the request of the data subject in some internal system, e.g., email or a service ticket system. Try to keep as little personal data as possible, e.g., only contact email.
1. **Delete data from the production database**. No need to write code. Just issue a command like `DELETE FROM users WHERE userId=?`. Welkin will record in its audit logs that an Application Developer connected directly to the database. For extra security via traceability, you can even enable PostgreSQL audit logs.
1. **Reply** to the data subject with an email like the following. This email assumes the default backup and log retention period of 30 days.

    > Hello data subject,
    >
    > As requested, we removed your personal data from our database.
    >
    > Please note that your data may persist for 30 days in our backups, audit logs and application logs. We have procedures in place to make sure that we re-delete your personal data if we ever need to restore from backups within the next 30 days.
    >
    > After 30 days, your personal data will be removed from backups and I will delete this email, so you will be forever forgotten.

1. **Delete the request** from your internal system after 30 days.

## Further Reading

- [Audit Logs](audit-logs.md)
- [Application Logs](../user-guide/logs.md)
- [Backups](../user-guide/backup.md)
