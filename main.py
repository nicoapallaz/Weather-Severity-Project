wind = 0
averageWind = []
rain = 0
averageRain = []
count = 0
while wind != -1.0 and rain != -1.0:
    rain = float(input())
    wind = float(input())
    if wind != -1.0 and rain != -1.0:
        count += 1
        averageWind.append(wind)
        averageRain.append(rain)
finalAverageWind = sum(averageWind) / count
finalAverageRain = sum(averageRain) / count
print("The average rain is " + str(round(finalAverageRain, 2)) + " inches")
print("The average wind is " + str(round(finalAverageWind, 2)) + " mph")
print("The weather severity for these " + str(len(averageRain)) + " readings is: " + str(round(finalAverageRain * 10 + finalAverageWind, 2)))