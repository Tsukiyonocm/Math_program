# Math_program

#### Starting Project - Basic Workings
I believe it would be easiest to restart this program using just a single form of math, thinking addition, then expanding it once I have the basic framwork setup. This version will likely have no menu framework to it. Will be a simple process of just displaying the correct answer if you choose to give up or get it right. I will need to decide on font size as well while doing this. Right now the default font size is very small all things considered and could be needed to enlarged.

- Framework
1. Open program and decide what type of math problem you are doing. (addition)
2. Generate and display the math problem with an input box for the answer.
3. A simple button to select when complete which generates a message saying if its correct or not.
4. If wrong, you can re-enter for another try, or, give up, where the correct answer will be displayed.
5. Play again? If yes, repeat step 2 thru 5. If no, close program. 

#### Future Updates
These updates will be in the future. I will not be working on these until the bare minimal is setup for the basic setup mentioned above.
1. Build out the framework to do multiple types of math. This can include: Addition, Subtraction, Multiplication, and Division.
    - Thinking this could be a drop down menu? Or perhaps something buried in the toolbar to choose as well. This will become more fluid as I learn more of the capabilities of Tkinter and what can be done in regards to regenerating the buttons.

2. How many questions would you like to do? The idea here is that you are generating a group of problems to see how many you can get right. Do 10 practice problems per day? 20 in a sitting? you can choose this from the get go and this would bypass, to an extent step 5 in the basic framework up till the last problem is done anyway. 
    - Could have tracking here so you know how many you got right vs wrong.
    - This could be added as a time trial as well to mimic a testing environment.
    - Could eliminate the option to change your answer as well. Then at the end, displaying the questions you got right and wrong with the associated correct answers.

3. Adding user profiles? This would likely require some sort of database to be added (sql, postgres, nosql?). Would be great for learning purposes on my own at least. Towards the project, you could track your level over time and track the amount of tests you do and how many you get right.

4. Choose the difficulty of the problem? For instance, at the beginning you have a choice between: 1, 10, 100, 1000. What this means is the numbers generated would be that deep. For example if you choose 10, this means the numbers could be generated up to 99, so double digits. 100 would generate up to 999 and so on.

5. Explaining the correct answer? This would likely be incredibly difficult to do simply because each problem would have somewhat unique answers and while it could be coded out, would be a bit boring and largely be very often similar answers in verbatim. Still, it could be of interest.

6. Refining the file system so that the overall code will be more specialized and like code in its own file system. 



Test Version Update Journal
------------
0.04 - I have the basic framework for a single problem largely set up now. I got it working where the problem is displayed, I can choose an answer and I get feedback on if question is correct or not. If its correct, the Check Answer button disappears and is replaced by a confirmation message. If its wrong, the button remains and a message pops up telling you that it was incorrect. I did also have to not have my functions in a seperate file for now as it was getting to hard to figure out how to get things working. So I will table this and fix this in the future once its more secure and running. 

0.03 - I started adding in the check answer button. I didnt think of a way to display if the answer was correct or not so need to look into the TKinter video again in order to properly display a message. I will likely need to create multiple events once the button is clicked, first to display if answer is correct or not, the second event will be to display a correct of incorrect option.

0.02 - Basic layout has been created. Still very basic though everything so far is in the correct spot. The functionality is not setup yet though, I will be working on that soon. Im trying to put the functions into a separate file, though making sure everything works has been a struggle so far. I might have to reassess this as I move forward if it makes sense to keep everything separate.

0.01 - Created basic project folders. Thats it. Im an over-achiever.

