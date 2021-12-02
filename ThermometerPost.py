import datetime, SensorDataOperation


def main():
  nowtime = str(datetime.datetime.now())
  dataType = 'HakusanThermometer'
  deviceNumber = '001'

  sdo = SensorDataOperation.SensorDataOperation(dataType=dataType, deviceNumber=deviceNumber)

  postData = {
    "id": sdo.dataId,
    "type": dataType,
    "dateissued": {
      "type": "TimeDate",
      "value": nowtime
    },
    "location": {
      "type": "geo:json",
      "value": {
        "type": "Point",
        "coordinates": [136.6285,36.5313]
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
  
  print(postData)
  response = sdo.post(postData=postData)
  print(response)
  sdo.delete()

if __name__ == "__main__":
  main()
