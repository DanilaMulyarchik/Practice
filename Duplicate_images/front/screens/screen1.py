from setting_save.settings_save import settings_read


def screen1():

    LT1 = """
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
                                on_press: app.settings('folder')                    
                    BoxLayout:
                        AnchorLayout: 
                            anchor_x: 'right'
                            anchor_y: 'top'


                            MDIconButton:
                                icon: 'information-outline'
                                on_press: app.information()

            GridLayout:
                rows: 3
                height: 100
                row_force_default: True
                row_default_height: 80
                vertical_align: 'top'

                BoxLayout:
                    orientation: 'vertical'

                    AnchorLayout:
                        anchor_x: 'center'
                        anchor_y: 'center'

                        BoxLayout:
                            orientation: 'horizontal'
                            spacing: dp(10)
                            padding: dp(10)

                            MDLabel:
                                id: folder
                                text: '%folder%'
                                halign: "left"
                                size_hint_x: None
                                width: 510
                                text_size: self.width, None
                                
                            MDRaisedButton:
                                text: 'Выбрать папку'
                                on_press: app.folder('folder')
                BoxLayout:
                
                    AnchorLayout:
                        anchor_x: 'center'
                        anchor_y: 'center'            

                        BoxLayout:
                            orientation: 'horizontal'
                            spacing: dp(10)
                            padding: dp(10)

                            MDTextField:
                                sadding: dp(10)
                                id: percent
                                hint_text: 'Введите процентное соотношение(по умолчанию 100)'
                                size_hint_x: None  
                                width: 510
                                input_filter: "int"

                            MDRaisedButton:
                                text: 'Поиск дубликатов'
                                on_press: app.compare_folder_img('folder', 'percent')

                BoxLayout:
                
                    AnchorLayout:
                        anchor_x: 'center'
                        anchor_y: 'center'

                        BoxLayout:
                            orientation: 'horizontal'
                            spacing: dp(10)
                            padding: dp(10)
                            
                            MDTextField:
                                sadding: dp(10)
                                id: save
                                hint_text: '%save%'
                                size_hint_x: None  
                                width: 510

                            MDRaisedButton:
                                text: 'Сохранить'
                                on_press: app.save('save')
                
                            MDRaisedButton:
                                text: 'Показать'
                                on_press: app.third_screen()
"""



    LT1 = LT1.replace('%folder%', settings_read('const'))
    LT1 = LT1.replace('%save%', settings_read('save'))
    return LT1