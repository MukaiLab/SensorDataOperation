# このファイルをimportして使ってください
# postDataの具体例と形式の詳細 https://fiware-tutorials.letsfiware.jp/Getting-Started/#_6
import requests, json


class SensorDataOperation:
    def __init__(self, dataType='dataType', deviceNumber='deviceNumber', postData=None, ipaddr='202.13.160.82:1026'):
        self.dataId = 'urn:ngsi-ld:'+ dataType +':'+ deviceNumber
        self.fiwareUrl = r'http://' + ipaddr + r'/v2/entities/'
        self.fiwareId = self.fiwareUrl + self.dataId
        self.postData = postData
        self.headers = {'Content-Type':'application/json',}
        self.fAPI = "?options=keyValues"


    def delete(self):
        return requests.delete(self.fiwareId)


    def post(self, postData=None):
        if postData is not None:
            self.postData = postData
        self.delete()
        return requests.post(self.fiwareUrl, headers=self.headers, data=json.dumps(self.postData))


    def get(self, need_metadata=True):
        if need_metadata:
            return requests.get(self.fiwareId)
        else:
            return requests.get(self.fiwareId + self.fAPI)


    def get_all(self, need_metadata=True):
        if need_metadata:
            return requests.get(self.fiwareUrl)
        else:
            return requests.get(self.fiwareUrl + self.fAPI)


if __name__ == '__main__':
    import datetime

    nowtime = str(datetime.datetime.now())
    dataType = 'HakusanTemperature'
    deviceNumber = '001'
    id = 'urn:ngsi-ld:'+ dataType +':'+ deviceNumber
    postData = { 
        "id": id,
        "type": dataType,
        "dateissued": {
            "type": "TimeDate",
            "value": nowtime
        },
        "location": {
            "type": "geo:json",
            "value": {
                "Type": "Point",
                "coordinates": [36.5313,136.6285]
            }
        },
        "temperature": {
            "type": "Temperature",
            "value": {
                "value": "25",
                "unit": "Degree"
            }
        }
    }

    sdo = SensorDataOperation(dataType=dataType, deviceNumber=deviceNumber, postData=postData)
    print(sdo.post())
    # a = SensorDataOperation().get_all().json()
    # print(a)
    getdata = sdo.get()
    print(getdata)
    print(getdata.json())
    print(sdo.delete())