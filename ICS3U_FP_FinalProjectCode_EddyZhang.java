/*
 * Name: Eddy Zhang
 * Course: ICS3U
 * Date: June 3, 2019
 * Final Project!
 */

package javaFinalProject;

import java.util.*;
import java.util.concurrent.TimeUnit;

public class ICS3U_FP_FinalProjectCode_EddyZhang {

	public static void main(String[] args) {
		String userName = greeting();
		questions(userName);
		
	}
	/*
	 * Introduction of the game to the user (asks for name, city)
	 * Pre: void
	 * Post: prints introduction (like the actual game show)
	 */
	public static String greeting() {
		Scanner input = new Scanner (System.in);
		Random rand = new Random ();
		System.out.println("Welcome to Family Feud! Here, contestants try to guess the top answers that we asked in a survey! \nIf your answer is on the scoreboard, you win points!");
		System.out.print("Enter your name: ");
		String userName = input.next();
		userName = userName.substring(0, 1).toUpperCase() + userName.substring(1).toLowerCase();
		input.nextLine();
		System.out.print("Where are you from? (enter city name): ");
		String userCity = input.nextLine();
		userCity = userCity.substring(0, 1).toUpperCase() + userCity.substring(1).toLowerCase();
		String[] cityNames = {"Montreal","New York City" ,"Vancouver","San Francisco","Los Angeles","Chicago","Toronto","Miami","Portland","Boston"};
		String[] computerNames = {"Bob","Kevin","Lucas","David","Tim","Maria","Emma","Jennifer","Emily","Anne"};
		int randomNum1 = rand.nextInt(9);
		int randomNum2 = rand.nextInt(9);
		String computerName = computerNames[randomNum1];
		String computerCity = cityNames[randomNum2];
		System.out.println("I'm Steve Harvey and like always, we got another good one for you today.  \nFrom "+ userCity +", it's "+ userName+""
				+ "! \nAnd from "+ computerCity +", they’re playing against "+computerName+"! \nLet's start the game! After 5 rounds, whoever has the most points wins!");
		hold();
		hold();
		return userName;
	}
	/*
	 * shows the user the questions and checks the answers of the user
	 * Pre: userName
	 * Post: asks the user (and the computer) questions, shows them if they are right or wrong
	 */
	public static void questions(String userName) {
		Scanner input = new Scanner (System.in);
		Random rand = new Random ();
		int[] questionsIndex = {0,1,2,3,4};
		String[] questions = {"Name a country that speaks Spanish. (enter full name of country: UK = United Kingdom)","Name something you might eat or drink with a hamburger.","We asked 100 Americans: How much would you tip for good service?","Name a sport some mothers hope their child never plays.","In high income countries, which 5 programming languages are the most popular?"};
		String[] answers0 = {"Spain", "Mexico", "United States", "Cuba", "Argentina"};
		String[] answers1 = {"French Fries", "Soft Drink", "Soup", "Salad", "Onion Rings"};
		String[] answers2 = {"20%", "15%", "25%", "18%", "$20"};
		String[] answers3 = {"Hockey", "Football", "Baseball", "Soccer", "Rugby"};
		String[] answers4 = {"Java", "Python", "JavaScript", "C#", "HTML"};
		String[] answers[] = {answers0, answers1, answers2, answers3, answers4};
		int[] points = {25, 20, 15, 10, 5};
		for (int i=0; i<questionsIndex.length; i++) {
		    int randomPosition = rand.nextInt(questionsIndex.length);
		    int temp = questionsIndex[i];
		    questionsIndex[i] = questionsIndex[randomPosition];
		    questionsIndex[randomPosition] = temp;
		}
		int userPoints = 0;
		int computerPoints = 0;
		for (int counter = 0; counter < 5; counter += 1) {
			System.out.println("Question " + (counter+1) + ":");
			String[] ans = answers[questionsIndex[counter]];
			String userAnswer = "";
			String scoreboard = "";
			int whichRight = 0;
			int turn = rand.nextInt(2);
			int[] indexOfAns = new int [ans.length];
			scoreboard = answerBoard(userAnswer, ans, scoreboard, points, turn, whichRight, indexOfAns);
			int numOfAns = 0;
			int counter4 = 0;
			for (int counter2 = 0; counter2 < 6 && numOfAns < ans.length;) {
				while (turn == 1 && numOfAns < ans.length) {
					System.out.println("It is your turn!");
					hold();
					System.out.println(questions[questionsIndex[counter]]);
					System.out.print(scoreboard);
					System.out.print("Your answer: ");
					userAnswer = input.nextLine();
					boolean userCorrect = false;
					boolean ansAgain = false;
					for (int counter3 = 0; counter3 < answers[questionsIndex[counter]].length; counter3 += 1) {
						String elements = ans[counter3].toLowerCase();
						String userAnswer1 = userAnswer.toLowerCase();
						if (elements.equals(userAnswer1) == true) {
							userCorrect = true;
							for(int counter5 = 0; counter5 < indexOfAns.length; counter5 += 1) {
								if (indexOfAns[counter5]==(counter3+1)) {
									userCorrect = false;
									ansAgain = true;
								} 
							}
							if (ansAgain == false) {
								userPoints += points[counter3];
								indexOfAns[counter4] += (counter3+1);
								counter4 += 1;
							}
						}
					}
					System.out.println("Survey says...");
					hold();
					if (userCorrect == true) {
						System.out.println("You are correct! " + userAnswer + " is on the list! Now, you have " + userPoints + " points. ");
						scoreboard = answerBoard(userAnswer, ans, scoreboard, points, turn, whichRight, indexOfAns);
						numOfAns += 1;
					} else {
						if (ansAgain == true) {
							System.out.print("The answer was already guessed! ");
						} else {
							System.out.print("You are incorrect! ");
						}
						turn = 0;
						counter2 += 1;
						if (counter2 == 6) {
							turn = 2;
						}
					}
					hold();
				}
				while (turn == 0 && numOfAns < ans.length) {
					for (int counter7 = 0; counter7 < answers[questionsIndex[counter]].length; counter7 += 1) {
						userAnswer = " ";
						boolean ansAgain = false;
						int rightWrong = rand.nextInt(2);
						System.out.println("It is your opponent's turn!");
						hold();
						System.out.println(questions[questionsIndex[counter]]);
						System.out.print(scoreboard);
						System.out.println("Survey says...");
						hold();
						if (rightWrong == 1) {
							whichRight = rand.nextInt(ans.length);
							for (int counter6 = 0; counter6 < indexOfAns.length; counter6+=1) {
								if (indexOfAns[counter6] == (whichRight+1)) {
									ansAgain = true;
								}
							}
							if (ansAgain == true) {
								System.out.println("The answer was already guessed! ");
								turn = 1;
							} else {
								indexOfAns[counter4] += (whichRight+1);
								counter4 += 1;
								computerPoints += points[whichRight];
								System.out.println("The computer is correct! " + ans[whichRight] + " is on the list! Now, the computer has " + computerPoints + " points!");
								hold();
								scoreboard = answerBoard(userAnswer, ans, scoreboard, points, turn, whichRight, indexOfAns);
								numOfAns += 1;
								if (numOfAns == ans.length) {
									turn = 2;
								}
							}
						} else {
							System.out.println("The computer is incorrect! ");
							turn = 1;
						}
						if (turn == 1) {
							counter2 += 1;
							counter7 = answers[questionsIndex[counter]].length;
							if (counter2 == 6) {
								turn = 2;
							}
						}
					}
					hold();
				}
				if (turn == 2) {
					System.out.println("This round is over! Let's see the remaining answers.");
					hold();
					scoreboard = answerBoard(userAnswer, ans, scoreboard, points, turn, whichRight, indexOfAns);
					System.out.println(scoreboard);
					hold();
				}
			}
		}
		scores(userPoints, computerPoints, userName);
	}
	/*
	 * Timer for the code
	 * Pre: void
	 * Post: stops code from printing for 3 seconds
	 */
	public static void hold() {
		try {
			TimeUnit.SECONDS.sleep(3);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
	/*
	 * generates the scoreboard for the game, for user to see the answers on scoreboard
	 * Pre: userAnswer, scoreboard (from previous round), points (value of each answer), who's turn is it, computer's generated answer, the answers that have been said
	 * Post: an updated scoreboard for the game
	 */
	public static String answerBoard(String userAnswer, String[] ans, String scoreboard, int[] points, int turn, int whichRight, int[] indexOfAns) {
		if (userAnswer == "") {
			scoreboard = "";
			for (int counter = 1; counter <= ans.length; counter += 1) {
				scoreboard += counter + " - \n";
			}
		} else {
			if (turn == 1) {
				for (int counter2 = 0; counter2 < ans.length; counter2 += 1) {
					String elements = ans[counter2].toLowerCase();
					userAnswer = userAnswer.toLowerCase();
					if (elements.equals(userAnswer) == true) {
						scoreboard = scoreboard.replace((counter2+1) + " - ",(counter2+1) + " - " + ans[counter2] + " (" + points[counter2] + ")");
					}
				}
			} else if (turn == 0) {
				scoreboard = scoreboard.replace((whichRight+1) + " - ",(whichRight+1) + " - " + ans[whichRight] + " (" + points[whichRight] + ")");
			} else {
				for (int counter2 = 0; counter2 < ans.length; counter2 += 1) {
					boolean isItThere = false;
					for (int n : indexOfAns) {
				         if ((counter2+1) == n) {
				            isItThere = true;
				         }
				      }
					if (isItThere == false) {
						scoreboard = scoreboard.replace((counter2+1) + " - ",(counter2+1) + " - " + ans[counter2] + " (" + points[counter2] + ")");
					}
				}
			}
		}
		return scoreboard;
	}
	/*
	 * Conclusion of the game
	 * Pre: amount of points the user and computer has
	 * Post: determines who wins (based on how many points each person has)
	 */
	public static void scores (int userPoints, int computerPoints, String userName) {
		System.out.println("5 rounds are over! Now, let's see who won!");
		hold();
		if (userPoints > computerPoints) {
			System.out.println("With " + userPoints + " points, " + userName + " won!");
		} else if (userPoints == computerPoints) {
			System.out.println("With " + userPoints + " points, it is a tie!");
		} else {
			System.out.println("With " + computerPoints + " points, the computer won!");
		}
	}
}
