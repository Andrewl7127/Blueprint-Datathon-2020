# Exploring Big Trends COVID-19 (Vertical 3)

This report provides an analysis and visualizations regarding the correlation between geographic, demographic, social, and political trends and COVID-19 cases and deaths.

**Abstract**

With one of the highest infection rates globally, the United States has been struggling to find a healthy balance between practicing social distancing and maintaining daily activity. As a result, certain measures must be taken to identify COVID-19 spread and mitigate COVID-19 pockets across the nation. To do so, we looked at various metrics on a county-by-county basis so as to best identify at-risk areas. The metrics we used include, but are not limited to, case/death counts, time spent in quarantine, and demographic factors (i.e. race, marital status, etc.). Our general hypothesis is that counties that do not respect social distancing policies have witnessed and/or will experience dramatic increases in COVID-19 cases. It is also worth mentioning that more population-dense regions will likely take longer to recover but we may see fewer new cases per capita.

**Methodology**

Using the provided SafeGraph data, Open Census data, County/State-level intervention data, and Historical Cases data, we sought to understand the relationship between COVID-19 and potential sociopolitical predictors. After cleaning, preprocessing, and aggregating the data, we created multiple visualizations, including interactive maps, to analyze the trends in how different variables such as travel time, percent of time spent in quarantine, and device count have varied over across U.S. counties over the course of the COVID-19 pandemic and their correlation to the increasing number of COVID cases and deaths. Finally, to further identify key socio-political predictors in COVID-19 cases, we trained a random forest model which can be found here [Random Forest Model](https://github.com/Andrewl7127/BlueprintDatathon/blob/main/Modeling.ipynb). For the sake of user-friendliness and potential further research, we hosted all our visualizations on a [web application](https://blueprint-datathon.herokuapp.com/) built through Streamlit and Heroku - a development-friendly cloud platform. 

**Discussion**

One of the first things that came to mind when understanding pandemic spread was to what degree each county enforced and respected common-sense quarantine procedures. To do so we looked at the ‘Travel Time’ - the distance traveled outside one’s home over a given time period. Similarly, we wanted to see the ‘% Time in Quarantine’ of each county (i.e. the percentage of time in which people respected quarantine procedures). Looking at the map pertaining to ‘Travel Time,’ it is worth noting that people generally traveled far less after the inception of the pandemic and this trend continues today - with only a handful of counties who have residents frequently exiting/entering county lines. This pattern likely can be attributed to the fact that people no longer cross larger distances or travel extensively due to the heavy restrictions enforced by the airline and other transportation industries. The travel time overall shows a consistent decreasing behavior and by itself does not seem to have a noticeable impact on COVID cases or deaths.

However, when analyzing the ‘% Time in Quarantine’ map it appears that the general public has grown nonchalant in following quarantine procedures as time has gone by. Remarkably in the early summer months (March, April, May), there was a noticeable increase in time spent in quarantine. At the onset of Summer and into Fall, however, there is a roughly 30% decrease across all states in time spent in quarantine (and away from the general public). This could lead to a sudden surge and potential 2nd wave.

On the topic of Telehealth, Dr. Artandi mentioned that many people who do not have access to the technology needed for virtual appointments are potentially at risk of being misinformed. This misinformation could result in patients not visiting hospitals when needed (or vice versa), potentially leading to more fatalities. In order to ascertain these ‘technology-devoid’ counties, we looked at the number of devices as a factor of county and time. Rural counties far from large cities disproportionately suffer the most. Places like New Mexico, Montana, and Nevada never rose above 50 devices, lagging far behind the national average of 120 devices. These regions in particular do indeed see a surge of cases as early as June.

Looking at COVID-19 cases, population-dense areas are hit hardest in terms of sheer numbers. All across the United States, COVID-19 cases either increased or at the very least stagnated over the Summer and into Fall. Namely, Southern California and the counties surrounding major cities (i.e. New York, Miami, Seattle, etc.) sported the highest COVID-19 case counts. This is logical seeing as more densely populated areas with more residents will give way to more case-by-case occurrences. As expected the number of deaths was directly proportional to the number of cases in a given county. Furthermore, looking at the COVID-19 case map it appears that counties situated around the coast (Pacific Coast, Gulf Coast, Miami Coast, Eastern Seaboard, etc.) all have a higher case count than their in-land counterpart (even within the same state or adjacent inland county). This is likely in part due to the fact large metropolitan cities are usually situated around bodies of water, but it could also be argued that since coastal cities are hubs for international trade, there could be increased exposure to the COVID-19 pathogen. Seeing as cases have rapidly been rapidly increasing in the Fall - especially along the Eastern and Western seaboard - this could indicate that as temperature decreases and summer conditions slow down, more cases pop up. However, we by no means have the full epidemiological picture seeing as the [2nd wave has still yet to happen](https://www.hopkinsmedicine.org/health/conditions-and-diseases/coronavirus/first-and-second-waves-of-coronavirus).

On the topic of demographics, a study by the [National Post](https://nationalpost.com/news/canada/effects-of-covid-19-lockdown-most-difficult-on-single-people-modelling-by-economists-suggests) found that the effect of COVID-19 lockdown has been the most difficult mentally for single people who no longer have constant social interaction. Based on the fact that more and more able-bodied people are breaking quarantine protocol (see COVID-19 Trends page), counties with a majority unmarried population are slowly becoming the hotspots for confirmed COVID-19 cases (not fatalities). This trend was especially pronounced when looking at the Demographic mapping for Proportion of Single Residents. As seen in the map, many major cities such as Houston, Boston, and the general South, (which were already hotspots to begin with) had a single population between 60-80%. The percent of time spent in quarantine in these regions especially dropped to 40-50% and continued decreasing by mid-Summer. This could indicate that single people are a large carrier who likely are already infecting at-risk populations.

To better visualize the relationship between time spent in quarantine and new COVID-19 case outbreaks, we looked at how these two metrics varied over time on a state-by-state basis. In nearly every side-by-side comparison over a period of 7 months (January - July), we can see that the states which respected quarantine protocol had fewer new cases - thereby flattening the curve. On the other hand, as the median percentage of time spent at home decreased, states typically saw the number of new cases rise month-to-month. It follows then that as people spend less time at home, the number of new cases would be expected to be higher due to there being more chances one is contaminated by or contaminates another. This trend is especially true in many of the midwest and plains states (e.g. Indiana, Illinois, Iowa, and Kansas), with some southeast states (e.g. Arkansas and North Carolina) seeing these spikes as well. Though time spent at home decreased across the board (likely due to growing impatience towards stay-at-home recommendations/orders), many states were able to minimize the spread of the virus following the spike of cases that many places in the country saw around July. We hypothesize that this is due to safeguarding actions such as mask-wearing and social-distancing mandates, and could have been motivated by extremely high increases in cases relative to the rest of the country (e.g. Arizona, New York, and California). As such, we contend that when precautionary measures are taken, states have shown the ability to conditionally reopen without reigniting the spread of the virus.

Furthermore, policy also plays a large part in public behavior. In order to quantify policy’s impact, we created a strictness measure that was an aggregate of various weighted policy metrics to see how “strict” different state policies were over a period of 10 months. From January to Mid-March virtually zero state-wide policy was officially put in place, however, with the onset of the first wave in April, many states implemented policies over the course of the Pandemic. Some key players include New York who implemented extremely strict policies towards the beginning of June and slowly made roll-backs once their COVID cases stagnated. Conversely, many Southern states have implemented strict policies that likely are not being respected or are not being actively enforced (i.e in the case of Alabama, Kentucky).

To further our hypothesis that the aforementioned sociopolitical factors are correlated with COVID-19 cases and death, we trained a random forest model to predict state per-capita COVID-19 cases based on recent state demographics and policies related to COVID-19. We decided on using a random forest model since random forests work well with nonlinear data, are robust to outliers, are resistant against overfitting, and handle various forms of data well. We created three models (base, best RandomSearchCV, and best GridSearchCV), and after preprocessing and hyperparameter tuning, our best model achieved 81% accuracy, strongly suggesting that there is a correlation between sociopolitical factors and COVID-19 cases. We then extracted the feature importances for each of the three models, and surprisingly, racial demographics played a large part which might point to the fact new studies suggest COVID-19 [disproportionately impacts people of African American and Asian heritage](https://www.hopkinsmedicine.org/health/conditions-and-diseases/coronavirus/covid19-racial-disparities). Other indicative features included face mask requirements and the proportion of married individuals, further supporting our hypothesis that COVID-19 cases were indeed a factor of social distancing policy and marital status. One potential shortcoming of the models, however, was the failure to account for time (i.e. who implemented policies first) as well as the limited data due to aggregation. This can be solved by getting a more specific dataset.

**Conclusion**

At the end of the day, we faced quite a few challenges along the way. One challenge was standardizing the datasets to have the same unique geographic identifiers (FIPS codes). When initially plotting our maps, we had multiple states missing data. After backtracking and looking at our geographic identifiers, we realized there were mislabeled FIPS codes due to missing leading zeros and created a function to properly identify and alter any inaccurate FIPS codes. Another challenge was matching data that was measured on different levels (state, county), which was solved through grouping and aggregation. 

Through the Blueprint Datathon, we developed skills using multiple technologies such as Python, R, and web application frameworks. After hours of wrestling with data cleaning and preprocessing, we realized the importance of data validity and quality. In terms of originality, we looked at our data in broad strokes. When taking on this task, we specifically wanted to use the entirety of the data despite the large size of the SafeGraph data (24 GB). Additionally, we wanted to take an objective perspective by letting the data guide our findings through intensive exploratory data analysis and visualizations. Finally, we wanted to apply machine learning and use its findings to complement our predictions. 
At the end of the day, by addressing these predictors and analyzing trends on either a county or state level, we can figure out what factors play into COVID-19 cases and deaths, where potential hotspots might arise, and what steps should be taken to protect our fellow Americans.

**Try it out:** https://blueprint-datathon.herokuapp.com/

