import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import importlib

# Test once again test if the function is in the code with the right amount of 
# arguments and right type of return, but only gives a mesage at test 0.
# Test also gives some mesages if students make certain mistakes.


@t.test(0)
def Correctfor_empty_1word(test):
    test_text = "StickBoy"
    function_name = "text_to_unique_words"
    
    def testMethod():
        hasfunction = assertlib.fileContainsFunctionDefinitions(_fileName, function_name)
        if not hasfunction:
            info = "Make sure you use a function named " + function_name + " as you're writing your code."
            return False, info
        
        nArguments = len(lib.getFunction(function_name, _fileName).arguments)
        if nArguments != 1:
            info = "Make sure your function has 1 argument."
            return False, info

        correct_return = assertlib.sameType(lib.getFunction(function_name, _fileName)(test_text), [])
        if not correct_return:
            info = "Make sure you return an list and nothing else."
            return False, info

        if assertlib.exact(lib.getFunction(function_name, _fileName)(test_text), [test_text]):
            info = "Make sure that all letters are lowercase."
            return False, info

        if not assertlib.exact(lib.getFunction(function_name, _fileName)(""), []):
            info = "For an empty text, the list of words should be empty"
            return False, info

        return assertlib.exact(lib.getFunction(function_name, _fileName)(""), []) and assertlib.exact(lib.getFunction(function_name, _fileName)(test_text), [test_text.lower()])

    test.test = testMethod
    test.description = lambda : "Works for an empty text and for one word."


@t.test(1)
def Correctfor_sentence(test):
    test_text = "Stick Boy's Festive Season"
    function_name = "text_to_unique_words"
    
    def testMethod():
        hasfunction = assertlib.fileContainsFunctionDefinitions(_fileName, function_name)
        if not hasfunction:
            return False
        
        nArguments = len(lib.getFunction(function_name, _fileName).arguments)
        if nArguments != 1:
            return False

        correct_return = assertlib.sameType(lib.getFunction(function_name, _fileName)(test_text), [])
        if not correct_return:
            return False

        if "boy's" not in lib.getFunction(function_name, _fileName)(test_text):
            info = "Make sure to deal in the right way with punctuations."
            return False, info

        return assertlib.exact(lib.getFunction(function_name, _fileName)(test_text), ['stick', "boy's", 'festive', 'season'])

    test.test = testMethod
    test.description = lambda : "Works for multiple words with punctuation."


@t.test(2)
def Correctfor_complex_sentence(test):
    test_text = "Stick  Boy noticed that his  Christmas tree, looked  healtier than he did."
    function_name = "text_to_unique_words"
    
    def testMethod():
        hasfunction = assertlib.fileContainsFunctionDefinitions(_fileName, function_name)
        if not hasfunction:
            return False
        
        nArguments = len(lib.getFunction(function_name, _fileName).arguments)
        if nArguments != 1:
            return False

        correct_return = assertlib.sameType(lib.getFunction(function_name, _fileName)(test_text), [])
        if not correct_return:
            return False

        if "" in lib.getFunction(function_name, _fileName)(test_text):
            info = "Make sure to deal in the right way with punctuations."
            return False, info

        return assertlib.exact(lib.getFunction(function_name, _fileName)(test_text), ['stick', 'boy', 'noticed', 'that', 'his', 'christmas', 'tree', 'looked', 'healtier', 'than', 'he', 'did'])

    test.test = testMethod
    test.description = lambda : "Works for multiple words with dubble spaces."
