from django.shortcuts import render
import json
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from disbursement import util

URL = 'https://nextar.flip.id'
USER = 'HyzioY7LP6ZoO7nTYKbG8O4ISkyWnX1JvAEVAhtWKZumooCzqp41'

@api_view(['PUT','POST'])
@permission_classes([IsAuthenticated])
def disbursement(request, result_id=None):
    if request.method == 'POST':
        if result_id != None:
            return 404, "Parameters not valid!"

        request_body = json.loads(request.body.decode('utf-8'))
        required_fields = ['bank_code', 'account_number', 'amount', 'remark']
        for r in required_fields:
            if r not in request_body.keys():
                return 404, "Parameters not valid!"

        param = {
            'url':'{}/disburse'.format(URL), 
            'user':USER, 
            'passwd':'', 
            'bank_code':request_body['bank_code'], 
            'account_number':request_body['account_number'], 
            'amount':request_body['amount'],
            'remark': '' if 'remark' not in request_body else request_body['remark']
        }
        status_code, message = util.create_disbursement(**param)
        content = {
            'status_code':status_code,
            'message':message
        }

        if status_code == 200:
            param = {
                "result_id": message['id'],
                "amount": message['amount'],
                "status": message['status'],
                "bank_code": message['bank_code'],
                "account_number": message['account_number'],
                "receipt": message['receipt'],
                "time_served": message['time_served'] if message['time_served']!="0000-00-00 00:00:00" else None,
                "remark": message['remark']
            }
            util.save_disbursement(**param)
        else:
            return Response({'message':'create disbursement failed!', 'dump':message}, status=status.HTTP_404_NOT_FOUND)

        return Response(content, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        api_config = {
            'url':'{}/disburse/'.format(URL), 
            'user':USER, 
            'passwd':'',
        }

        result = util.update_disbursement(result_id, api_config)
        if result[0] not in [200]:
            return Response({'message':'parameter not valid!'}, status=status.HTTP_404_NOT_FOUND)
        return Response(result[1], status=status.HTTP_200_OK)

