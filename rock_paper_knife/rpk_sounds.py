'''
mini audio module for rock paper scissors
'''
# Audio
from pygame import mixer
# initialize the pygame mixer
mixer.init(44100)
# coin_Up
def coin_up():
    c.play()
    c.set_volume(0.70)
try:
    c = mixer.Sound("assets/audio/smb_coin.wav")
except:
    prompt = "Error: Sound file not found"
# startup sound
def presents_up():
    pr.play()
    pr.set_volume(0.70)
try:
    pr = mixer.Sound("assets/audio/presenting.wav")
except:
    prompt = "Error: Sound file not found"

# startup sound
def glitchy_up():
    g.play()
    g.set_volume(0.70)
try:
    g = mixer.Sound("assets/audio/uh_hello_fast.wav")
except:
    prompt = "Error: Sound file not found"

# ROCK sound
def rock_up():
    rock.play()
    rock.set_volume(0.60)
try:
    rock = mixer.Sound("assets/audio/rock.wav")
except:
    prompt = "Error: Sound file not found"
# PAPER sound
def paper_up():
    pap.play()
    pap.set_volume(0.50)
try:
    pap = mixer.Sound("assets/audio/paper.wav")
except:
    prompt = "Error: Sound file not found"
# KNIFE sound
def knife_up():
    kn.play()
    kn.set_volume(0.50)
try:
    kn = mixer.Sound("assets/audio/knife.wav")
except:
    prompt = "Error: Sound file not found"
# KNIFE sound
def chug_up():
    chug.play()
    chug.set_volume(0.30)
try:
    chug = mixer.Sound("assets/audio/chug_one.wav")
except:
    prompt = "Error: Sound file not found"

# nsmb power up sound
def power_up():
    p.play()
    p.set_volume(0.80)
try:
    p = mixer.Sound("assets/audio/nsmb_power-up.wav")
except:
    prompt = "Error: Sound file not found"

# KNIFE sound
def cpu_up():
    cpu.play()
    #cpu.set_volume(0.90)
try:
    cpu = mixer.Sound("assets/audio/computing.wav")
except:
    prompt = "Error: Sound file not found"
# nsmb power up sound
def shell_up():
    sh.play()
    sh.set_volume(0.90)
try:
    sh = mixer.Sound("assets/audio/smw_pipe.wav")
except:
    prompt = "Error: Sound file not found"

# nsmb power up sound
def player_up():
    pl.play()
    pl.set_volume(0.70)
try:
    pl = mixer.Sound("assets/audio/smw_pause.wav")
except:
    prompt = "Error: Sound file not found"
# nsmb power up sound
def bump_up():
    b.play()
    b.set_volume(0.70)
try:
    b = mixer.Sound("assets/audio/smb_bump.wav")
except:
    prompt = "Error: Sound file not found"

# nsmb power up sound
def ready_up():
    r.play()
    r.set_volume(0.70)
try:
    r = mixer.Sound("assets/audio/smw_princess_help.wav")
except:
    prompt = "Error: Sound file not found"

# nsmb power up sound
def battle_up():
    ba.play()
    ba.set_volume(0.40)
try:
    ba = mixer.Sound("assets/audio/battle.wav")
except:
    prompt = "Error: Sound file not found"

# nsmb power up sound
def countdown():
    co.play()
    co.set_volume(0.70)
try:
    co = mixer.Sound("assets/audio/kart_timer.wav")
except:
    prompt = "Error: Sound file not found"

# nsmb power up sound
def ktimer3():
    k3.play()
    k3.set_volume(0.70)
try:
    k3 = mixer.Sound("assets/audio/kart_timer3.wav")
except:
    prompt = "Error: Sound file not found"
# nsmb power up sound
def ktimer2():
    k2.play()
    k2.set_volume(0.70)
try:
    k2 = mixer.Sound("assets/audio/kart_timer2.wav")
except:
    prompt = "Error: Sound file not found"
# nsmb power up sound
def ktimer1():
    k1.play()
    k1.set_volume(0.70)
try:
    k1 = mixer.Sound("assets/audio/kart_timer1.wav")
except:
    prompt = "Error: Sound file not found"
# nsmb power up sound
def one_up():
    up.play()
    up.set_volume(0.70)
try:
    up = mixer.Sound("assets/audio/smw_1-up.wav")
except:
    prompt = "Error: Sound file not found"
# nsmb power up sound
def win_up():
    wi.play()
    wi.set_volume(0.70)
try:
    wi = mixer.Sound("assets/audio/sm64_bowser_message.wav")
except:
    prompt = "Error: Sound file not found"
# nsmb power up sound
def lose_up():
    lo.play()
    lo.set_volume(0.70)
try:
    lo = mixer.Sound("assets/audio/sm64_bowser_message.wav")
except:
    prompt = "Error: Sound file not found"

# nsmb power up sound
def thanks_up():
    th.play()
    th.set_volume(0.70)
try:
    th = mixer.Sound("assets/audio/sm64_mario_thank_you.wav")
except:
    prompt = "Error: Sound file not found"

# MK2 sounds
def insert_coin():
    insert.play()
    insert.set_volume(0.50)
try:
    insert = mixer.Sound("assets/audio/coin_insert.wav")
except:
    prompt = "Error: Sound file not found"
# MK2 sounds
def fight_up():
    f.play()
    f.set_volume(0.30)
try:
    f = mixer.Sound("assets/audio/mk_fight.wav")
except:
    prompt = "Error: Sound file not found"

def kom_dun():
    ko.play()
    ko.set_volume(0.50)
try:
    ko = mixer.Sound("assets/audio/kombat_dun.wav")
except:
    prompt = "Error: Sound file not found"

# MK2 sounds
def error_up():
    er.play()
    er.set_volume(0.50)
try:
    er = mixer.Sound("assets/audio/mk2_error.wav")
except:
    prompt = "Error: Sound file not found"

# MK2 sounds
def gong_up():
    go.play()
    go.set_volume(0.50)
try:
    go = mixer.Sound("assets/audio/mk2_gong.wav")
except:
    prompt = "Error: Sound file not found"

def life_up():
    li.play()
    li.set_volume(0.70)
try:
    li = mixer.Sound("assets/audio/SF_life.wav")
except:
    prompt = "Error: Sound file not found"

def peak_up():
    pe.play()
    pe.set_volume(0.70)
try:
    pe = mixer.Sound("assets/audio/SF_peak.wav")
except:
    prompt = "Error: Sound file not found"

def punch_up():
    pu.play()
    pu.set_volume(0.70)
try:
    pu = mixer.Sound("assets/audio/mk2_punch1.wav")
except:
    prompt = "Error: Sound file not found"

def punch2_up():
    p2.play()
    p2.set_volume(0.70)
try:
    p2 = mixer.Sound("assets/audio/mk2_punch2.wav")
except:
    prompt = "Error: Sound file not found"
