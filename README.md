# DF Sports-Recommender-System (My Capstone Project)
This was my final project at the Digital Futures Data Analytics training pathway. For this project I aimed to create a model to recommend the sport you would be best at using basic attributes such as height and weight. As a result I have uploaded the [Sports Recommender App](https://sports-recommender-system-joseph-brennan.streamlit.app/) on streamlit which does just that. I believe that this model is pretty good and could be very useful if you want to get involved with a new sport you've never played before. Please try it out if you're reading this!

## Contents:

1. Introduction
2. Data Collection
3. Data Formatting
4. What age will I be at my physical peak?
5. The Sport Recommender App


## 1. Introduction

At the end of the Digital Futures Data Analytics training academy we given a capstone project to put everything we learned in the academy in to practice. This was an individual project and the scope of it was extremely open. We were given just over a week to complete this project before giving a presentation of our work to the rest of the academy cohort. The project could be about anything as long as it involved data.

At the start of 2025, I decided that I wanted to exercise more and be more active in my life. I was making an effort to exercise everyday and since this was at the forefront of my mind, I decided to base this project on sports and activity. I was 23 at the time of this project and so the first question I thought of was 'What age will I be at my physical peak?'. As a 23 year old I hoped that my physical peak was yet to come as it would help motivate me to keep exercising. Then thinking about motivation for exercising I thought that maybe it would be good to get into sports. In the past I'd played a lot of football and tennis, but I was always pretty average. However, there are many sports that I never tried before, therefore not knowing if I would be good at them or not. Getting involved in a sport that I could be good at would be great motivation for keeping active and that led me to creating the Sport Recommender App as part of this project.


## 2. Data Collection

The first thing I needed to do was find data to use for this project. I quickly realised that the perfect data to use was data on Olympic athletes. The Olympics is a competition that contains a large amount of different sports so using Olympics data would be perfect for my Sports Recommender model. Also, Olympic athletes are the definition of humans at their physical peak so it would be exploring data about athletes could be good way to find out the age I would be at my physical peak. So now I knew what sort of data I wanted, I needed to go about finding the best possible dataset. I knew that for the goals of my project the Olympics dataset needed to have all of the following:

- The **age** of athletes.
- The **height** and **weight** of athletes.
- The **sport** that each athlete competed in.

It didn't take me too long to find out what the options were. The first option I thought of would be to try and scrape athlete information from the official [Paris 2024 Olympics website](https://www.olympics.com/en/olympic-games/paris-2024/athletes). However, I quickly realised that this would take far too long and since the website doesn't contain the height or weight of the athletes anyway I knew I had to look for an alternative. Thankfully, the perfect alternative was already right here on Github! A Github user called [Keith Galli](https://github.com/KeithGalli) had scraped the entirety of [Olympedia](https://www.olympedia.org/), a website that contained detailed information about Olympic athletes from 1896-2020. Not only was this data so vast, but it also contained the heights and weights of athletes which made this data perfect for my project. The only drawbacks from this dataset were that it didn't contain data from the most recent Olympic games in 2024 and also that there was a lot of missing data in certain columns including the height and weight of many athletes. However, the benifits of this dataset far outweighed the negatives and it was definitely far better than I could have hoped.

Keith Galli uploaded the data from Olympedia on to his [Olympics Dataset repository](https://github.com/KeithGalli/Olympics-Dataset/tree/master) and this repository is therefore the original source of the data in my project.


## 3. Data Formatting

Now that I located the dataset I was going to use, I needed to explore it. I used the python pandas library to read the two csv files from Keith Galli's Olympics dataset repository. These two datasets were:

(i) [athletes/bios.csv](https://github.com/KeithGalli/Olympics-Dataset/blob/master/athletes/bios.csv)
- This csv contained the athlete biographical data which included height, weight, and date of birth.

(ii) [results/results.csv](https://github.com/KeithGalli/Olympics-Dataset/blob/master/results/results.csv)
- This csv contained the athlete results which included Olympic discipline, event, and the year that the athlete competed in the Olympics.

In my python notebook, I merged these two dataframes into one on the athletes' unique ```athlete_id```. Then I needed to clean and format this combined dataframe for the purposes of my project. To summarise the formatting, the main tasks I performed were as follows.

- I created a new ```age``` column by calculating the age of each athlete by subtracting the start dates of the Olympics they competed in by their dates of birth.
- I reduced the dataframe to only contain disciplines and events that appeared in the 2020 Olympic games.
- I created a new ```male``` column which distinguishes the gender of each athlete (True if male, False if female).
- I created a new  ```physical``` column which distinguishes between Olympic sports I classed as physical (e.g. Athletics) and Olympic sports that I classed as non-physical (e.g. Golf).
- I created a new ```team``` column which distinguishes between team Olympic events and non-team events.

More details showing the way I cleaned and formatted the data are in my Jupyter Notebooks:
- [Capstone Initial Dataset](https://github.com/JBrennan2001/Sports-Recommender-System/blob/main/creating_initial_dataset.ipynb)
- [Capstone EDA](https://github.com/JBrennan2001/Sports-Recommender-System/blob/main/capstone_eda.ipynb)

## 4. What age will I be at my physical peak?

Once the data was cleaned and formatted I was ready to explore the data properly in order to try and answer the question 'What age will I be at my physical peak?'. The initial answer to this question appeared when I found out that the average age of every athlete in the dataset was 26. However, this wasn't accurate for various reasons, most importantly because
- the data ranged over a 124 year time period where the average age of athletes had probably fluctuated massively, AND
- not all Olympic disciplines should have been considered equal physically (e.g. athletics required more physicality than golf).

So I explored the change in average age over time and created a visualisation showing the average age of athletes competing in physically demanding sports and each Olympic games from 1896-2020. The main points that I took away from this graph were that:
- the average age did indeed fluctuate a lot over the years meaning that I needed to focus on only the most recent Olympics,
- the average age clearly depended on the Olympic sport meaning that I needed to do more research and analysis to find out why this was the case.

Following on from this I looked at the age distribution of athletes competing in certain sports at the 2020 Olympics. I created boxplots to present this information and discovered that the non-physical sports (e.g. Shooting) and the physical team sports (e.g. Beach Volleyball) had a much higher median athlete age than physical individual sports such as athletics. In my presentation I explored the reasons why this was the case, the main reason being that the athletes competing in physical individual sports were more likely to be at their physical peak. 

However, the median age of athletes competing in physical individual sports was still very different depending on the sport. For example, the Swimming median age was 24 whilst the Athletics median age was 27. I realised at this point that the physical peak of these sports was different because they require different physical demands. I also realised that it isn't really possible to get an exact age for physical peak because of this. Therefore I concluded that the age of physical peak was likely in the range 24-27, but with the caveat that this was for Olympic athletes and may be different for an average person like me.

More details about my exploratory data analysis and research into this question are contained in the following files:
- [Capstone EDA](https://github.com/JBrennan2001/Sports-Recommender-System/blob/main/capstone_eda.ipynb)
- [Capstone Presentation](https://github.com/JBrennan2001/Sports-Recommender-System/blob/main/Capstone%20Presentation.pptx)


## 5. The Sport Recommender App

The final part and the most important part of my project was creating the Sport Recommender App. For this recommender, I created a model using the Decision Tree classifier in the python scikit-learn library. This model was trained on the Olympics dataset that I had already cleaned, formatted and analysed. Specifically, it was trained on part of this [Model Dataset](https://github.com/JBrennan2001/Sports-Recommender-System/blob/main/Model%20Data.csv) which
- only contained data from 2000-2020 (don't want the data to be outdated),
- didn't contain any football players (the majority of men's football players at the Olympics must be 24 or below, skewing the data),
- didn't contain athletes that had null entries in the height or weight column.

The model was trained to predict the Olympic discipline of each athlete (the target) using the following six features:
- Height
- Weight
- Age
- Gender
- Physical (is the discipline classed as physical?)
- Team (is the event classed as a team event?)

