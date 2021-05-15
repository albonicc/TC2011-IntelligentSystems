# TC2011-IntelligentSystems

## Course Objective
Upon completion of this course, students will be able to formulate, design and develop simple intelligent systems based on different machine learning approaches, analyze and distinguish diverse intelligent systems and select an intelligent system to apply it to specific real-life situations. Therefore, the main course content includes: Formulation of intelligent agents, agents that solve problems, knowledge-based agents and agents that learn.

## What I did in this course?
The whole course was oriented into the final proyect, which was a competition among the students enrolled in Kaggle [https://www.kaggle.com/c/detecting-fake-news]. The competition consisted in creating a model capable of detecting Fake News. In order to acheive this, a training dataset of 500 news in English and Spanish was provided, each news in the dataset had an ID and a class, where the possible classes were: 1 - Fake News, 0 - Not Fake News. The accuracy of every trained model was tested with a testing dataset of 150 news, each trained model had to assign labels to the testing dataset based on the previous experience from the training process, then the training dataset was uploaded to Kaggle as a CSV file in order to Kaggle assign a grade depending on the accuracy of the model.

Throughout this course, I used [Weka](https://www.cs.waikato.ac.nz/ml/weka/), which is a Graphical ML framework developed by the University of Waikato, for training all my models and preprocessing my data.

### Extracting features from Dataset
I used different APIs for extracting different features from the training news dataset. In the first stage of the course. I extracted 10 features using [MeaningCloud](https://www.meaningcloud.com/) and [ParallelDots](https://www.paralleldots.com/) APIs, 5 for sentiment analysis and 5 for emotions.

After not getting the results I expected (accuracy score in Kaggle of 0.61666 using a Random Forest classifier), I extracted 5 new features from the ParallelDots API, 1 related to emotions (excited) and 4 related to Intent (spam, news, feedback and marketing). My accuracy score in Kaggle increased a little after extracting these new 5 features (0.68055 using a Logistic Regression classifier).

I was still not satisfied with my results. My hypothesis was that I wasn't obtained good results because my number of features was too low, so I decided to extract 150 new features related to linguistics based on LIWC (Linguistic Inquiry and Word Count) and SALLEE (Syntax-Aware LexicaL Emotion Engine; pronounced “Sally”) using the [Receptivity API](https://www.receptiviti.com/). Then I used again the Logistic Regression classifier but with all the new features, resulting in a higher score in Kaggle (0.89166). It was a great improvement but I was still not satisfied, so I tried different classifiers aiming for a higher score.

Then I used a Random Forest classifier with the 165 features, obtaining a new all-time-high score of 0.96666 in Kaggle. After that, I supposed that not all the features were relevant for the classification of Fake News, so then I used a CFsSubsetEval Attribute Evaluator for preproccesing data, which threw that only 17 of the 165 features where relevant for the detection of Fake News.

Finnaly, I obtained a new all-time-high score in Kaggle of 0.97500 using a LMT classifier with the 17 most relevant features. This new score not only made me obtain my best score throughout all the Kaggle competition, but also it made me obtain the 1st place in the competition. 
