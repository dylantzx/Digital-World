from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button 


class MyLabel(Label): #inherits from label

    def __init__(self, **kwargs):
        #This is like Foo.talk(f)
        #f will become self, and thus self is the object instance
        Label.__init__(self, **kwargs)
        #Size is the event, self.setter() is the callback
        self.bind(size=self.setter('text_size')) #text_size is the invisible rectangular text box   
        self.padding = (20, 20) #horizontal and vertical space
        self.font_size=24
        self.halign='left'
        self.valign='middle'

class MyInput(TextInput): #MyInput is a child of TextInput

    def __init__(self, **kwargs):
        #python automatically inserts self into the argument
        #This is like f.talk(), where f will be inserted automatically
        super().__init__(**kwargs) #super gives parent class of input
        self.font_size = 24
        self.multiline = False #disable writing multiple lines
        
class Investment(App):
    #main class contains build method and contains the App inheritance
    #No __init__ because im not modifying the property of App 
    def build(self):
        layout = GridLayout(cols=2)
        #horizontal alignment -> halign
        #Vertical alignment -> valign
        l1 = MyLabel(text="Investment Amount")
        layout.add_widget(l1)
        #Make it as an attribute of your app by adding the self
        self.txt_investment = MyInput(text = "")
        layout.add_widget(self.txt_investment)
        
        l2 = MyLabel(text="Years") #text is the property
        layout.add_widget(l2)
        
        self.txt_years = MyInput(text = "")
        layout.add_widget(self.txt_years)
        
        l3 = MyLabel(text="Annual Interest Rate")
        layout.add_widget(l3)
        
        self.txt_air = TextInput(text = "")
        layout.add_widget(self.txt_air)
            
        l4 = MyLabel(text="Future Value")
        layout.add_widget(l4)
        
        self.l5 = MyLabel(text =" 0.0")
        layout.add_widget(self.l5)
        
        #Label has no on_press event and needs on_touch_down which requires additional argument touch
        #on_press event only has 1 argument needed called instance
        btn = Button(text="Calculate", on_press=self.calculate, font_size=24)
        layout.add_widget(btn)
        
        return layout #Layout is returned, meaning that it is the root widget which is the widget that contains other widget

    def calculate(self, instance): #instance is the button pressed
        
        inv_amt = float(self.txt_investment.text)
        #print(inv_amt, type(inv_amt)) #Note that it is a string, so need to float it
        years = float(self.txt_years.text)
        mth_int_rate = float(self.txt_air.text)/1200 #divide by 100 because is a percentage
        future_val = inv_amt * (1+mth_int_rate)**(years*12)
        self.l5.text = "{:.2f}".format(future_val)

Investment().run()
