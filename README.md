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

Now that I located the dataset I was going to use, I needed to explore it. I used the ```pandas``` library in python to read the 
