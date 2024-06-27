import json
import pandas as pd
from glob import glob
import os
from datetime import datetime

# # simdi = datetime.now()
# # yil = simdi.year
# # ay = simdi.month
# # gun = simdi.day


## JSON dosyalarının bulunduğu dizin
os.chdir("../json")
json_files = glob('*.json')

# combined_data = []

# # Her bir JSON dosyasını okuyup verileri birleştirilmiş veri listesine ekleyin
# for file in json_files:
#     with open(file, 'r', encoding='utf-8') as f:
#         data = json.load(f)
#         print(data)
#         df = pd.DataFrame(data["pckOrderDetails"])
#         excel_file = file+'combined_data.xlsx'
#         df.to_excel(excel_file, index=False)



import pandas as pd
import os

# Birleştirmek istediğiniz Excel dosyalarının bulunduğu dizin
directory = 'C:/Users/emre.karagoz/Desktop/Python/json'

# Dosya listesini alın
file_list = os.listdir(directory)

# Birleştirilmiş veri çerçevesi
merged_df = pd.DataFrame()

for file in file_list:
    if file.endswith('.xlsx'):
        file_path = os.path.join(directory, file)
        # Excel dosyasını okuyarak başlık satırını alın
        df = pd.read_excel(file_path, header=0)  # header=0, ilk satırı başlık olarak kabul eder

    #     # İlk Excel dosyasıysa, başlık satırını direk olarak birleştirilmiş DataFrame'e ekleyin
        if merged_df.empty:
            merged_df = df
    #     else:
    #         # Diğer Excel dosyalarını birleştirilmiş DataFrame'e sadece veri satırları olarak ekleyin
            merged_df = pd.concat([merged_df, df], ignore_index=True)
excel_file = "emre.xlsx"
merged_df.to_excel(excel_file, index=False)


