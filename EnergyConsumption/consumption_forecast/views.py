from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import base64
import io
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from machine_learning.models import loaded_SVM_typical_to_high, loaded_SVM_typical_to_low, loaded_linear_reg_model

def home(request):
    """View function for the home page."""
    return render(request, 'consumption_forecast/home.html')

def help(request):
    """View function for the help page."""
    return render(request, 'consumption_forecast/help.html')

def upload_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        # Process the uploaded CSV file here
        try:
            # Read the CSV file using pandas
            df = pd.read_excel(csv_file)
            # Further processing with your DataFrame
            # For example, set the index
            df.set_index('DateTime', inplace=True)
            # Load the saved models from files and perform predictions
            # (Assuming loaded_SVM_typical_to_high, loaded_SVM_typical_to_low,
            # and loaded_linear_reg_model are defined and imported)
            predictions_model_one = loaded_SVM_typical_to_high.predict(df)
            predictions_model_two = loaded_SVM_typical_to_low.predict(df)
            predictions = loaded_linear_reg_model.predict(df)
            # Calculate SVM_Ready_df if necessary
            df['Global_active_power'] = predictions
            columns_order = ['Global_active_power'] + df.columns[df.columns != 'Global_active_power'].tolist()
            df = df.reindex(columns=columns_order)
            SVM_Ready_df = df
            SVM_Ready_df.index = pd.to_datetime(SVM_Ready_df.index)
            # Prepare statistical information
            true_count1 = sum(predictions_model_one)
            true_count2 = sum(predictions_model_two)
            typical_sum = SVM_Ready_df.shape[0] - true_count1 - true_count2
            mean = sum(predictions) / len(predictions)
            variance = sum([((x - mean) ** 2) for x in predictions]) / len(predictions)
            std_deviation = variance ** 0.5

            # Generate the plots
            plt.figure(figsize=(12, 6))
            plt.plot(df.index, df['Global_active_power'], label='Global Active Power')
            plt.xlabel('Date and Time')
            plt.ylabel('Global Active Power')
            plt.title('Global Active Power over Time')
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            plt.close()
            global_active_power_plot_data = base64.b64encode(buffer.getvalue()).decode()

            plt.figure(figsize=(8, 6))
            plt.hist(df['Global_active_power'], bins=50, color='skyblue', edgecolor='black')
            plt.xlabel('Global Active Power')
            plt.ylabel('Frequency')
            plt.title('Histogram of Global Active Power')
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            plt.close()
            histogram_global_active_power_plot_data = base64.b64encode(buffer.getvalue()).decode()

            plt.figure(figsize=(8, 6))
            plt.boxplot(df['Global_active_power'])
            plt.ylabel('Global Active Power')
            plt.title('Box Plot of Global Active Power')
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            plt.close()
            boxplot_global_active_power_plot_data = base64.b64encode(buffer.getvalue()).decode()

            plt.figure(figsize=(8, 6))
            plt.scatter(df['Global_active_power'], df['Voltage'], alpha=0.5)
            plt.xlabel('Global Active Power')
            plt.ylabel('Voltage')
            plt.title('Scatter Plot: Global Active Power vs. Voltage')
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            plt.close()
            scatterplot_global_active_power_voltage_plot_data = base64.b64encode(buffer.getvalue()).decode()

            corr_matrix = df.corr()
            plt.figure(figsize=(10, 8))
            sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
            plt.title('Correlation Heatmap')
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            plt.close()
            correlation_heatmap_plot_data = base64.b64encode(buffer.getvalue()).decode()

            plt.figure(figsize=(10, 8))
            sns.pairplot(df[['Global_active_power', 'Global_reactive_power', 'Voltage', 'Global_intensity']], diag_kind='kde')
            plt.title('Pair Plot of Selected Variables')
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            plt.close()
            pairplot_selected_variables_plot_data = base64.b64encode(buffer.getvalue()).decode()

            plt.figure(figsize=(10, 8))
            sns.violinplot(x=df.index.hour, y=df['Global_active_power'], inner="quartile")
            plt.xlabel('Hour of the Day')
            plt.ylabel('Global Active Power')
            plt.title('Violin Plot: Global Active Power by Hour')
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            plt.close()
            violinplot_global_active_power_hour_plot_data = base64.b64encode(buffer.getvalue()).decode()

            # Pass data to the template
            context = {
                'true_count1': true_count1,
                'true_count2': true_count2,
                'typical_sum': typical_sum,
                'mean': mean,
                'variance': variance,
                'std_deviation': std_deviation,
                'plot_data': {
                    'global_active_power': global_active_power_plot_data,
                    'histogram_global_active_power': histogram_global_active_power_plot_data,
                    'boxplot_global_active_power': boxplot_global_active_power_plot_data,
                    'scatterplot_global_active_power_voltage': scatterplot_global_active_power_voltage_plot_data,
                    'correlation_heatmap': correlation_heatmap_plot_data,
                    'pairplot_selected_variables': pairplot_selected_variables_plot_data,
                    'violinplot_global_active_power_hour': violinplot_global_active_power_hour_plot_data,
                }
            }
            # Render the template with the data
            return render(request, 'consumption_forecast/results.html', context)
        except Exception as e:
            # Handle any errors that occur during processing
            return render(request, 'consumption_forecast/error.html', {'error_message': str(e)})
    else:
        return render(request, 'consumption_forecast/error.html', {'error_message': 'No file uploaded'})

def error(request):
    error_message = "An error occurred. Please try again later."
    return render(request, 'consumption_forecast/error.html', {'error_message': error_message})

def results(request, context):
    # Simply render the template with the processed data passed from 'upload_csv'
    return render(request, 'consumption_forecast/results.html', context)