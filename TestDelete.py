import SensorDataOperation


def main():
  dataType = 'SensorDataOperationTest'
  deviceNumber = '001'

  sdo = SensorDataOperation.SensorDataOperation(dataType=dataType, deviceNumber=deviceNumber)

  response = sdo.delete()
  print(response)

if __name__ == "__main__":
  main()
