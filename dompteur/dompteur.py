import dearpygui.dearpygui as dpg
import dearpygui.demo as demo

dpg.create_context()
dpg.create_viewport(title="Dompteur", width=600, height=600)

with dpg.window(tag="Dompteur Config"):
    dpg.add_text("Test me")
    dpg.add_button(label="Build")
    dpg.add_input_text(label='conf.py')
    dpg.add_slider_float(label="slide", default_value=0.4, max_value=50)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Dompteur Config", True)
dpg.start_dearpygui()
dpg.destroy_context()