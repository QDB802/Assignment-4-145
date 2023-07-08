/* CMPT 145 
 * Original Author: Lauresa Stilling
 * Date Created:	4 July 2023
 * Last Edited:	  	6 July 2023
 * All rights reserved.
 * This document contains resources for homework assigned to students of
 * CMPT 145 and shall not be distributed without permission. Posting this
 * file to a public or private website, or providing this file to a person
 * not registered in CMPT 145, constitutes Academic Misconduct, according
 * to the University of Saskatchewan Policy on Academic Misconduct.
 */

#include <stdio.h> 	// printf, scanf


void fizzbuzz(int n){
	int i;
	for (i=1; i<=n; i++){
		if (i%3==0 && i%5==0){
			printf("FizzBuzz\t");
		}
		else if (i%3 == 0){
			printf("Fizz\t");
		}
		else if (i%5 == 0){
			printf("Buzz\t");
		}
		else{
			printf("%d\t",i);
		}
	}
}

int main(){
	int input;
	printf("Enter a number: ");
	scanf("%d", &input); // How one gets input from the user.
	fizzbuzz(input);
}
