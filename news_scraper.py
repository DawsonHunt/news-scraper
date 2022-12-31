from bs4 import BeautifulSoup
import requests

## Ask user for one or more topics
topics = []
user_text = ""
while user_text.lower() != 'search':
	user_text = input("Enter news topics to search for ('Exit' to quit, 'Search' to begin search): ")

	if user_text.lower() == 'exit':
		exit()

	topics.append(user_text)
 
topics = topics[:-1] #the while loop keeps the final 'search' that the user enters, so get rid of it
num_stories = int(input("How many top stories of each topic do you want to get?: "))

# Loop through all topics, search for them, and get the top 5 stories
stories = []
for topic in topics:
	url = f'https://news.google.com/search?q={topic}'
	result = requests.get(url).text
	doc = BeautifulSoup(result, 'html.parser')

	top_5_stories = doc.find_all(class_="DY5T1d RZIKme")[:num_stories]
	for story in top_5_stories:
		headline = story.string
		link = 'https://news.google.com' + story['href'][1:]
		story_dict = {'topic': topic, 'story': f'{headline}', 'link': f'{link}'}
		stories.append(story_dict)

# Print the stories
for item in stories:
	print(f"Topic: {item['topic']}")
	print("---")
	print(f"Story: {item['story']}")
	print('---')
	print(f"Link: {item['link']}")
	print('-'*70)



