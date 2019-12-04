# User prompted to describe the weather
user_weather = input('Is it sunny, rainy or rainy and stormy? ')

# If statements printing responses based on answers - lower means caps are irrelevant and stripping prevents white space from having an effect
if user_weather.lower().strip() == 'sunny':
    print('Shorts all the way my man')
elif user_weather.lower().strip() == 'rainy':
    print('Take an umbrella')
elif user_weather.lower().strip() == 'stormy':
    print('Just stay inside')
elif user_weather.lower().strip() == 'rainy and stormy':
    print('Definitely stay indoors')
else:
    print('sorry, i didnt quite catch that')