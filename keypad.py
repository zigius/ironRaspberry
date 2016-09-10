import RPi.GPIO as GPIO
import time
import play2
def operation_expired(oldtime, started):
  expired = False
  if (time.time() - oldtime >= 3 and started):
    expired  = True
  return expired

def get_pin():

  GPIO.setmode(GPIO.BOARD)

  ESCAPE_CHAR = '#'
  MATRIX = [ ['1','2','3','A'],
    ['4','5','6','B'],
    ['7','8','9','C'],
    ['*',0,'#','D'] ]


  ROW = [7,11,13,15]
  COL = [12,16,18,22]

  for j in range(4):
    GPIO.setup(COL[j], GPIO.OUT)
    GPIO.output(COL[j], 1)

  for i in range(4):
    GPIO.setup(ROW[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

  pin_buf = []
  run_time = time.time()
  started = False
  try:
    while(True):
      for j in range(4):
        GPIO.output(COL[j],0)
        for i in range(4):
          if GPIO.input(ROW[i]) == 0:
            if MATRIX[i][j] == ESCAPE_CHAR:
                return ''.join(pin_buf)

            if operation_expired(run_time, started):
              print "operation expired. input registered as new string"
              pin_buf = []

            run_time = time.time()
            pin_buf.append(MATRIX[i][j])
            print 'pin_buf'
            print pin_buf

            started = True
            time.sleep(0.2)
            while(GPIO.input(ROW[i]) == 0):
              pass
        GPIO.output(COL[j],1)
  except Exception as ex:
    print ex
    GPIO.cleanup()

if __name__ == "__main__":
  try:
    while(True):
      user_id = get_pin()
      if user_id == '':
        continue
      print type(user_id)
      print user_id
      user_id_int = int(user_id)
      print type(user_id_int)
      play2.play_track(user_id_int)
  except Exception as ex:
    print ex

