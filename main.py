#wrapper to execute this test.py script and fetch us whatever error has occurred during the test script execution to accomplish that we are going to use "subprocess"
from subprocess import Popen , PIPE
import requests

#now define a method execute_return() & this is going to take the command to be executed as a parameter
def execute_return(cmd) :
    args = cmd.split()                                #so now the subprocess method requires the command to be split & passed so now we are going to split this command by default it would split it on the spaces
    proc = Popen(args, stdout=PIPE, stderr=PIPE)      #then we will initialize object from the Popen class and this is going to take in the Arguments and then the "stdout" which will be initialized to PIPE, so "Output PIPE stream" & "error PIPE stream"
    out, err = proc.communicate()                     #then we are going to fetch the output & the error code using the communicate method, this would fetch us the output & the error code
    return out,err                                    #now we are gonna return it
print(execute_return("python test.py"))               #let's call this method by passing "python test.py" & print it

#WHAT IS THE ABOVE METHOD ACTUALLY DOING??
#1. Therefore so now what this method would do is it would basically take in the command "python_test.py"
#2. It would split it
#3. Then it would initialize this proc object with the output & error stream & then it would fetch it

#Now Run main.py and an error stream will occur
# Now we need to parse this error and make sure that all the unnecessary stuff is removed before we use this error to search in stach overflow,

#Writing a method that would make a request to the stack exchange API, it is going to take in the error string & make a request to the stack exchange API
#BUT we need to import the request module to make the particular request
#The below block of code is written after the if __name__ == "__main__": was written but it is inserted here midway

def make_req(error):
    resp = requests.get("https://api.stackexchange.com/"+"/2.3/search?order=desc&sort=activity&tagged=Python&intitle={}&site=stackoverflow".format(error))      #take the response and do a GET request for the endpoint on the API server, the get takes parameters as the URL of the endpoint #we need to replace intitle with whatever is being passed, so remove Type error text, this makes our format of whatever is being passes and whatever error is being passed to the API
    return resp.json()                                                                                                                                          #lastly we return respons in json

#A method to extract the URLs from the json, it would take out the links, this method would iterate to all the iteams we have fetched and make sure that particular, error Question has an answer and append the link
def get_urls(json_dict):
    url_list = []                                                    #initialize a list called URL list, here will come the list of all the URLs that we'll extract from the json code when is_answered == true
    count = 0                                                        #Since json could be huge we'll make sure that not more than 3 elements are returned for now, this is to make sure that we're not continuously iterating, through that json
    for i in json_dict["items"]:                                     #now we need to traverse through the json dict of items to extract those urls
        if i["is_answered"]:                                         #then only if that particular querie has an answer we're gonna fetch the URL
            url_list.append(i["link"])                               #append the link in the URL list, key for link would be "link"
        count+=1
        if count==3 or count == len(i):
            break

    import webbrowser                                                  #Import the Webbrowser module This helps open the browser directly with whatever link we're gonna supply
    for i in url_list:
        webbrowser.open(i)                                             #this will iterate throught whatever urls we have fetched and open the browsers automatically


    #define a main method in that call the method above & assign values to some variables
if __name__ == "__main__":
    op, err = execute_return("python test.py")                      #we see that error returned is a binary object but we will convert it to string
    error_message = err.decode("utf-8").strip().split("/r/n")[-1]   #to do this create one more variable, we are going to decode this from binary to utf-8, then split it based on backslash(/r) & backslash(/n), because of the output error message, also strip un-necessary spaces
    print(error_message)                                            #print error message

# 1. in output a list is returned with traceback, the file & then the actual error -> The actual error is last but one element in the list
# 2. the error we are interested in is the last element of this list, so we need to extract this message we add [-1] after split("/r/n") to accomplish this
# 3. OUTPUT IN TERMINAL -> TypeError: unsupported operand type(s) for +: 'int' and 'str' -> Now this is the error message we are interested in

    if error_message:                                               #now if there is an error,we are going to create a new variable called "filter_err"
        filter_err = error_message.split(":")                       #we are gonna split the error message based on the colon to extract the "type of the error" & the "error message"
        json1 = make_req(filter_err[0])                             #First passing only the type of the error
        json2 = make_req(filter_err[1])                             #second passing the error message
        json = make_req(filter_err[0])                             #third one is going to take the entire error message
        get_urls(json1)
        get_urls(json2)
        get_urls(json)
    else:
        print("No Error")

#1. Now we are going to use the "Stack EXCHANGE API" to querie for this particular error message, so google search the stack exchange API
#2. In the documentation there are different API endcalls but we are interested in search call
#3. In the search we observe that it akes in the in-title field -> the error message that we have found out, Tagged -> python as the tag for now we'll only be interested in Python ones, you can change the tag antime for other languages
#4. Take this error message TypeError: unsupported operand type(s) for +: 'int' and 'str' & querie that in the API there, paste it in "intitle" field and run
#5. The result i the API webpage window is in "json",
#6. Now we are going to achieve this same using "request library" in Python
#7. In the json code there are items: and in the items there is list and in this list we have if true then send some links
#8. We are only interested in having the answer = true so if the answer is there we are going to be returned that link
#9. Therefore we need to call inside the make request method these 3 -> json1 = make_req(filter_err[0]), json2 = make_req(filter_err[1]), json1 = make_req(filter_err[0]), In total we are making three calls to fetch the json









