#!/usr/bin/python
import curses, random
import time

str1 = """
         __
 _(\    |@@|
(__/\__ \--/ __
   \___|----|  |   __
       \ }{ /\ )_ / _\\
       /\__/\ \__O (__
      (--/\--)    \__/
      _)(  )(_
     `---''---`
"""

str2 = """
       __
   _  |@@|
  / \ \--/ __
  ) O|----|  |   __
 / / \ }{ /\ )_ / _\\
 )/  /\__/\ \__O (__
|/  (--/\--)    \__/
/   _)(  )(_
   `---''---`
"""

anim = [str1, str2]

screen  = curses.initscr()
last = 0
while 1 :
  if last == 0:
    last = 1
  else :
    last = 0

  screen.addstr(0,0, anim[last])
  screen.refresh()
  time.sleep(0.5)

# curses.endwin()