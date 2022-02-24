# Math_program

#### Starting Project - Basic Workings
I believe it would be easiest to restart this program using just a single form of math, thinking addition, then expanding it once I have the basic framwork setup. This version will likely have no menu framework to it. Will be a simple process of just displaying the correct answer if you choose to give up or get it right. I will need to decide on font size as well while doing this. Right now the default font size is very small all things considered and could be needed to enlarged.

- Detailed Initial Framework
1. Upon opening of program, you are given a screen where you can choose the type of problem you want to do. (Addition, Subtraction, Multiplication, Division).

2. After clicking your choice, the next screen has you decide to what level you want to make for difficulty.     (1, 10, 100, 1000). For instance, if you choose Addition first and then choose 1, your problems will max value at 9, if you choose 10 it maxes at 99, and so on.

3. After choosing your difficulty the problem is put on the screen. You type your answer into an entry box to see if correct.

4. You hit submit to see if you are correct. If you are, the system congrats you and asks if you want to play again (yes or no), if wrong, the system tells you to try again and blanks the entry box for you to type a new choice. In addition, there will be a button called "Give Up" which generates if you cant figure it out and it will display the correct answer in the entry box.

5. If you got the question correct, there will be two options: Play Again? and Close Program? Depending on your choice it will either generate another problem for you to do, though this will not repeat the first two steps, it will just generate another problem based on past settings. If you choose to close, it just shuts the whole thing down.
#### Completed Updates
- Basic functionality for all math types is complete and running. (Starting at ver. 0.08)
- Give up button works mid problem if the user gets it wrong and cant figure it out. (Starting at ver. 0.07)
- Quit button added to all pages except mid-problem. (Starting at ver 0.07)
- Difficulty options for all math types implemented. (Starting at ver. 0.06)


#### Future Updates
These updates will be in the future. I will not be working on these until the bare minimal is setup for the basic setup mentioned above. (Bare minimal was reached at 0.05 so some of this will start being integrated from there after.)

1. I would like the difficulty and math type questions to be a drop down menu so things can be changed on the fly instead of needing to restart the whole program to change things.

2. How many questions would you like to do? The idea here is that you are generating a group of problems to see how many you can get right. Do 10 practice problems per day? 20 in a sitting? you can choose this from the get go and this would bypass, to an extent step 5 in the basic framework up till the last problem is done anyway.
    - Could have tracking here so you know how many you got right vs wrong.
    - This could be added as a time trial as well to mimic a testing environment.
    - Could eliminate the option to change your answer as well. Then at the end, displaying the questions you got right and wrong with the associated correct answers.

3. Adding user profiles? This would likely require some sort of database to be added (sql, postgres, nosql?). Would be great for learning purposes on my own at least. Towards the project, you could track your level over time and track the amount of tests you do and how many you get right.

4. Explaining the correct answer? This would likely be incredibly difficult to do simply because each problem would have somewhat unique answers and while it could be coded out, would be a bit boring and largely be very often similar answers in verbatim. Still, it could be of interest.

5. Refining the file system so that the overall code will be more specialized and like code in its own file system.

6. Is it possible to host the program online in order for me to show others it?

7. Create a custom entry for the difficulty option screen. This is because sometimes the students would be learning particular numbers. For instance, only learning the addition problems of numbers + 4, or the 5 times tables for instance.


#### Function Description

<b>gen_ran_num()</b> - This one is sort of self explanatory. It generates the random numbers that is used by the program in order to generate the math problems. In the case of Division and Subtraction, the numbers will likely need to be verified to be placed in the correct order via another function later.

<b>check_answer_add()</b> - The first thing this does is check if the entry box entry is a number by calling is_num(description below).If it is, then it checks to see if the answer_entry is equal to the sum of both num_a and num_b. If yes, we display the status_bar correct message, we make the check_button disappear, and the another_problem button appears instead allowing the user to do another problem. Else, the program generates the status_bar message that you were incorrect, resets the answer_entry to blank and allows the user to try again.

<b>is_num()</b> - First the program tries to set the answer_entry to an integer. If this succeds, all good and we move out of the function. If it fails to do that though, such as in case of someone entering text instead of a number, the status_bar is set to text telling the user that only numbers can be entered. Then it resets the answer_entry to blank again.

<b>delete_status()</b> - Sets the answer_entry to blank while also clearing the status_bar to blank as well. (I dont believe this one is being used much currently, so this might get deleted or it might be more useful in the future.)

<b>difficulty_choice</b> - This turns on all the buttons for the choice options: one_button, ten_button, hund_button, and thou_button. Then it proceeds to call turn_off_math_type function which turns off the choices of math types.

<b>add_diff_set_1</b> - This allows us to update the if the user chooses the easiest difficulty. This makes the maximum value used by the problems to be 9. This will call addition_choice with the new value, and turn_off_diff_opt.

<b>add_diff_set_10</b> - This allows us to update the if the user chooses a middle difficulty. This makes the maximum value used by the problems to be 99. This will call addition_choice with the new value, and turn_off_diff_opt.

<b>add_diff_set_100</b> - This allows us to update the if the user chooses a middle difficulty. This makes the maximum value used by the problems to be 999. This will call addition_choice with the new value, and turn_off_diff_opt.

<b>add_diff_set_1000</b> - This allows us to update the if the user chooses a hardest difficulty. This makes the maximum value used by the problems to be 9999. This will call addition_choice with the new value, and turn_off_diff_opt.

<b>another_problem()</b> - Reset the random integer associated with num_a and num_b. Makes the another_problem button disappear and resets the check_button to be visible instead. Then it runs the delete_status function in order to clear the entry box and the status_bar. Lastly, this also calls turn_on_add which turns on all the labels and buttons associated with doing addition problems.

<b>addition_choice</b> - This first calls another_problem in order to set the random numbers, then it calls turn_on_add in order to setup and start the first addition problem (or subsequent addition problems).

<b>turn_on_add</b> - This function simply turns on all the labels, buttons, and entry box for the addition problems.

<b>turn_off_math_type</b> - The start page where you choose between addition, subtraction, division and multiplication, this is called in order to make those choices disappear after the user makes a choice.

<b>turn_off_diff_opt</b> - When choosing the difficulty, this is called after to make those options disappear.

<b>quit_prog</b> - This does exactly as it would sound like, it quits out of the program.

<b>gave_up</b> - When in the middle of a problem, if you have gotten it wrong there is now a chance to give up and have the answer displayed. This function first pulls the numbers from the problem and figures out the answer. Displays the answer to the user, while loading the another_problem button to display and hiding the give_up button. 


Test Version Update Journal
------------
0.08 - Major Updates seem to be rolling out daily right now. I have all math types working. I have reworked the code base again and got rid of a good bit of redundent code in the process. I was right in the sense that once I got subtraction added, the rest of things would fall into place quickly with just a couple of lines of code. The main problem I ran into was with division because of dividing by 0, which cant be done. So I had to write a extra if statement to change a 0 to 1 if it popped up only in the context of the division practice. I am pretty sure I can still rewrnite a few sections of code a bit better, but, right now everything works and I am overall happy with my work here. Now I think its time to move on to some of the other features I wished to add to this. 

0.07 - A somewhat major update to the overall code base even though functionality has not changed much. The main changes right now is the addition of the "Give Up" and "Quit" functionality. These do as they say, either quit the program, or give up on the problem you were trying. Otherwise I have spent a good bit of time reformatting the code so that the math symbol, math difficulty, and type of math to be done can be done inside of one function. This is in contrast to it originally being done inside of several functions, as was the choice with the difficulty. I have also begun building out the subtraction side of things as well. I believe once I get this basic framework setup, that the rest will come along quite quickly.

0.06 - Large Update overall. I added in the initial selection screen to choose the type of math you wish to do. Though as of now, only the addition is working. Once the selection is made, I also added in the functionality to choose your difficulty level as well which can range from numbers maxing at 9 up to 9999. All this required a fair bit of remastering of the various functions and what they set out to accomplish which I will update the definitions for those at a later time. I will need to research how to work these button variables I believe a bit, as of now, the difficulty is handled through 4 seperate functions that all do largely the same basic things, I imagine there is an easier way to do this, or at least a more efficient way to do it. For now though, my code works and I can revamp it later on. 

0.05 - The basic framework seems to be almost setup now. I have it generating multiple problems, it tells you if the answer is wrong, it will also yell at you if you try typing something that is not a number. Overall I think this is pretty good setup so far. In this particular update I got the button added to generate another problem, I updated the message asking if you wanted to do another problem, also changed display so the correct buttons are displayed depending on the process we are doing. Also added in a basic number check system to make sure we are not typing letters in for a number problem.

0.04 - I have the basic framework for a single problem largely set up now. I got it working where the problem is displayed, I can choose an answer and I get feedback on if question is correct or not. If its correct, the Check Answer button disappears and is replaced by a confirmation message. If its wrong, the button remains and a message pops up telling you that it was incorrect. I did also have to not have my functions in a seperate file for now as it was getting to hard to figure out how to get things working. So I will table this and fix this in the future once its more secure and running. 

0.03 - I started adding in the check answer button. I didnt think of a way to display if the answer was correct or not so need to look into the TKinter video again in order to properly display a message. I will likely need to create multiple events once the button is clicked, first to display if answer is correct or not, the second event will be to display a correct of incorrect option.

0.02 - Basic layout has been created. Still very basic though everything so far is in the correct spot. The functionality is not setup yet though, I will be working on that soon. Im trying to put the functions into a separate file, though making sure everything works has been a struggle so far. I might have to reassess this as I move forward if it makes sense to keep everything separate.

0.01 - Created basic project folders. Thats it. Im an over-achiever.



#### Links that helped me out

- Multiple Lines of Text in Tkinter Label
https://www.tutorialspoint.com/how-to-display-multiple-lines-of-text-in-tkinter-label#:~:text=You%20can%20also%20add%20multiple,line%20in%20the%20Label%20widget.

- Set Text of Tkinter Widget with a Button
https://www.delftstack.com/howto/python-tkinter/how-to-set-text-of-tkinter-entry-widget-by-using-a-button/

- How to change visibility of a button in tkinter
https://www.reddit.com/r/learnpython/comments/b4n1pl/how_to_change_the_visibility_of_a_button_in/
https://stackoverflow.com/questions/34276672/how-to-make-a-label-appear-then-disappear-after-a-certain-amount-of-time-in-pyth
https://www.tutorialspoint.com/get-the-text-of-a-button-widget-in-tkinter

- Setting and retrieving values of Tkinter variables
https://www.geeksforgeeks.org/python-setting-and-retrieving-values-of-tkinter-variable/

- General Tkinter Entry widget
https://pythonguides.com/python-tkinter-entry/
https://www.geeksforgeeks.org/python-tkinter-entry-widget/

- Initial Tkinter Basics Video Tutorial Alan D Moore
https://www.youtube.com/playlist?list=PLXlKT56RD3kBUYQiG_jrAMOtm_SfPLvwR

- Make Tkinter buttons same size
https://stackoverflow.com/questions/47860148/make-tkinter-buttons-the-same-size/62777051

