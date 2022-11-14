import dearpygui.dearpygui as dpg
import boto3 
import json
import pandas

# Load Data Into DynamoDB

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('futures')

# Get Instrument ID from DynamoDB
SOYA = table.get_item(
    Key={
         "instrument_ID": "SOYA"
    }
)

# Convert Json Data from SOYA to a Pandas DataFrame


# store the for loop in a list 
price_list = []
for i in range(0, 7):
    price_list.append(SOYA['Item']['price' + str(i+1)])

# Convert Strings in Price List into doubles
price_list = [float(i) for i in price_list]
print(price_list)

# # Creating Context Window
# dpg.create_context()

# # Soya Window
# with dpg.window(label="SOYA", width=400, height=400):
#      # create a theme for the plot
#     with dpg.theme(tag="plot_theme"):
#         with dpg.theme_component(dpg.mvBarSeries):
#             dpg.add_theme_color(dpg.mvPlotCol_Fill, (150, 255, 0), category=dpg.mvThemeCat_Plots)


#     # Creating Plot
#     with dpg.plot(label="Soya Future Contract Price", height=-1, width=-1):
#         # Creating Legend 
#         dpg.add_plot_legend()

#         # create x axis
#         dpg.add_plot_axis(dpg.mvXAxis, label="Contract", no_gridlines=True, tag="x_axis")
#         dpg.set_axis_limits("x_axis", 0, 12)
#         dpg.set_axis_ticks(dpg.last_item(), (("C1", 1), ("C2", 3), ("C3", 5), ("C4", 7), ("C5", 9), ("C6", 11)))

#         # create y axis
#         dpg.add_plot_axis(dpg.mvYAxis, label="Price", tag="y_axis")
#         dpg.set_axis_limits("y_axis", 0, 110)

#         # add series to y axis
#         dpg.add_bar_series([1, 3, 5, 7, 9, 11], [100, 75, 90, 67, 70, 80], label="Contract Price", weight=1, parent="y_axis", tag="soya_series")

#         # bing theme to plot
#         dpg.bind_item_theme("soya_series", "plot_theme")






# dpg.create_viewport(title='Custom Title', width=820, height=820)
# dpg.setup_dearpygui()
# dpg.show_viewport()
# dpg.start_dearpygui()
# dpg.destroy_context()