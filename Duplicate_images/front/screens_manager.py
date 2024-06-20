LT = """
ScreenManager:
    Screen:
        name: "first"
        
        GridLayout:
            rows: 2
            row_force_default: True
            row_default_height: 160
            vertical_align: 'top'
            
            
            GridLayout:
                cols: 2
                
                AnchorLayout:
                    anchor_x: 'left'
                    anchor_y: 'top'
                
                    MDIconButton:
                        icon: 'arrow-left'
                        on_press: app.second_screen()
                        
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
                                on_press: app.settings()                    
                    BoxLayout:
                        AnchorLayout: 
                            anchor_x: 'right'
                            anchor_y: 'top'

                            
                            MDIconButton:
                                icon: 'information-outline'
                                on_press: app.information()
                
            BoxLayout:
                height: 100
                GridLayout
                    cols: 2
                    
                    BoxLayout:
                        orientation: 'vertical'
                        
                        AnchorLayout:
                            anchor_x: 'center'
                            anchor_y: 'center'
    
                            BoxLayout:
                                orientation: 'horizontal'
                                spacing: dp(10)
                                padding: dp(10)
                                    
                                MDTextField:
                                    sadding: dp(10)
                                    id: folder
                                    hint_text: 'Choose folder'
                                    size_hint_x: None  
                                    width: dp(200)
                                                            
                                MDRaisedButton:
                                    text: 'Folder'
                        
                        AnchorLayout:
                            anchor_x: 'center'
                            anchor_y: 'center'            
                              
                            BoxLayout:
                                orientation: 'horizontal'
                                spacing: dp(10)
                                padding: dp(10)
                                    
                                MDTextField:
                                    sadding: dp(10)
                                    id: folder
                                    hint_text: 'Write %'
                                    size_hint_x: None  
                                    width: dp(200)
                                                            
                                MDRaisedButton:
                                    text: 'Work'
                        
                        AnchorLayout:
                            anchor_x: 'center'
                            anchor_y: 'center'
                            
                            BoxLayout:
                                orientation: 'horizontal'
                                spacing: dp(10)
                                padding: dp(10)
                                    
                                MDTextField:
                                    sadding: dp(10)
                                    id: folder
                                    hint_text: 'Choose folder'
                                    size_hint_x: None  
                                    width: dp(200)
                                                            
                                MDRaisedButton:
                                    text: 'Save'
                    
                    AnchorLayout:
                        FitImage:
                            id: img
                            source: ""
                            size_hint_y: None
                            height: 300
            
    Screen:
        name: 'second'
        
        MDIconButton:
            icon: 'arrow-right'
            on_press: app.first_screen()
        
    
    
"""
