command = ""
started = False
while True:
    command = input('ennter command: ').lower()
    if(command== 'start'):
        if started:
            print("Car is already started" )
        else:
            started=True
            print('Car started')
    elif(command=='stop'):
        print('car stopped')
    elif(command=='quit'):
        break
    elif command=='help':
        print("""start to start
        stop to stop
        help to help""")
