import raspberryfun

class CommandLine:
    """
    Class for ease the use of raspberryfun classes
    """
    def __init__(self):
        print("RaspberryFun commandline")
        self.__interpreter()
        
    def __interpreter(self):
        #Command interpreter
        command = ""
        while command != "exit":
            command = input("# ");
            if command == "help":
                print("Choose class:")
                print("lights\tfunctions for playing with leds")
                print("exit\tExit program")
            #Functions for lights class
            elif command == "lights":
                while command != "back":
                    with raspberryfun.Lights() as program:
                        command = input("lights# ");
                        if command == "help":
                            print("Choose function:")
                            print("all\t-\tlights up all led")
                            print("basic\t-\tbasic one way running light")
                            print("twoway\t-\ttwo way running light");
                            print("back\tgo back")
                        #LightUpAll
                        elif(command == "all"):
                            print("Press CTRL+C to stop")
                            program.LightUpAll()
                        #BasicRunningLight
                        elif(command == "basic"):
                            time = float(raw_input("time between led change[1.0]: "))
                            print("Press CTRL+C to stop")
                            program.BasicRunningLight(time)
                        #BasicTwoWayRunningLight
                        elif command == "twoway":
                            time = float(raw_input("time between led change[1.0]: "))
                            tail = int(input("tail size 1-5 [2]: "))
                            print("Press CTRL+C to stop")
                            program.BasicTwoWayRunningLight(time,tail)
                        elif command == "back":
                            continue
                        else:
                            print("Invalid command, insert help to list commands")
            #place for cleaning up
            elif command == "exit":
                print("bye")
            else:
                print("Invalid command, insert help to list commands")
                        
                    
