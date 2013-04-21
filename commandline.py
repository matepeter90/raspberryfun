import raspberryfun
import cmd

class CommandLine(cmd.Cmd):
    """ Class for ease the use of raspberryfun classes """

    intro = "RaspberryFun commandline"
    prompt = '# '
    ruler = '-'

    def do_lights(self, line):
        """Commands for Lights class"""
        LightsCommand().cmdloop()

    def do_exit(self, line):
        """ Exit cmd """
        return True

    def do_EOF(self, line):
        return True
    
class SubCommand(cmd.Cmd):
    """ Base class for raspberryfun class commands"""

    def do_exit(self, line):
        """ Exit cmd """
        return True
    
    def do_EOF(self, line):
        return True

class LightsCommand(SubCommand):
    """ Class for raspberryfun Lights commands """
    prompt = "lights# "
    
    def do_all(self, line):
        """ LightUpAll """
        with raspberryfun.Lights() as program:
            print("Press CTRL+C to stop")
            program.LightUpAll()
        
    def do_basic(self, line):
        """
            Basic one direction running light
            time -- timestep between leds [sec]
        """
        with raspberryfun.Lights() as program:
            if time == "":
                time = 1.0
            else:
                try:
                    time = float(line)
                except:
                    print("Invalid value, using default")
                    time = 1.0
                    print("Press CTRL+C to stop")
                    program.BasicRunningLight(time)
                    
    def do_twoway(self, line):
        """
           Two way running light
           time -- timestep between leds [sec]
           tail -- how much led should be lit
        """
        args = line.split()
        if len(args) != 2:
            print("Invalid number of arguments should be two: time tail")
        with raspberryfun.Lights() as program:
            try:
                time = float(args[0])
            except:
                print("Invalid value, using default")
                time = 1.0
            try:
                tail = int(args[1])
            except:
                print("Invalid value, using default")
                tail = 2
            print("Press CTRL+C to stop")
            program.BasicTwoWayRunningLight(time,tail)
        
    
