from pyvdp.visadirect import VisaDirectDispatcher


API = 'reports'
METHOD = 'transactiondata'


def get(from_date, to_date):
    """Fetches transaction report for given dates range.

    :param str from_date: **Required**. Starting date *ddmmyyyy*
    :param str to_date: **Required**. Ending date *ddmmyyyy*
    :return: CSV-formatted list of transactions.
    
    **Usage:**
    
    ..  code-block:: python
    
        from pyvdp.visadirect.reports import transactiondata
        
        result = transactiondata.get('31122015', '31122016')
        print(result)
    """
    query = '?fromDate=' + from_date + '&toDate=' + to_date
    c = VisaDirectDispatcher(api=API, method=METHOD, http_verb='get', query_string=query)
    return c.send()
