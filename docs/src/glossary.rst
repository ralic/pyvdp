.. glossary


========
Glossary
========

This is a glossary on the specific terms and definitions, that are used across payment systems world

..  glossary::

    Account Funding Transaction (AFT)
        Pull-type of transaction, used to pull funds from a sender's account as opposed by OCT push-type.
        Usually AFT preceeds OCT.

    Account Funding Transaction Reversal (AFTR)
        A reversal to AFT

    Original Credit Transaction (OCT)
        Push-type of transaction, used to push funds to recipient's account. Usually performed after AFT.

    Original Credit Transaction Reversal (OCTR)
        A reversal to OCT

    Systems Trace Audit Number (STAN)
        6-digit unique positive integer required for any transaction. However when performing AFTR, it must match original
        STAN, used for original AFT transaction.

    Retrieval Reference Number (RRN)
        12-symbols string used to tie together service calls related to a single financial transaction. When passing AFT
        and OCT, RRN must differ between this two calls. When passing AFTR, RRN must match RRN value, used for original
        AFT transaction. Recommended format is ydddhhnnnnnn, where:
        - y - last digit of current year (0-9)
        - ddd - number of current day in the year (001-366)
        - hh - two digit hour (00-23)
        - nnnnnnn - any 6 digits, usually STAN

    Bank Identification Number (BIN)
        stub

    Primary Account Number (PAN)
        stub

    Customer Authentication Verification Value (CAVV)
        stub

    Business Application Identifier (BAI)
        stub

    Card Verification Value (CVV)
        stub
