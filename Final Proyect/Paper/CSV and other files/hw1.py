'''Python Modules'''
import csv
import meaningcloud
import paralleldots

'''API's keys'''
license_key_mc = '7ea5541fcc9a26dcacd98d7806d2b40c' # MeaningCloud
license_key_pd = 'OGE8u9UpldaHfshI47DZouZPzJPsEqxjHSVFBE7XoFo' #Parallel Dots 5
# license_key_pd = '7t9Wz426XtNCmNqXFKaaULaZiNpiDvcrbqvuRKZ7C0M' # Parallel Dots 4
# license_key_pd = 'Eenf7s28vA3jJGQGNOTsVGKXUt3PH5iR6zPbDMeVehY' # Parallel Dots 3
# license_key_pd = 'HqDCrmIo27TYOLKVkb64jSMkWC8Gt12vOl5aSG7mQF0' # Parallel Dots 2
# license_key_pd = 'c2kfJ0zi0mMLf1nc8JGN8isHAQeEg2XsYmbOmcJ4Pb8' # Parallel Dots 1

paralleldots.set_api_key(license_key_pd)

def api_calls(text):

    # Gets the sentiment response of each text of the CSV file by using the MeaningCloud API
    sentiment_response = meaningcloud.SentimentResponse(meaningcloud.SentimentRequest(license_key_mc, lang='en', txt=text, txtf='plain').sendReq()).getResults()

    # Gets the emotion response of each text of CSV file by using the parallel dots API
    emotion_response = paralleldots.emotion(text)

    # Gets the intent response for each text of the CSV file
    intent_response=paralleldots.intent(text)

    # Sentiments Meaning Cloud
    sentiment_dict = {
        'score_tag': sentiment_response['score_tag'],
        'agreement': sentiment_response['agreement'],
        'subjectivity': sentiment_response['subjectivity'],
        'confidence': sentiment_response['confidence'],
        'irony': sentiment_response['irony']
    }
    
    # Emotions Parallel Dots
    emotion_dict = {
        'happy': emotion_response['emotion']['Happy'], # Returns a dict
        'angry': emotion_response['emotion']['Angry'], 
        'bored': emotion_response['emotion']['Bored'], 
        'fear' : emotion_response['emotion']['Fear'],
        'sad'  : emotion_response['emotion']['Sad']  
    }

    # Intent Parallel Dots
    intent_dict = {
        'news': intent_response['intent']['news'],
        'query': intent_response['intent']['query'],
        'spam': intent_response['intent']['spam'],
        'marketing': intent_response['intent']['marketing'],
        'feedback': intent_response['intent']['feedback']
    }
    
    e_s_dict = dict(sentiment_dict)
    e_s_dict.update(emotion_dict)
    e_s_dict.update(intent_dict)

    return e_s_dict

def extract_data():
    with open('Training492.csv') as csv_file: 
        csv_reader = csv.DictReader(csv_file) # Parses the contents of Training.csv as dictionaries

        with open('output.csv','w') as file: 
            fieldnames = ['ID', 'Text', 'Class', 'score_tag', 'agreement', 'subjectivity', 'confidence', 'irony', 'happy', 'angry', 'bored', 'fear', 'sad', 'news', 'query', 'spam', 'marketing', 'feedback']

            csv_writer = csv.DictWriter(file, fieldnames=fieldnames) # Establishes the headers of output.csv
            csv_writer.writeheader() 

            for row in csv_reader:
                text = row['Text']
                e_s_dict = api_calls(text) # Calls the API's of Meaning Cloud and Paralled dots
                print(e_s_dict)
                new_row = dict(row)
                new_row.update(e_s_dict)  # Merges the data of Training.csv with the responses of the APIs
                csv_writer.writerow(new_row)


''' Starts execution of the program '''
if __name__ == "__main__":           
    extract_data()


