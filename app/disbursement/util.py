import requests
from requests.auth import HTTPBasicAuth
from disbursement.models import Disbursement

def update_disbursement(result_id, api_config):
    """
        update disbursement status

        Args:
            result_id = transaction id
            api_config = api configuration
                format:
                    {
                        'url':<url>, 
                        'user':<user>, 
                        'passwd':<passwd>,
                    }
        Return:
            status_code, message
    """
    headers =  {'Content-type': 'application/x-www-form-urlencoded'}

    response = requests.get("{}{}".format(api_config['url'], result_id), \
                    auth=HTTPBasicAuth(api_config['user'], api_config['passwd']), \
                        headers=headers)
    if response.status_code not in [200]:
        return 404, "Error on 3rd party!"

    dis = Disbursement.objects.filter(result_id=result_id).first()
    if dis:
        dis.status = response.json()['status']
        dis.time_served = response.json()['time_served']
        dis.receipt = response.json()['receipt']
        dis.save()

    return 200, response.json()

def save_disbursement(**kwargs):
    """
        save disbursement to DB

        Args:
            kwargs['result_id']: url of rest api
            kwargs['bank_code']: user
            kwargs['account_number']: password
            kwargs['amount']: amount 
            kwargs['status']: status 
            kwargs['remark']: remark
        Return:
            Disbursement object
    """

    dis = Disbursement(**kwargs)
    dis.save()

    return dis

def create_disbursement(**kwargs):
    """
        call disbursement api, return the result

        Args:
            kwargs['url']: url of rest api
            kwargs['user']: user
            kwargs['passwd']: password
            kwargs['bank_code']: bank code
            kwargs['account_number']: bank account number
            kwargs['amount']: amount 
            kwargs['remark']: remark
        Return:
            status_code, message
    """
    headers =  {'Content-type': 'application/x-www-form-urlencoded'}
    body = {
        'bank_code': kwargs['bank_code'],
        'account_number': kwargs['account_number'],
        'amount': kwargs['amount'],
        'remark': None if 'remark' not in kwargs else kwargs['remark']
    }

    response = requests.post(kwargs['url'], \
                    auth=HTTPBasicAuth(kwargs['user'], kwargs['passwd']), \
                        headers=headers, \
                            data=body)
    
    if response.status_code not in [200]:
        return 404, response
        
    return 200, response.json()