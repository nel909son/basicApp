from kivymd.app import MDApp
from kivy.lang import Builder
from toolbar import bottom_and_top_nav
import kivy
from kivy.uix.slider import Slider
from kivy.clock import Clock
from kivy.animation import Animation 

class Timer(object):
    #slider = Slider(min=-100, max=100, value=25)
    #start_value = slider.value
    pass
    

class Meditation(MDApp):
    global timer_start_val

    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        return Builder.load_string( bottom_and_top_nav )
    
    def set_timer(self):
      
       timer_start_val = int(self.root.ids.slider.value)
       return timer_start_val 
    
    def update_timer(self,*args):
        #update the timer time length
        print("time done")
       
    
    def start_timer(self):
        timer_start_val = int(self.root.ids.slider.value)
        Clock.schedule_once( self.stop_timer, timer_start_val)
        #self.start_countdown()
        
        #timer_set = int(self.root.ids.slider.value)
        #self.root.ids.timer.text = f"timer set for {timer_set} secs"

    def start_countdown(self):
        Animation.cancel_all(self)
        self.anim = Animation(timer_start_val = 0 , furation = self.timer_start_val )

    def stop_timer(self, *args):
        #to manually stop timer or after time runs out
        print("times up")
   
    def round_timer(self):
        num_rounds = int(self.root.ids.num_rounds.value)
        
        
        
        
      
        while num_rounds > 0:
            num_rounds -= 1
            self.start_round_timer()

    def start_round_timer(self):
        round_len = int(self.root.ids.round_len.value)
        Clock.schedule_once(self.start_round_break, round_len)

        print("start")

    def start_round_break(self):
        break_len = int(self.root.ids.break_len.value)
     
        print("break")
        Clock.schedule_once(self.stop_round_timer, break_len)

    def stop_round_timer(self):
        print("stop")

        

  

Meditation().run()