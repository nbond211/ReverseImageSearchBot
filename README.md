# ReverseImageSearchBot

ReverseImageBot is a Twitter bot that creates generative art content utilizing Bing Image Search and Google Image Reverse Search.

ReverseImageBot works as follows:
1.	Selects a random word from a list of all words in the English language.
2.	Performs a Bing Image Search using the randomly generated word as the search term and uploads the first image result to Twitter.
3.	Retrieves the image uploaded most recently to the Twitter account and performs a Google Image Reverse Search on the image, generating a “best guess” for the search term that generated the image.
4.	Performs a Bing Image Search using the “best guess” term as the search term and retrieves the first image result.
5.	Using the image just retrieved and the image uploaded most recently to the Twitter account, merges the two images together using an overlay, and uploads the generated image to Twitter.
6.	Repeats steps 3 – 5. Stops when Google Image Reverse Search can no longer recognize the image.


ReverseImageBot exists as two Python scripts, “reverseImageSearchBot_initialization.py” and “ReverseImageSearchBot_search&combine.py”. “reverseImageSearchBot_initialization.py” initializes the system by generating a random word and image from that word. “ReverseImageSearchBot_search&combine.py” runs repeatedly and generated new words and images from the previous content. 
