import pandas as pd

maxTemp = [22, 26, 20, 23, 23, 25, 27, 27]
minTemp = [13, 11, 16, 14, 16, 15, 15, 15]
sonnenstunden = [7, 16, 3, 7, 6, 13, 7, 8]
datum = ['28.06.', '29.06.', '30.06.', '01.07','02.07', '03.07.', '04.07', '05.07']
tage = ['Mi', 'Do', 'Fr', 'Sa', 'So', 'Mo', 'Di', 'Mi']
wind = [2, 2, 3, 3, 4, 4, 2, 2]

vorhersage = pd.DataFrame({
"Tage" : tage,
"Datum" : datum,
"Maximal" : maxTemp,
"Minimal" : minTemp,
"Sonne" : sonnenstunden,
"Wind" : wind
})
# Run through interactive Window to see plot
vorhersage.plot(x = "Datum", y = ["Maximal", "Minimal"])

vorhersage.plot(x = "Datum", y = ["Maximal", "Minimal", "Sonne"])



