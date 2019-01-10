#include <iostream>
using namespace std;

string lunarAddition(string x, string y){
	
	//Determining which length is greater and if necessary making it the same
	if(x.length() != y.length()){
		
		string longer, shorter;
		if(x.length() > y.length()){
			longer = x;
			shorter = y;
		}else{
			longer = y;
			shorter = x;
		}
		
		
		for(int i = 0; i < longer.length(); i++){
			longer[i] = '0';
		}
		
		for(int i = longer.length()-shorter.length(); i < longer.length(); i++){
			longer[i] = shorter[i-(longer.length()-shorter.length())];
		}
		
		if(x.length() > y.length()) y = longer;
		else x = longer;
	}
	
	//Adding using lunar arithmetics
	string number;
	for(int i = 0; i < x.length(); i++){
		if((int)x[i] > (int)y[i]){
			number += x[i];
		}else{
			number += y[i];
		}
	}
	
	return number;
}

string lunarMultiplication(string x, string y){
	
	string number[2];
	for(int i = 0; i < x.length(); i++){
		for(int ii = 0; ii < y.length(); ii++){
			if((int)x[i] < (int)y[ii]){
				number[i] += x[i];
			}else{
				number[i] += y[ii];
			}
		}
	}
	
	//Adding zeros to the end of the strings respectfully
	number[1] += '0';
	
	return lunarAddition(number[0],number[1]);
}

int main(){
	cout << lunarAddition("22221","333") << endl;
	cout << lunarMultiplication("12","23") << endl;
}
