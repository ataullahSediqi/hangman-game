import random
import kivy
                                                                      
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.screenmanager import RiseInTransition 
from kivy.uix.togglebutton import ToggleButton



#2019 / 9 / 17
kivy.require('1.11.1')
                                                   
                                                   
                                                    
def list_to_str(List):
    new = ""
    for x in List:
        new += x + ''
    return new
words_file = open('words1.txt' ,'r+')
all_words = words_file.read()
words = all_words.split()
len_1 = []
len_2 = []
len_3 = []
len_4 = []
len_5 = []
len_6 = []
len_7 = []
len_8 = []
len_9 = []
len_10 = []

for word in words:
    if len(word) == 1:
        len_1.append(word)
    elif len(word) == 2:
        len_2.append(word)
    elif len(word) ==3:
        len_3.append(word)
    elif len(word) ==4:
        len_4.append(word)
    elif len(word) ==5:
        len_5.append(word)
    elif len(word) ==6:
        len_6.append(word)
    elif len(word) ==7:
        len_7.append(word)
    elif len(word) ==8:
        len_8.append(word)
    elif len(word) ==9:
        len_9.append(word)
    elif len(word) ==10:
        len_10.append(word)



info_about = """

     Application by Ataullah Sediqi


"""



class Replay_Screen(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 3 
        self.cols = 3 
        self.no_1 = Label()
        self.no_2 = Label()
        self.no_3 = Label()
        self.no_4 = Label()
        self.no_5 = Label()
        self.no_6 = Label()
        self.no_7 = Label()
        self.no_8 = Label()
        self.btn_replay = Button(text=(" you lost the game  \n       replay ").upper(), on_press=replay_event_handler)
        self.add_widget(self.no_1)
        self.add_widget(self.no_2)
        self.add_widget(self.no_3)
        self.add_widget(self.no_4)
        self.add_widget(self.btn_replay)
        self.add_widget(self.no_5)
        self.add_widget(self.no_6)
        self.add_widget(self.no_7)
        self.add_widget(self.no_8)






class MyLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 6
        self.cols = 3
        self.nothing2 = Label(text='')
        self.add_widget(self.nothing2)
        self.nothing3 = Label(text="")
        self.add_widget(self.nothing3)
        self.nothing4 = Label(text="")
        self.add_widget(self.nothing4)
        self.nothing5 = Label(text="")
        self.nothing6 = Label(text="")
        self.nothing7 = Label(text="")
        self.nothing8 = Label(text="")
        self.nothing9 = Label(text="")
        self.nothing12 = Label(text="")
        self.nothing13 = Label(text="")
        self.nothing14 = Label(text="")
        self.nothing15= Label(text="")
        self.nothing16 = Label(text="")
        self.nothing17 = Label(text="")
        self.gm_level = Button(text="LEVEL" , font_size=24 , on_press =go_to_Level)
        self.nothing19 = Label(text="")
        self.nothing20 = Label(text="")
        self.nothing21 = Label(text="")
        self.nothing10 = Label(text="")
        self.nothing11 = Label(text="")
        self.play_btn = Button(text="PLAY" , font_size=26, on_press=call_able)
        self.about = Button(text=" About me" , font_size = 26 , on_press=change_info)
        self.add_widget(self.nothing6)
        self.add_widget(self.play_btn)
        self.add_widget(self.nothing8)
        self.add_widget(self.nothing7)
        self.add_widget(self.gm_level)
        self.nothing = Label(text="")
        self.add_widget(self.nothing)
        self.add_widget(self.nothing9)
        self.add_widget(self.about)
        self.add_widget(self.nothing11)
        self.add_widget(self.nothing12)
        self.add_widget(self.nothing13)
        self.add_widget(self.nothing14)
        self.add_widget(self.nothing15)
        self.add_widget(self.nothing16)
        self.add_widget(self.nothing17)





        

class About_me(BoxLayout):
    def __init__(self , **kwargs):
        super().__init__(**kwargs)
        self.full_info = Label(text=info_about , font_size = 24)
        self.add_widget(self.full_info)

class Level(BoxLayout):
    def __init__(self , **kwargs):
        super().__init__(**kwargs)
        self.root1 = BoxLayout()
        self.root1.orientation= 'vertical'
        self.add_widget(self.root1)
        self.btn1 = ToggleButton(group="level_btn",text="Level 1".upper() , size_hint_x =.7 ,on_press=on_press_len_1)
        self.btn2 = ToggleButton(group="level_btn",text="Level 2".upper(), size_hint_x =.7 ,on_press= on_press_len_2)
        self.btn3 = ToggleButton(group="level_btn",text="Level 3".upper() , size_hint_x =.7 ,on_press= on_press_len_3)
        self.btn4 = ToggleButton(group="level_btn",text="Level 4".upper(), size_hint_x =.7 ,on_press= on_press_len_4)
        self.btn5 = ToggleButton(group="level_btn",text="Level 5".upper(), size_hint_x =.7 ,on_press= on_press_len_5)        
        self.btn6 = ToggleButton(group="level_btn",text="Level 6".upper(), size_hint_x =.7 ,on_press= on_press_len_6)        
        self.btn7 = ToggleButton(group="level_btn",text="Level 7".upper(), size_hint_x =.7 ,on_press= on_press_len_7)        
        self.btn8 = ToggleButton(group="level_btn",text="Level 8".upper(), size_hint_x =.7 ,on_press= on_press_len_8)        
        self.btn9 = ToggleButton(group="level_btn",text="Level 9".upper(), size_hint_x =.7 ,on_press= on_press_len_9)        
        self.btn10 = ToggleButton(group="level_btn",text="Level 10".upper() , size_hint_x =.7 ,on_press= on_press_len_10)
        
        self.root1.add_widget(self.btn1)
        self.root1.add_widget(self.btn2)
        self.root1.add_widget(self.btn3)
        self.root1.add_widget(self.btn4)
        self.root1.add_widget(self.btn5)
        self.root1.add_widget(self.btn6)
        self.root1.add_widget(self.btn7)
        self.root1.add_widget(self.btn8)
        self.root1.add_widget(self.btn9)
        self.root1.add_widget(self.btn10)
        self.root2 = BoxLayout()
        self.root2.orientation = 'vertical'
        self.add_widget(self.root2)
        self.not1 = Label(text="")
        self.not2 = Label(text="")
        self.back_btn = Button(text="back".upper() , size_hint_x=.5 , on_press = go_to_menu ) 
        self.root2.add_widget(self.not2)
        self.root2.add_widget(self.back_btn)  
        self.root2.add_widget(self.not1)  
           


   

   


class Mymain(BoxLayout): 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.word = random.choice(len_4)
        self.turns = 5
        self.guesses = []
        self.true_gusess= []
        self.rong_gusess = []
        self.word_index = list(self.word)
        self.litter_guessed = ["_ " for i in self.word]
        self.main_area = BoxLayout()
        self.add_widget(self.main_area)
        self.guess = BoxLayout(size_hint = [1,.31])
        self.main_area.add_widget(self.guess)
        self.labofg = Label(text="_ "*len(self.word) , font_size=23 )
        self.guess.add_widget(self.labofg)
        self.scnd_sec = BoxLayout()
        self.main_area.add_widget(self.scnd_sec)
        self.main_area.orientation = 'vertical'
        self.img_box = BoxLayout()
        self.img = Image(source='hangman-pics/1.png')
        self.scnd_sec.add_widget(self.img_box)
        self.img_box.add_widget(self.img)
        self.rhi = BoxLayout()
        self.scnd_sec.add_widget(self.rhi)
        self.rhi.orientation = 'vertical'
        self.text_input = TextInput(foreground_color = [2.5,2.5,2.5,1], multiline= False , font_size=40, background_color=[0.20,0.20,0.20,1 ])
        self.rhi.add_widget(self.text_input)
        self.btn_go = Button(text="GO!" ,font_size = 25 , on_press=self.main)
        self.rhi.add_widget(self.btn_go)
    def main(self , event):
        user_guess = self.text_input.text
        if user_guess in list(self.word):
            if user_guess not in self.guesses:
                self.guesses.append(user_guess)
            if user_guess not in self.true_gusess:
                self.true_gusess.append(user_guess)
            for i, l in enumerate(self.word_index):
                if l == user_guess:   
                    self.litter_guessed[i] = l
               
        else:
            self.rong_gusess.append(user_guess)
        self.text_input.text=''
        if len(self.rong_gusess) == 1:
            self.img.source = 'hangman-pics/2.png'
        elif len(self.rong_gusess) == 2:
            
            self.img.source = 'hangman-pics/3.png'
        elif len(self.rong_gusess) == 3:
            self.img.source='hangman-pics/4.png'
        elif len(self.rong_gusess) == 4:
            self.img.source='hangman-pics/5.png'
            My_ScreenManager.current = 'replay screen'
                                                
        else:
            self.guesses.append(user_guess)
                                                                                             
        litter_join = "".join(self.litter_guessed)
        
        self.labofg.text= litter_join

        if len(self.rong_gusess) == 4:
            self.labofg.text = 'you lose'

        if list_to_str(self.litter_guessed) == self.word:
            self.labofg.text = f"""You won the game,the word was '{litter_join}'"""
            My_ScreenManager.current = 'Won'

    def restart(self):
        self.true_gusess= []
        self.guesses = []
        self.rong_gusess = []
        self.img.source= 'hangman-pics/1.png'
        self.litter_guessed = ["_ " for i in self.word]
        self.word_index = list(self.word)
        self.labofg.text="_ "*len(self.word)
    

def on_press_len_1(event):
    obj_Hangman.word = random.choice(len_1)
    obj_Hangman.restart()

def on_press_len_2(event):
    obj_Hangman.word = random.choice(len_2)
    obj_Hangman.restart()


def on_press_len_3(event):
    obj_Hangman.word = random.choice(len_3)
    obj_Hangman.restart()

def on_press_len_4(event):
    obj_Hangman.word = random.choice(len_4)
    obj_Hangman.restart()

def on_press_len_5(event):
    obj_Hangman.word = random.choice(len_5)
    obj_Hangman.restart()

def on_press_len_6(event):
    obj_Hangman.word = random.choice(len_6)
    obj_Hangman.restart()

def on_press_len_7(event):
    obj_Hangman.word = random.choice(len_7)
    obj_Hangman.restart()

def on_press_len_8(event):
    obj_Hangman.word = random.choice(len_8)
    obj_Hangman.restart()

def on_press_len_9(event):
    obj_Hangman.word = random.choice(len_9)
    obj_Hangman.restart()

def on_press_len_10(event):
    obj_Hangman.word = random.choice(len_10)
    obj_Hangman.restart()



def call_able(event):    
    My_ScreenManager.current = 'hangman'
    



def replay_event_handler(event):
    obj_Hangman.restart()
    My_ScreenManager.current='menu'
    

def go_to_Level(event):
    My_ScreenManager.current = "level"


def go_to_menu(event):
    My_ScreenManager.current = "menu"



s1 = Screen(name="hangman")
s2 = Screen(name="menu")
s3 = Screen(name="developer")
s4 = Screen(name="level")
s5 = Screen(name="Won")
s4.add_widget(Level())
def change_info(event):
    My_ScreenManager.current = "developer" 
About_me_obj = About_me()
s3.add_widget(About_me_obj)


screen_replay = Screen(name= 'replay screen' )                                                                                                                                                                                                                  
obj_replay = Replay_Screen()
obj_level = Level()
obj_Mylayout = MyLayout()
obj_Hangman = Mymain()


class Won(GridLayout):
    def __init__(self , **kwargs):
        super().__init__()
        self.cols = 3
        self.rows = 3
        self.root = BoxLayout()
        self.add_widget(self.root)
        self.lbl1 = Label()
        self.lbl3 = Label()
        self.lbl4 = Label()
        self.lbl5 = Label()
        self.lbl6 = Label()
        self.lbl7 = Label()
        self.lbl8 = Label()
        self.add_widget(self.lbl1)
        self.button = Button(text="you won the game  \n      replay".upper() , on_press=replay_event_handler )
        self.lbl2 = Label()
        self.add_widget(self.lbl2)
        self.add_widget(self.lbl3)
        self.add_widget(self.button)
        self.add_widget(self.lbl4)
        self.add_widget(self.lbl5)
        self.add_widget(self.lbl6)
        self.add_widget(self.lbl7)


obj_won = Won()
screen_replay.add_widget(obj_replay)
s2.add_widget(obj_Mylayout)
s1.add_widget(obj_Hangman)
s5.add_widget(obj_won)
My_ScreenManager = ScreenManager(transition=RiseInTransition() )
My_ScreenManager.add_widget(screen_replay)
My_ScreenManager.add_widget(s3)
My_ScreenManager.add_widget(s4)
My_ScreenManager.add_widget(s2)
My_ScreenManager.add_widget(s1)
My_ScreenManager.add_widget(s5)
My_ScreenManager.current = 'menu'

class Menu(App):
    def build(self):
        return My_ScreenManager
if __name__=="__main__":
    Menu().run()            
