import dearpygui.dearpygui as dpg
import dynamodb_data as db

# Creating Context Window
dpg.create_context()

# Soya Window
with dpg.window(label="SOYA", width=400, height=810):
     # create a theme for the plot
    with dpg.theme(tag="plot1_theme"):
        with dpg.theme_component(dpg.mvBarSeries):
            dpg.add_theme_color(dpg.mvPlotCol_Fill, (17, 29, 94), category=dpg.mvThemeCat_Plots)

    # Creating Plot
    with dpg.plot(label="Soya Future Contract Price", height=-1, width=-1):
        # Creating Legend 
        dpg.add_plot_legend()

        # create x axis
        dpg.add_plot_axis(dpg.mvXAxis, label="Contract", no_gridlines=True, tag="x1_axis")
        dpg.set_axis_limits("x1_axis", 0, 12)
        dpg.set_axis_ticks(dpg.last_item(), (("C1", 1), ("C2", 3), ("C3", 5), ("C4", 7), ("C5", 9), ("C6", 11)))

        # create y axis
        dpg.add_plot_axis(dpg.mvYAxis, label="Price", tag="y1_axis")
        dpg.set_axis_limits("y1_axis", 8500, 10500)

        # add series to y axis
        dpg.add_bar_series([1, 3, 5, 7, 9, 11], db.SOYA_PRICES, label="SOYA Price", weight=1, parent="y1_axis", tag="soya_series")

        # bing theme to plot
        dpg.bind_item_theme("soya_series", "plot1_theme")

# Creating Context Window
dpg.create_context()

# SUNS Window
with dpg.window(label="SUNS", width=400, height=400):
     # create a theme for the plot
    with dpg.theme(tag="plot2_theme"):
        with dpg.theme_component(dpg.mvBarSeries):
            dpg.add_theme_color(dpg.mvPlotCol_Fill, (199, 0, 57), category=dpg.mvThemeCat_Plots)

    # Creating Plot
    with dpg.plot(label="SUNS Future Contract Price", height=-1, width=-1):
        # Creating Legend 
        dpg.add_plot_legend()

        # create x axis
        dpg.add_plot_axis(dpg.mvXAxis, label="Contract", no_gridlines=True, tag="x2_axis")
        dpg.set_axis_limits("x2_axis", 0, 12)
        dpg.set_axis_ticks(dpg.last_item(), (("C1", 1), ("C2", 3), ("C3", 5), ("C4", 7), ("C5", 9), ("C6", 11)))

        # create y axis
        dpg.add_plot_axis(dpg.mvYAxis, label="Price", tag="y2_axis")
        dpg.set_axis_limits("y2_axis", 8000, 12500)

        # add series to y axis
        dpg.add_bar_series([1, 3, 5, 7, 9, 11], db.SUNS_PRICES, label="SUNS Price", weight=1, parent="y2_axis", tag="suns_series")

        # bing theme to plot
        dpg.bind_item_theme("suns_series", "plot2_theme")

# WEAT Window
with dpg.window(label="WEAT", width=400, height=400):
     # create a theme for the plot
    with dpg.theme(tag="plot3_theme"):
        with dpg.theme_component(dpg.mvBarSeries):
            dpg.add_theme_color(dpg.mvPlotCol_Fill, (243, 113, 33), category=dpg.mvThemeCat_Plots)

    # Creating Plot
    with dpg.plot(label="WEAT Future Contract Price", height=-1, width=-1):
        # Creating Legend 
        dpg.add_plot_legend()

        # create x axis
        dpg.add_plot_axis(dpg.mvXAxis, label="Contract", no_gridlines=True, tag="x3_axis")
        dpg.set_axis_limits("x3_axis", 0, 12)
        dpg.set_axis_ticks(dpg.last_item(), (("C1", 1), ("C2", 3), ("C3", 5), ("C4", 7), ("C5", 9), ("C6", 11)))

        # create y axis
        dpg.add_plot_axis(dpg.mvYAxis, label="Price", tag="y3_axis")
        dpg.set_axis_limits("y3_axis", 6800, 7300)

        # add series to y axis
        dpg.add_bar_series([1, 3, 5, 7, 9, 11], db.WEAT_PRICES, label="WEAT Price", weight=1, parent="y3_axis", tag="weat_series")

        # bing theme to plot
        dpg.bind_item_theme("weat_series", "plot3_theme")

# WMAZ Window
with dpg.window(label="WMAZ", width=400, height=400):
     # create a theme for the plot
    with dpg.theme(tag="plot4_theme"):
        with dpg.theme_component(dpg.mvBarSeries):
            dpg.add_theme_color(dpg.mvPlotCol_Fill, (192, 226, 24), category=dpg.mvThemeCat_Plots)

    # Creating Plot
    with dpg.plot(label="WMAZ Future Contract Price", height=-1, width=-1):
        # Creating Legend 
        dpg.add_plot_legend()

        # create x axis
        dpg.add_plot_axis(dpg.mvXAxis, label="Contract", no_gridlines=True, tag="x4_axis")
        dpg.set_axis_limits("x4_axis", 0, 12)
        dpg.set_axis_ticks(dpg.last_item(), (("C1", 1), ("C2", 3), ("C3", 5), ("C4", 7), ("C5", 9), ("C6", 11)))

        # create y axis
        dpg.add_plot_axis(dpg.mvYAxis, label="Price", tag="y4_axis")
        dpg.set_axis_limits("y4_axis", 4000, 5200)

        # add series to y axis
        dpg.add_bar_series([1, 3, 5, 7, 9, 11], db.WMAZ_PRICES, label="WMAZ Price", weight=1, parent="y4_axis", tag="wmaz_series")

        # bing theme to plot
        dpg.bind_item_theme("wmaz_series", "plot4_theme")

# YMAZ Window
with dpg.window(label="YMAZ", width=400, height=400):
     # create a theme for the plot
    with dpg.theme(tag="plot5_theme"):
        with dpg.theme_component(dpg.mvBarSeries):
            dpg.add_theme_color(dpg.mvPlotCol_Fill, (142, 0, 199), category=dpg.mvThemeCat_Plots)

    # Creating Plot
    with dpg.plot(label="YMAZ Future Contract Price", height=-1, width=-1):
        # Creating Legend 
        dpg.add_plot_legend()

        # create x axis
        dpg.add_plot_axis(dpg.mvXAxis, label="Contract", no_gridlines=True, tag="x5_axis")
        dpg.set_axis_limits("x5_axis", 0, 12)
        dpg.set_axis_ticks(dpg.last_item(), (("C1", 1), ("C2", 3), ("C3", 5), ("C4", 7), ("C5", 9), ("C6", 11)))

        # create y axis
        dpg.add_plot_axis(dpg.mvYAxis, label="Price", tag="y5_axis")
        dpg.set_axis_limits("y5_axis", 4000, 5200)

        # add series to y axis
        dpg.add_bar_series([1, 3, 5, 7, 9, 11], db.YMAZ_PRICES, label="YMAZ Price", weight=1, parent="y5_axis", tag="ymaz_series")

        # bing theme to plot
        dpg.bind_item_theme("ymaz_series", "plot5_theme")

dpg.create_viewport(title='Custom Title', width=1220, height=820)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()