import SensorDataOperation


def main():
  dataType = 'SensorDataOperationTest'
  deviceNumber = '001'

  sdo = SensorDataOperation.SensorDataOperation(dataType=dataType, deviceNumber=deviceNumber)

  response = sdo.get()
  print(response)
  print(response.json())

if __name__ == "__main__":
  main()
