import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title="RRManager")
with dpg.viewport_menu_bar():
        with dpg.menu(label="main"):
            dpg.add_menu_item(label="2")
        with dpg.menu(label="windows"):
            dpg.add_menu_item(label="XAMPP")
with dpg.window(label='window1',pos=(0,0)):
    
    dpg.add_text("Rogue Racing Manager V2")
    
with dpg.window(label='XAMPP',pos=(150,0)):
    dpg.add_text("Start XAMPP Server")
    dpg.add_button(label="Start")
    dpg.add_button(label="Stop")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
