import sys, time
import rpk_sounds as sm

def kart_timer():
    sm.ktimer3()
    # live countdown
    _TIME = 3
    while _TIME > 0:
        m, s = divmod(_TIME, 60)
        h, m = divmod(m, 60)
        m, s = divmod(s, 3600)
        print(f"\r{int(s)}") #.rjust(5))
        _TIME -= 1
        time.sleep(1)

        # add each print line (per second)
        if _TIME == 3:
            #sm.ktimer3()
            pass
        elif _TIME == 2:
            sm.ktimer2()
        elif _TIME == 1:
            sm.ktimer1()

    else:
        sm.chug_up()
        time.sleep(1)
#kart_timer()
