import dearpygui.dearpygui as dpg
import dynamodb_data as db

# Creating Context Window
dpg.create_context()

# Soya Window
with dpg.window(label="SOYA", width=400, height=400):
     # create a theme for the plot
    with dpg.theme(tag="plot_theme"):
        with dpg.theme_component(dpg.mvBarSeries):
            dpg.add_theme_color(dpg.mvPlotCol_Fill, (150, 255, 0), category=dpg.mvThemeCat_Plots)

    # Creating Plot
    with dpg.plot(label="Soya Future Contract Price", height=-1, width=-1):
        # Creating Legend 
        dpg.add_plot_legend()

        # create x axis
        dpg.add_plot_axis(dpg.mvXAxis, label="Contract", no_gridlines=True, tag="x_axis")
        dpg.set_axis_limits("x_axis", 0, 12)
        dpg.set_axis_ticks(dpg.last_item(), (("C1", 1), ("C2", 3), ("C3", 5), ("C4", 7), ("C5", 9), ("C6", 11)))

        # create y axis
        dpg.add_plot_axis(dpg.mvYAxis, label="Price", tag="y_axis")
        dpg.set_axis_limits("y_axis", 0, 12000)

        # add series to y axis
        dpg.add_bar_series([1, 3, 5, 7, 9, 11], db.SOYA_PRICES, label="Contract Price", weight=1, parent="y_axis", tag="soya_series")

        # bing theme to plot
        dpg.bind_item_theme("soya_series", "plot_theme")






dpg.create_viewport(title='Custom Title', width=820, height=820)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()