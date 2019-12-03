user_weather = input('Is it sunny, rainy or rainy and stormy? ')
if user_weather.strip() == 'sunny':
    print('Shorts all the way my man')
elif user_weather.strip() == 'rainy':
    print('Take an umbrella')
elif user_weather.strip() == 'stormy':
    print('Just stay inside')
elif user_weather.strip() == 'rainy and stormy':
    print('Definitely stay indoors')
else:
    print('sorry, i didnt quite catch that')