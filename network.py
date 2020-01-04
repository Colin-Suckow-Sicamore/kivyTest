import requests
import json

novunexHeaders = {
           'ApiSubscriptionKey': '1012d419-4f89-4c62-864a-21cb5f9c1073',
           'AccountGuid': 'nox000000022',
           'SubscriptionId': '1',
           'ApiSubscriptionKeyUser':'sicamorebreakroom@gmail.com'
       }

def getInfoFromCardId(cardId):
    response = requests.get("https://public.novunex.app/api/public/entity/filter?entityTypeId=166&filter=IdCard=" + cardId, headers=novunexHeaders)
    responseJson = json.loads(response.text)
    return responseJson['List'][0]["Attributes"]