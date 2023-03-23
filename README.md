# surf up

## Introduction:
The purpose of this report is to analyze weather data for the months of June and December in Oahu, Hawaii, using SQLAlchemy to query a SQLite database. The investor wants to know about the temperature and precipitation patterns to decide whether to build a Surf and Ice Cream shop year-round in the area. The data will be analyzed using statistics like mean, maximum, minimum, and visualized using histograms and scatterplots.

## Analysis:
The following tables present the statistics for temperature and precipitation in June and December.

#### Table 1: June Statistics for Temperature and Precipitation

![Pic_1](https://github.com/21abomas/surfs_up/blob/main/june_stat_temp_prcp.png)

#### Table 2: December Statistics for Temperature and Precipitation

![Pic_2](https://github.com/21abomas/surfs_up/blob/main/dec_stat_temp_prcp.png)

From Table 1, we can observe that the mean temperature in June is 74.94°F, which is higher than the mean temperature in December (71.04°F). However, the mean precipitation in June (0.14 inches) is lower than in December (0.22 inches).

## Visualizations:
To better understand the distribution of temperature and precipitation data, the following histograms were generated.

Pic_1: Histogram of Temperature in June

![Pic_3](https://github.com/21abomas/surfs_up/blob/main/june_temp.png)

Pic_2: Histogram of Temperature in December

![Pic_4](https://github.com/21abomas/surfs_up/blob/main/december.png)

Pic_3: Histogram of Precipitation in June

![Pic_5](https://github.com/21abomas/surfs_up/blob/main/june_temp_by_prediction.png)

Pic_4: Histogram of Precipitation in December

![Pic_6](https://github.com/21abomas/surfs_up/blob/main/december_temp_pri.png)

The histograms show that the temperature data is not strongly skewed for either month. The frequency centers around the means for both months. The precipitation data is more skewed in both months, but it is not significant. The frequency centers around 0.0-0.2 inches for June and 0.0-0.15 inches for December.

## sumarry:

Based on the statistical analysis and visualizations, it can be concluded that the temperature and precipitation means are reasonably close in June and December. The temperature data is not strongly skewed for either month. The ratio of the temperatures to the precipitation for the two months is also reasonably similar with few outliers over 3 inches of precipitation. Therefore, it can be recommended to the investor to build
