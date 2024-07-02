LT3 = '''
    Screen:
        name: "third"
    
        GridLayout:
            rows: 2
            vertical_align: 'top'

    
            GridLayout:
                cols: 2
                height: 0.1 
    
                AnchorLayout:
                    anchor_x: 'left'
                    anchor_y: 'top'
    
                    MDIconButton:
                        icon: 'arrow-left'
                        on_press: app.first_screen()
    
                GridLayout: 
                    cols: 3
    
                    BoxLayout:
    
                        AnchorLayout: 
                            anchor_x: 'right'
                            anchor_y: 'top'
    
                            MDIconButton:
                                id: theme_button
                                icon: 'weather-sunny'
                                on_press: app.change_color()
    
                    BoxLayout:
                        AnchorLayout: 
                            anchor_x: 'right'
                            anchor_y: 'top'
    
                            MDIconButton:
                                icon: "cog-outline"
                                on_press: app.settings('front')               
                    BoxLayout:
                        AnchorLayout: 
                            anchor_x: 'right'
                            anchor_y: 'top'
    
    
                            MDIconButton:
                                icon: 'information-outline'
                                on_press: app.information()
    
            BoxLayout:
                orientation: 'vertical'
                height_hint: 0.9
    
                ScrollView:
                    GridLayout:
                        id: grid
                        cols: 3
                        spacing: dp(10)
                        size_hint_y: None
                        height: self.minimum_height
'''
