import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv


df = pd.read_csv('medium_data.csv')
sample1 = pd.read_csv('sample_2.csv')

sampleData = sample1["reading_time"].tolist()
data = df["reading_time"].tolist()

mean = statistics.mean(data)
std = statistics.stdev(data)
mean_of_sample1 = statistics.mean(sampleData)

print("Mean of the population is: ", mean)
print("Standard Deviation of the population is: ", std)


def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean


# pass the num of times you want the mean of the data points as a parametre in range function in a for loop
meanList = []
for i in range(0, 1000):
    set_of_means = random_set_of_mean(100)
    meanList.append(set_of_means)

# Calculating mean and standard deviation for the sampling distribution
standard_dev = statistics.stdev(meanList)
print("Standard Deviation for this sampling distribution is: ", standard_dev)

sampling_mean = statistics.mean(meanList)
print("Mean of sampling distribution is: ", sampling_mean)


# finding the standard deviation for starting and ending value
first_std_start, first_std_end = sampling_mean - \
    standard_dev, sampling_mean+standard_dev
second_std_start, second_std_end = sampling_mean - \
    (2*standard_dev), sampling_mean+(2*standard_dev)
third_std_start, third_std_end = sampling_mean - \
    (3*standard_dev), sampling_mean+(3*standard_dev)

print("Standard Deviation 1: ", first_std_start, first_std_end)
print("Standard Deviation 2: ", second_std_start, second_std_end)
print("Standard Deviation 3: ", third_std_start, third_std_end)


# finding the mean of the first data and plotting it on the plot
print("Mean of Sample: ", mean_of_sample1)
z_score = (mean_of_sample1 - mean)/std
print(z_score)

figure1 = ff.create_distplot([meanList], ["Reading Time"], show_hist=False)
figure1.add_trace(go.Scatter(x=[mean, mean], y=[
                  0, 0.17], mode="lines", name="Mean"))
figure1.add_trace(go.Scatter(x=[sampling_mean, sampling_mean], y=[
                  0, 0.17], mode='lines', name='Mean of sampling distribution'))

figure1.add_trace(go.Scatter(x=[first_std_start, first_std_start], y=[
                  0, 0.17], mode="lines", name="First Standard Deviation Start"))
figure1.add_trace(go.Scatter(x=[first_std_end, first_std_end], y=[
                  0, 0.17], mode="lines", name="First Standard Deviation End"))

figure1.add_trace(go.Scatter(x=[second_std_start, second_std_start], y=[
                  0, 0.17], mode="lines", name="Second Standard Deviation Start"))
figure1.add_trace(go.Scatter(x=[second_std_end, second_std_end], y=[
                  0, 0.17], mode="lines", name="Second Standard Deviation End"))

figure1.add_trace(go.Scatter(x=[third_std_start, third_std_start], y=[
                  0, 0.17], mode="lines", name="Third Standard Deviation Start"))
figure1.add_trace(go.Scatter(x=[third_std_end,  third_std_end], y=[
                  0, 0.17], mode="lines", name="Third Standard Deviation End"))
figure1.show()
