import pandas as pd

sheet = pd.read_csv("AIS_2024_09_10.csv")
sheet["BaseDateTime"] = pd.to_datetime(sheet["BaseDateTime"])

sheet_sorted = sheet.sort_values(by=["BaseDateTime"])
sheet_result = sheet_sorted.groupby(["MMSI", sheet_sorted["BaseDateTime"].dt.floor("h")], as_index=False).first()
#sheet_result.info()
#sheet_result.head()

sheet_for_map = sheet_result.drop(['SOG', 'COG', 'Heading', 'VesselName', 'IMO', 'CallSign', 'VesselType', 'Status', 'Length', 'Width', 'Draft', 'Cargo', 'TransceiverClass'], axis=1)
#sheet_for_map.info(verbose=True, show_counts=True)
#sheet_for_map.head()

sheet_for_info = sheet_result.drop(['BaseDateTime', 'LAT', 'LON', 'SOG', 'COG', 'Heading', 'IMO', 'CallSign', 'VesselType', 'Status', 'Cargo', 'TransceiverClass'], axis=1).drop_duplicates(subset=["MMSI"], keep="first")
#sheet_for_info.info(verbose=True, show_counts=True)
#sheet_for_info.head()