from hal import hal_input_switch as switch
from hal import hal_led as leds
from time import sleep



def main():
    switch.init()
    leds.init()
    i = 0

    while 1:
        if switch.read_slide_switch() == 1:
            leds.set_output(24,1)
            sleep(0.1)
            leds.set_output(24,0)
            sleep(0.1)
            i = 0
        else:
            if i < 25:
                i += 1
                sleep(0.05)
                leds.set_output(24,1)
                sleep(0.05)
                leds.set_output(24,0)




if __name__ == "__main__":
    main()