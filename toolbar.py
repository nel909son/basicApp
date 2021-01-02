  

bottom_and_top_nav =    '''

BoxLayout:
    orientation:'vertical'

    MDToolbar:
        title: 'Meditation App'
        md_bg_color: 1, 1, 1, 1
        specific_text_color: 0, 0, 0, 1

    MDBottomNavigation:
        panel_color: .2, .2, .2, 0

        MDBottomNavigationItem:
            name: 'screen1'
            text: 'timer'
            icon: 'alarm'

            MDSlider:
                id: slider
                min: 0
                max: 200
                value:50
                pos_hint: {"center_x": .5, "center_y": .5}
                
           
            MDLabel:
                id: timer
                text : str(int(slider.value))
                pos_hint: { "center_x": .6, "center_y":.6}
            MDLabel:
                id: countdown
                pos_hint: {"center_x" : .7, "center_y": .7}

            MDIconButton:
                icon: "alarm"
                pos_hint: { "center_x": .8, "center_y": .6}
                on_touch_up: app.set_timer()
                on_touch_down: app.start_timer()
                
                

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'round timer'
            icon: 'alarm-multiple'

            MDLabel:
                text: 'number of rounds'
                pos_hint: {"center_x": .5, "center_y": .9}

            MDSlider:
                id: num_rounds
                min: 0
                max: 100
                value:0
                pos_hint: { "center_x": .5, "center_y":.95}

            MDLabel:
                text: 'length of rounds'
                pos_hint: {"center_x": .6, "center_y": .8}

            MDSlider:
                id: round_len
                min: 0
                max: 100
                value: 0
                pos_hint: { "center_x": .6, "center_y":.85}
            MDLabel:
                text: 'length of breaks'
                pos_hint: {"center_x": .7, "center_y": .7}
            MDSlider:
                id: break_len
                min: 0
                max: 100
                value: 0
                pos_hint: { "center_x": .7, "center_y":.75}

            MDIconButton:
                icon: 'clock-start'
                pos_hint: {"center_x": .8, "center_y": .6}
                on_touch_down: app.round_timer()

      

            

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'history'
            icon: 'album'

            MDLabel:
                text: 'history'
                halign: 'center'

        
        MDBottomNavigationItem:
            name: 'screen 4'
            text: 'settings'
            icon: 'application-settings'

            MDLabel:
                text: 'settings(alarm sound)/api controls/themes'
                halign: 'center'
'''