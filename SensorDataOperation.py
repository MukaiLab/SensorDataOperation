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
    dataType = 'SensorDataOperationTest'
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
                "type": "Point",
                "coordinates": [136.6285, 36.5313]
            }
        },
        "SensorDataOperationTest": {
            "type": "Text",
            "value": "SensorDataOperationTest"
        }
    }

    # インスタンス化。 dataTypeとdeviceNumberは必須。
    sdo = SensorDataOperation(dataType=dataType, deviceNumber=deviceNumber)
    # ここでpostDataを引数に入れてもよい。後で変えることもできる。
    # sdo = SensorDataOperation(dataType=dataType, deviceNumber=deviceNumber, postData=postData)

    # postDataをpostする。 新しくデータをpostする場合はここでpostDataを引数に入れる。
    print(sdo.post(postData=postData))
    # インスタンス化する際にpostDataを引数に入れている場合はここでの引数は無くても良い。
    # print(sdo.post())

    # FIWAREにあるデータを全部getする。
    # a = SensorDataOperation().get_all()
    # a = sdo.get_all() # 上の行と同じ。
    # print(a)
    # print(a.json())

    # getする
    getdata = sdo.get()
    print(getdata)

    # getしたデータをjson形式で表示する
    print(getdata.json())

    # postしたデータをdeleteする
    print(sdo.delete())

    # fiwareURL
    print(sdo.fiwareUrl)
    
    # dataId
    print(sdo.dataId)

    # fiwareId
    print(sdo.fiwareId)
