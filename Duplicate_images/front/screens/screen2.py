LT2 = """
    Screen:
        name: 'second'

        GridLayout:
            rows: 3
            row_force_default: True
            row_default_height: 160
            vertical_align: 'top'


            GridLayout:
                cols: 2

                GridLayout: 
                    cols: 3

                    BoxLayout:

                        AnchorLayout: 
                            anchor_x: 'left'
                            anchor_y: 'top'


                            MDIconButton:
                                icon: 'information-outline'
                                on_press: app.information()

                    BoxLayout:
                        AnchorLayout: 
                            anchor_x: 'left'
                            anchor_y: 'top'

                            MDIconButton:
                                icon: "cog-outline"
                                on_press: app.settings()                    
                    BoxLayout:
                        AnchorLayout: 
                            anchor_x: 'left'
                            anchor_y: 'top'

                            MDIconButton:
                                id: theme_button
                                icon: 'weather-sunny'
                                on_press: app.change_color()

                AnchorLayout:
                    anchor_x: 'right'
                    anchor_y: 'top'

                    MDIconButton:
                        icon: 'arrow-right'
                        on_press: app.first_screen()
# 2 row     |

            GridLayout:
                rows: 1

                GridLayout:
                    cols:2

                    BoxLayout:
                        orientation : 'vertical'

                        AnchorLayout:
                            anchor_x: 'center'
                            anchor_y: 'center'

                            FitImage:
                                id: img_screen_2_1
                                source: ""
                                size_hint_y: None
                                height: dp(200)

                    BoxLayout:
                        AnchorLayout:
                            anchor_x: 'center'
                            anchor_y: 'center'

                            FitImage:
                                id: img_screen_2_2
                                size_hint_y: None
                                source: ""
                                height: dp(200)
#row 3         
            GridLayout:
                cols:3

                BoxLayout:

                    AnchorLayout:
                        anchor_x: 'center'
                        anchor_y: 'center'

                        MDRaisedButton:
                            text: 'Image1'
                            on_press: app.image('img_screen_2_1')
                            
                BoxLayout:

                    AnchorLayout:
                        anchor_x: 'center'
                        anchor_y: 'center'

                        MDRaisedButton:
                            text: 'Work'
                            on_press: app.work('img_screen_2_1', 'img_screen_2_2')

                BoxLayout:

                    AnchorLayout:
                        anchor_x: 'center'
                        anchor_y: 'center'

                        MDRaisedButton:
                            text: 'Image2'
                            on_press: app.image('img_screen_2_2')

"""