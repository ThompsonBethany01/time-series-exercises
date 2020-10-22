# Time Series Exercises: Analyzing, Modeling, Forecasting Temporal Events   

> Completed by Bethany Thompson in the Darden Codeup Cohort   

## About Time Series
- finding patterns in temporal data and making predictions, forecasting, based on those patterns
- Different from basic regression because time is dependent
    - This means that each 'feature', i.e. each new point in time, is dependent on the previous features
    - the previous features are the historical points in time

## Learning Goals
- acquire data via: a REST API, Cloud File Storage (AWS-S3), and SQL.
- practice using pandas to operate on dates and datetime values
- address some of the complexities of time series data, including seasonality, sampling, and storing.
- create forecasts, or time series models, using Simple Average, Moving Average, Holts Linear Trend, and Prophet, and Autoregressive model.
- practice forecasting sales (store/items sales data) and learn techniques for working with with time series data like logs (user behavior) or other financial measurements over time