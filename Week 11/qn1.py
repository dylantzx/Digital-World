
from kivy.app import App
from kivy.uix.label import Label


class AlternateApp(App):
    text_state = 0
    def build(self):
                #build widgets
        #return the root widget
        lbl_toggle = Label(text = "Programming is Fun. ", font_size = "24")
        #1st way using bind(), where on_touch_down is the event name and self.alternate is the method being bound
        lbl_toggle.bind(on_touch_down = self.alternate) #not a function call
        return lbl_toggle
  
    def alternate(self, instance, touch):
        #instance is the widget that triggers the event
        #print(instance.text)# This is to access the text
        if self.text_state == 0:
            instance.text = "It is Fun to Program" #This is to change the text
            #self.text_state = 1
        
        else:
            instance.text = "Programming is Fun" #This is to change the text
            #self.text_state = 0
            
        
        self.text_state = 1 - self.text_state #To toggle between the states.
        #For eg, at the start, text_state = 0 thus self.text state = 1 and when text.state == 1,
        #self.text_state == 0
     

myapp = AlternateApp()
myapp.run()
