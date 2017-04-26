from pyvdp.visadirect import VisaDirectDispatcher


def get(data):
    """Fetches transaction report for given dates range.

    :param dict data: **Required**. Dictionary with dates range.
    :return: CSV-formatted list of transactions.
    
    **Usage:**
    
    ..  code:: python
    
        from pyvdp.visadirect.reports import transactiondata
        
        data = {
            "fromDate": "31122015",
            "toDate": "31122016"
        }
        
        result = transactiondata.get(data)
        print(result)
        
    **Response:**
    
    ..  code:: text
    
        Processing Date,Acquirer Bin,Visa Transaction ID,Transaction State,Reason Code,Card Acceptor ID,Card Acceptor Name,System Trace Audit Number,Account Number Masked,Transaction Date,Transaction Time,Transaction Amount,Transaction Currency,Auth Code,RRN,FeeProgramIndicator Code,FeeProgramIndicator Desc,Settlement Datetime 
        2016-02-02,408999,528706215101,CRED VOUCHER,NOT APPLICABLE,Cardacceptor_1,VISA MONEY TRANSFER,215101,429393XXXXXX7715,2016-02-14,032206,2461.37,840,082541,528706215101,,ORIGINAL CREDIT,2016-02-02:325 
        2016-02-02,408999,585032554732529,CRED REVERSAL,TRANSACTION NOT COMPLETED/TIMEOUT,Cardacceptor_1,VISA MONEY TRANSFER,465493,2009EDXXXXXXCF17,2015-02-01,152429,14.32,840,312448,503215465493,,VMT FF NATL,2016-02-02:2017 
        2016-02-02,408999,528706215101,CRED VOUCHER,NOT APPLICABLE,Cardacceptor_1,VISA MONEY TRANSFER,215101,429393XXXXXX7715,2016-02-14,032206,2461.37,840,082541,528706215101,,ORIGINAL CREDIT,2016-02-02:325 
        2016-03-02,408999,385274484362603,CRED CHGBK,CREDIT NOT PROCESSED,Cardacceptor_1,VISA MONEY TRANSFER,616315,479325XXXXXX0000716,2015-10-01,012716,68.18,840,000000,527413616315,,OCTRANFR NATL,2016-03-02:2226 
        2016-02-02,408999,385274484362603,SALES DRAFT,NOT APPLICABLE,Cardacceptor_1,VISA MONEY TRANSFER,616315,479325XXXXXX0000716,2015-10-01,012716,68.18,840,000000,527413616315,,OCTRANFR NATL,2016-03-02:2226 
        2016-04-02,408999,585032554732529,SALES REVERSAL,TRANSACTION NOT COMPLETED/TIMEOUT,Cardacceptor_1,VISA MONEY TRANSFER,465493,2009EDXXXXXXCF17,2015-02-01,152429,14.32,840,312448,503215465493,,VMT FF NATL,2016-04-02:2017
    """
    c = VisaDirectDispatcher(resource='visadirect',
                             api='reports',
                             version='v1',
                             method='transactiondata',
                             http_verb='GET',
                             auth_method='ssl',
                             data=data)
    return c.send()
