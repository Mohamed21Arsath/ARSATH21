# ARSATH21
                         COVID-19 VACCINATION ANALYIS  

PROBLEM STATEMENT : 

This project aims to comprehensively analyze Covid-19 vaccine data, specifically concentrating on vaccine effectiveness, distribution patterns, and adverse reactions. The primary objective is to generate actionable insights to assist policymakers and healthcare entities in enhancing their vaccination deployment strategies.
 
CONTRIBUTERS:

DINESH BABU P K
MOHAMED ARSATH T
JEYAKMUAR N K
YASHWANTH  J A
PRITHIVIRAJ  S D

INTRODUCTION:

This project involves the analysis of COVID-19 vaccination data using Python and various data analysis libraries. The analysis is performed on two datasets: one containing information about vaccine manufacturers, and the other containing country-level vaccination data.
              
Data Sources
The project utilizes two primary data sources:
- [country_vaccinations_by_manufacturer.csv](data/country_vaccinations_by_manufacturer.csv): Data on vaccine manufacturers.
- [country_vaccinations.csv](data/country_vaccinations.csv): Country-level vaccination data.




Columns in `country_vaccinations.csv :

- `location`: The location or country where vaccinations are recorded.
- `date`: The date on which vaccination data was reported.
- `vaccine`: The type of vaccine administered.
- `total_vaccinations`: The total number of vaccinations administered on the specified date.

 Requirements

To run the analysis script, ensure that you have the following Python libraries installed:
- NumPy
- Pandas
- Seaborn
- Matplotlib
- Plotly
- Plotly Express

Running the Code in Google Colab

To run the code in Google Colab, follow these steps:

1. Open Google Colab in your web browser.
2. Click on "File" > "New Notebook" to create a new Colab notebook.
3. Copy and paste the code from `vaccine_data_analysis.py` into the Colab notebook.
4. Upload the dataset files `country_vaccinations_by_manufacturer.csv` and `country_vaccinations.csv` to your Google Drive.
5. Mount your Google Drive in the Colab notebook using the following code:

```python
from google.colab import drive
drive.mount('/content/drive')



Analysed: 
. Visualization of Data
![Alt text](image-1.png)
 
Top countries in vaccinations Utilization
![Alt text](image-2.png)

Fully Vaccinated Count
![Alt text](image-3.png)

Most commonly used vaccines in the World
![Alt text](image-4.png)

Daily vaccinations per million top countries
![Alt text](image-5.png)

Country wise daily vaccination per million
![Alt text](image-6.png)

