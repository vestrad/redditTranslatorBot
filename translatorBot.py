import praw
import time
from googletrans import Translator
import winsound
def eraseUpTo(comment):
    index = comment.find("!translate")
    return comment[index:]
def translateDefault(sentence):
    print("Translating to english...")
    translator = Translator()
    result = translator.translate(sentence, dest = 'en')
    return result.text
def translatetoEnglish(sentence):
    print("Translating to english...")
    translator = Translator()
    result = translator.translate(sentence, dest = 'en')
    return result.text
def translatetoSpanish(sentence):
    print("Translating to spanish...")
    translator = Translator()
    result = translator.translate(sentence, dest='es')
    return result.text
def findSentence(text):
    list = text.split()
    list.pop(0)
    result = " "
    result = result.join(list)
    #print(result)
    return result
def runBot(commentBody):
    translator = Translator()
    text = commentBody
    text = eraseUpTo(commentBody)
    sentence = findSentence(text)
    print("The text is: ", sentence)
    source = translator.detect(sentence)
    language = source.lang
    print("The source language is: ", language)
    if language == 'en':
        translation = translatetoSpanish(sentence)
        print("The translation is: ", translation)
        return translation
    elif language == 'es':
        translation = translatetoEnglish(sentence)
        print("The translation is: ", translation)
        return translation
    else:
        translation = translateDefault(sentence)
        print("The translation is: ", translation)
        return translation
def findComment(keyphrase, inputSubreddit):
    reddit = praw.Reddit('bot1')
    
    subreddit = reddit.subreddit(inputSubreddit)
    '''
    #template for reddi bot
    for comment in subreddit.stream.comments():
        print("Searching...")
        print("************")
        print(comment.body)
        print("************")
        if keyphrase in comment.body:
            print("Comment found! Replying...")
            comment.reply("I was summoned")
            print("Replied!")
        time.sleep(2.1)
        '''
    for comment in subreddit.stream.comments(skip_existing=True):
        print("Searching...")
        print("************")
        print(comment.body)
        print("************")
        if keyphrase in comment.body:
            winsound.Beep(2500, 1000)
            print("Comment found! Replying...")
            reply = runBot(comment.body)
            if reply.isspace() is True or not reply:
                comment.reply("I need input text!")
            else:
                commentReply = "The translation is: " + reply
                comment.reply(commentReply)
            print("Replied!")
        time.sleep(2)
def main():
    subreddit = "testingground4bots"
    keyphrase = "!translate"
    findComment(keyphrase, subreddit)
    '''
    CODE THAT TRANSLATES BASED ON INPUT STRING
    EXAMPLE: !translate german [text]
    
    text = "some tex goes here !translate german the quick red fox jumps over the lazy dog"
    index = text.find("translate")
    text = text[index:]
    print(text)
    wordList = text.split()
    print(wordList)
    destination = wordList[1]
    wordList.pop(0)
    wordList.pop(0)
    sentence = " ".join(wordList)
    translator = Translator()
    translate = translator.translate(sentence, dest = destination)
    print(translate.text)
    '''
main()
