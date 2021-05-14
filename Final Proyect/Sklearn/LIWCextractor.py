'''Python Modules'''
import csv
import json
import requests

''' Api's keys'''
url = 'https://api.receptiviti.com/v1/score'
api_key = 'd0ea705cac674e19a54b2adf0e3873e4'
api_secret = 'o7mMl4rcQY5R2dq5od6F6Xy3UKZqkp6glk6qh5OeYo9Y/6Lo8Qqm0XaW'

def api_calls(text):
    data = json.dumps({
    'request_id': 'req-1',
    'content': text,
    'language': 'en'
    })
    response = requests.post(url, auth=(api_key, api_secret), data=data)

    data = response.json()
    results = data['results']
    results_summary = results[0]['summary']
    results_liwc = results[0]['liwc']['scores']
    results_sallee_counts = results[0]['sallee']['counts']
    results_sallee_scores = results[0]['sallee']['scores']

    features = {
        'word_count': results_summary['word_count'],
        'words_per_sentence': results_summary['words_per_sentence'],
        'sentence_count': results_summary['sentence_count'],
        'six_plus_words': results_summary['six_plus_words'],
        'emojis': results_summary['emojis'],
        'emoticons': results_summary['emoticons'],
        'hashtags': results_summary['hashtags'],
        'urls': results_summary['urls'],
        'analytical_thinking': results_liwc['analytical_thinking'],
        'authentic': results_liwc['authentic'],
        'clout': results_liwc['clout'],
        'emotional_tone': results_liwc['emotional_tone'],
        'dictionary_words': results_liwc['dictionary_words'],
        'achievement': results_liwc['categories']['achievement'],
        'adjectives': results_liwc['categories']['adjectives'],
        'adverbs': results_liwc['categories']['adverbs'],
        'affect': results_liwc['categories']['affect'],
        'affiliation': results_liwc['categories']['affiliation'],
        'all_punctuation': results_liwc['categories']['all_punctuation'],
        'anger_words': results_liwc['categories']['anger_words'],
        'anxiety_words': results_liwc['categories']['anxiety_words'],
        'apostrophes': results_liwc['categories']['apostrophes'],
        'articles': results_liwc['categories']['articles'],
        'assent': results_liwc['categories']['assent'],
        'auxiliary_verbs': results_liwc['categories']['auxiliary_verbs'],
        'biological_processes': results_liwc['categories']['biological_processes'],
        'body': results_liwc['categories']['body'],
        'causation': results_liwc['categories']['causation'],
        'certainty': results_liwc['categories']['certainty'],
        'cognitive_processes': results_liwc['categories']['cognitive_processes'],
        'colons': results_liwc['categories']['colons'],
        'commas': results_liwc['categories']['commas'],
        'comparisons': results_liwc['categories']['comparisons'],
        'conjunctions': results_liwc['categories']['conjunctions'],
        'dashes': results_liwc['categories']['dashes'],
        'death': results_liwc['categories']['death'],
        'differentiation': results_liwc['categories']['differentiation'],  
        'discrepancies': results_liwc['categories']['discrepancies'],
        'drives': results_liwc['categories']['drives'],
        'exclamations': results_liwc['categories']['exclamations'],
        'family': results_liwc['categories']['family'],
        'feel': results_liwc['categories']['feel'],
        'female': results_liwc['categories']['female'],
        'filler_words': results_liwc['categories']['filler_words'],
        'focus_future': results_liwc['categories']['focus_future'],
        'focus_past': results_liwc['categories']['focus_past'],
        'focus_present': results_liwc['categories']['friends'],
        'friends': results_liwc['categories']['friends'],
        'function_words': results_liwc['categories']['function_words'],
        'health': results_liwc['categories']['health'],
        'hear': results_liwc['categories']['hear'],
        'home': results_liwc['categories']['home'],
        'i': results_liwc['categories']['i'],
        'impersonal_pronouns': results_liwc['categories']['impersonal_pronouns'],
        'informal_language': results_liwc['categories']['informal_language'],
        'ingestion': results_liwc['categories']['ingestion'],
        'insight': results_liwc['categories']['insight'],
        'interrogatives': results_liwc['categories']['interrogatives'],
        'leisure': results_liwc['categories']['leisure'],
        'male': results_liwc['categories']['male'],
        'money': results_liwc['categories']['money'],
        'motion': results_liwc['categories']['motion'],
        'negations': results_liwc['categories']['negations'],
        'negative_emotion_words': results_liwc['categories']['negative_emotion_words'],
        'netspeak': results_liwc['categories']['netspeak'],
        'nonfluencies': results_liwc['categories']['nonfluencies'],
        'numbers': results_liwc['categories']['numbers'],
        'other_grammar': results_liwc['categories']['other_grammar'],
        'other_punctuation': results_liwc['categories']['other_punctuation'],
        'parentheses': results_liwc['categories']['parentheses'],
        'perceptual_processes': results_liwc['categories']['perceptual_processes'],
        'periods': results_liwc['categories']['periods'],
        'personal_concerns': results_liwc['categories']['personal_concerns'],
        'personal_pronouns': results_liwc['categories']['personal_pronouns'],
        'positive_emotion_words': results_liwc['categories']['positive_emotion_words'],
        'power': results_liwc['categories']['power'],
        'prepositions': results_liwc['categories']['prepositions'],
        'pronouns': results_liwc['categories']['pronouns'],
        'quantifiers': results_liwc['categories']['quantifiers'],
        'question_marks': results_liwc['categories']['question_marks'],
        'quotes': results_liwc['categories']['quotes'],
        'relativity': results_liwc['categories']['relativity'],
        'religion': results_liwc['categories']['religion'],
        'reward': results_liwc['categories']['reward'],
        'risk': results_liwc['categories']['risk'],
        'sad_words': results_liwc['categories']['sad_words'],
        'see': results_liwc['categories']['see'],
        'semicolons': results_liwc['categories']['semicolons'],
        'sexual': results_liwc['categories']['sexual'],
        'she_he': results_liwc['categories']['she_he'],
        'social': results_liwc['categories']['social'],
        'space': results_liwc['categories']['space'],
        'swear_words': results_liwc['categories']['swear_words'],
        'tentative': results_liwc['categories']['tentative'],
        'they': results_liwc['categories']['they'],
        'time': results_liwc['categories']['time'],
        'time_orientation': results_liwc['categories']['time_orientation'],
        'verbs': results_liwc['categories']['verbs'],
        'we': results_liwc['categories']['we'],
        'work': results_liwc['categories']['work'],
        'you': results_liwc['categories']['you'],
        'admiration_count': results_sallee_counts['emotions']['admiration'],
        'amusement_count': results_sallee_counts['emotions']['amusement'],
        'anger_count': results_sallee_counts['emotions']['anger'],
        'boredom_count': results_sallee_counts['emotions']['boredom'],
        'calmness_count': results_sallee_counts['emotions']['calmness'],
        'curiosity_count': results_sallee_counts['emotions']['curiosity'],
        'desire_count': results_sallee_counts['emotions']['desire'],
        'disgust_count': results_sallee_counts['emotions']['disgust'],
        'excitement_count': results_sallee_counts['emotions']['excitement'],
        'fear_count': results_sallee_counts['emotions']['fear'],
        'gratitude_count': results_sallee_counts['emotions']['gratitude'],
        'joy_count': results_sallee_counts['emotions']['joy'],
        'love_count': results_sallee_counts['emotions']['love'],
        'pain_count': results_sallee_counts['emotions']['pain'],
        'sadness_count': results_sallee_counts['emotions']['admiration'],
        'surprise_count': results_sallee_counts['emotions']['surprise'],
        'goodfeel_count': results_sallee_counts['goodfeel'],
        'ambifeel_count': results_sallee_counts['ambifeel'],
        'badfeel_count': results_sallee_counts['badfeel'],
        'emotionality_count': results_sallee_counts['emotionality'],
        'sentiment_count': results_sallee_counts['goodfeel'],
        'non_emotion_count': results_sallee_counts['non_emotion'],
        'admiration_score': results_sallee_scores['emotions']['admiration'],
        'amusement_score': results_sallee_scores['emotions']['amusement'],
        'anger_score': results_sallee_scores['emotions']['anger'],
        'boredom_score': results_sallee_scores['emotions']['boredom'],
        'calmness_score': results_sallee_scores['emotions']['calmness'],
        'curiosity_score': results_sallee_scores['emotions']['curiosity'],
        'desire_score': results_sallee_scores['emotions']['desire'],
        'disgust_score': results_sallee_scores['emotions']['disgust'],
        'excitement_score': results_sallee_scores['emotions']['excitement'],
        'fear_score': results_sallee_scores['emotions']['fear'],
        'gratitude_score': results_sallee_scores['emotions']['gratitude'],
        'joy_score': results_sallee_scores['emotions']['joy'],
        'love_score': results_sallee_scores['emotions']['love'],
        'pain_score': results_sallee_scores['emotions']['pain'],
        'sadness_score': results_sallee_scores['emotions']['sadness'],
        'surprise_score': results_sallee_scores['emotions']['surprise'],
        'goodfeel_score': results_sallee_scores['goodfeel'],
        'ambifeel_score': results_sallee_scores['ambifeel'],
        'badfeel_score': results_sallee_scores['badfeel'],
        'emotionality_score': results_sallee_scores['emotionality'],
        'sentiment_score': results_sallee_scores['sentiment'],
        'non_emotion_score':results_sallee_scores['non_emotion'],
        'emotion_word_count': results[0]['sallee']['emotion_word_count']
    }

    return dict(features)

def extract_data():
    with open('Training-test.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        with open('output.csv','w') as file: 
            fieldnames = ['ID', 'Text', 'Class', 'word_count', 'words_per_sentence', 'sentence_count', 'six_plus_words', 'emojis', 'emoticons', 'hashtags', 'urls', 'analytical_thinking', 'authentic', 'clout', 'emotional_tone', 'dictionary_words', 'achievement', 'adjectives', 'adverbs', 'affect', 'affiliation', 'all_punctuation', 'anger_words', 'anxiety_words', 'apostrophes', 'articles', 'assent', 'auxiliary_verbs', 'biological_processes', 'body', 'causation', 'certainty', 'cognitive_processes', 'colons', 'commas', 'comparisons', 'conjunctions', 'dashes', 'death', 'differentiation', 'discrepancies', 'drives', 'exclamations', 'family', 'feel', 'female', 'filler_words','focus_future', 'focus_past', 'focus_present', 'friends', 'function_words', 'health', 'hear', 'home', 'i', 'impersonal_pronouns', 'informal_language', 'ingestion', 'insight', 'interrogatives', 'leisure', 'male', 'money', 'motion', 'negations', 'negative_emotion_words','netspeak', 'nonfluencies', 'numbers','other_grammar', 'other_punctuation', 'parentheses', 'perceptual_processes', 'periods', 'personal_concerns', 'personal_pronouns', 'positive_emotion_words', 'power', 'prepositions', 'pronouns', 'quantifiers', 'question_marks', 'quotes', 'relativity', 'religion', 'reward', 'risk', 'sad_words', 'see', 'semicolons', 'sexual', 'she_he', 'social', 'space', 'swear_words', 'tentative', 'they', 'time', 'time_orientation', 'verbs', 'we', 'work', 'you', 'admiration_count', 'amusement_count', 'anger_count', 'boredom_count', 'calmness_count', 'curiosity_count', 'desire_count', 'disgust_count', 'excitement_count', 'fear_count', 'gratitude_count', 'joy_count', 'love_count', 'pain_count', 'sadness_count', 'surprise_count', 'goodfeel_count', 'ambifeel_count', 'badfeel_count', 'emotionality_count', 'sentiment_count', 'non_emotion_count', 'admiration_score', 'amusement_score', 'anger_score', 'boredom_score', 'calmness_score', 'curiosity_score', 'desire_score', 'disgust_score', 'excitement_score', 'fear_score', 'gratitude_score','joy_score', 'love_score', 'pain_score', 'sadness_score', 'surprise_score', 'goodfeel_score', 'ambifeel_score', 'badfeel_score', 'emotionality_score', 'sentiment_score', 'non_emotion_score', 'emotion_word_count']

            csv_writer = csv.DictWriter(file, fieldnames=fieldnames) # Establishes the headers of output.csv
            csv_writer.writeheader() 

            for row in csv_reader:
                text = row['Text']
                print(type(text))
                features_dict = api_calls(text)
                print(features_dict)
                new_row = dict(row)
                new_row.update(features_dict)
                csv_writer.writerow(new_row)

'''Starts execution of the program'''
if __name__ == "__main__":
    extract_data()


'''Debugging'''
# print(response.json())
# print(type(response))
# print(type(response.json()))