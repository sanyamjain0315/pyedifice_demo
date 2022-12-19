import edifice as ed
import time
from edifice import Window,View,Component,Label,Button
meters=10.0
t=0
class demo(Component):
    def __init__(self):
        super().__init__()
        self.meters=0.0
        self.seconds=0.0
        self.timer=ed.Timer(lambda: self.changes())
    def changes(self):
        if(self.meters>=100):    
            self.timer.stop()
            return
        self.set_state(meters=self.meters+2,seconds=self.seconds+0.1)

    def render(self):
        return Window(title="Nirmaan GUI",icon='nirmaanhyperloop_logo.jpg')(
            View(layout='row',style={"margin":10,"width":900,"height":200})(
                View(layout='row',style={"height":20,"width":500,"border-radius":10,"background":"#555555","align":"left"})(#Progress slider
                    View(layout='row',style={"height":20,"width":(self.meters*5),"border-radius":10,"background":"#1ec6e1","align":"left"}),
                ),
                View(layout='column',style={"width":100,"height":100,"background":"#555555","align":"center","border-radius":10})(#distance travelled
                    Label(text="Distance travelled",style={"color":"white","align":"center","font-size":15}),
                    Label(text=f"{round(self.meters,2)} m",style={"color":"white","align":"center","font":"bold","font-size":15}),
                ),
                View(layout='column',style={"width":100,"height":100,"background":"#555555","align":"center","border-radius":10})(#time passed
                    Label(text="Time Elapsed",style={"color":"white","align":"center","font-size":15}),
                    Label(text=f"{round(self.seconds,2)} s",style={"color":"white","align":"center","font":"bold","font-size":15}),
                ),
                Button(title='Start',style={"width":100,"height":100,"background":"#555555","border-radius":50,"color":"white","font-size":15},on_click=lambda e: self.timer.start(100))
            )
        )

if __name__=='__main__':
    ed.App(demo()).start()