#include "pch.h"
#include <iostream>
#include <algorithm>  
#include <vector>
#include <ctime>
#include <cstdlib>
#include <string>

using namespace std;

/*
Function which prints the menu available for the user
*/
void printMenu() {
	cout << "1. Give an encryption function (identity permutation by default)\n";
	cout << "2. Encrypt word\n";
	cout << "3. Decrypt word\n";
	cout << "0. Exit\n";
	cout << "Give a command: ";
}

/*
Function which prints the encryption function
*/
void printEncryptionFunction(vector<int> function) {
	cout << "  ";

	for (int i = 0; i < 26; i++)
		cout << (char)('a' + i) << ' ';

	cout << "\n";

	for (vector<int>::iterator it = function.begin(); it != function.end(); ++it)
		if (*it != 0)
			cout << (char)('@' + *it) << " ";
		else
			cout << "  ";
}

/*
Function which prints the decryption function
*/
void printDecryptionFunction(vector<int> function) {
	cout << "  ";

	for (int i = 0; i < 26; i++)
		cout << (char)('A' + i) << ' ';

	cout << "\n";

	for (vector<int>::iterator it = function.begin(); it != function.end(); ++it)
		if (*it != 0)
			cout << (char)('`' + *it) << " ";
		else
			cout << "  ";
}

/*
@param vector<int> encryptionFunction - a permutation which determines how the word is encrypted
@param string expression - the expression to be encrypted
return string - the encrypted expression according to the function
*/
string encryptExpression(vector<int> encryptionFunction, string expression) {
	string encrypted_expression = expression;
	for (unsigned int i = 0; i < expression.length(); i++)
	{
		if(expression[i] != ' ')
			encrypted_expression[i] = (char) '@' + encryptionFunction[expression[i] - '`'];
		else
			encrypted_expression[i] = (char) '@' + encryptionFunction[0];

		if (encrypted_expression[i] == '@')
			encrypted_expression[i] = ' ';
	}
	return encrypted_expression;

}

/*
@param vector<int> decryptionFunction - a permutation which determines how the word is decrypted
@param string expression - the expression to be decrypted
return string - the decrypted expression according to the function
*/
string decryptExpression(vector<int> decryptionFunction, string expression) {
	string decrypted_expression = expression;
	for (unsigned int i = 0; i < expression.length(); i++)
	{
		if (expression[i] != ' ')
			decrypted_expression[i] = (char) '`' + decryptionFunction[expression[i] - '@'];
		else
			decrypted_expression[i] = (char) '`' + decryptionFunction[0];
		if (decrypted_expression[i] == '`')
			decrypted_expression[i] = ' ';

	}
	return decrypted_expression;
}

/*
@param string expression - the expression to be checked
return bool - check if the expression contains only characters from the established alphabet
*/
bool isValidExpressionForEncryption(string expression) {
	for (char c : expression) {
		if (!((c-'a' >= 0 && c-'z' <= 0) || c == ' '))
			return false;
	}
	return true;
}

/*
@param string expression - the expression to be checked
return bool - check if the expression contains only characters from the established alphabet
*/
bool isValidExpressionForDecryption(string expression) {
	for (char c : expression) {
		if (!((c - 'A' >= 0 && c - 'Z' <= 0) || c == ' '))
			return false;
	}
	return true;
}

/*
@param string expression - the expression to be checked
return bool - check if the expression contains only unique characters
*/
bool containsDuplicates(string expression) {
	for (unsigned int i = 0; i < expression.length(); i++)
	{
		for (unsigned int j = i + 1; j < expression.length(); j++)
		{
			if (expression[i] == expression[j]) {
				return true;
			}
		}
	}
	return false;
}

/*
@param string expression - the expression used for creating the encryption function
@param vector<int> encryptionFunction - the identity permutation
return vector<int> - the encryption function constructed (as a permutation)
*/
vector<int> constructEncryptionFunction(string expression, vector<int> encryptionFunction) {
	int a = -1;
	int b = -1;
	for (unsigned int i = 0; i < expression.length(); i++)
	{
		if (expression[i] == ' ')
		{
			a = encryptionFunction[0];
			b = encryptionFunction[i];
			encryptionFunction[0] = b;
			encryptionFunction[i] = a;
		}
		else
		{
			a = encryptionFunction[expression[i] - '`'];
			b = encryptionFunction[i];
			encryptionFunction[expression[i] - '`'] = b;
			encryptionFunction[i] = a;
		}
	}

	return encryptionFunction;
}

/*
@param vector<int> encryptionFunction - the encyrption function in discussion
@param vector<int> decryptionFunction - the identity permutation where the result will be stored
return vector<int> - the decryption function constructed (as a permutation)
*/
vector<int> constructDecryptionFunction(vector<int> encryptionFunction, vector<int> decryptionFunction) {
	for (int i = 0; i < 27; i++)
		decryptionFunction[encryptionFunction[i]] = i;
	return decryptionFunction;
}

/*
Function which takes care of creating the encryption function option in the menu
*/
vector<int> giveEncryptionFunctionOption(vector<int> encryptionFunction) {
	string expression;
	cout << "\nGive me a valid expression (space, a-z): ";
	getline(cin, expression);
	if (!isValidExpressionForEncryption(expression) || containsDuplicates(expression))
		while (!isValidExpressionForEncryption(expression) || containsDuplicates(expression)) {
			if(!isValidExpressionForEncryption(expression))
				cout << "\nInvalid expression! Give me a valid expression (space, a-z): \n";
			if(containsDuplicates(expression))
				cout << "\nInvalid expression! It contains duplicates: \n";
			getline(cin, expression);
		}

	return constructEncryptionFunction(expression, encryptionFunction);
}

/*
Function which takes care of the encrypting option in the menu
*/
void encryptExpressionOption(vector<int> encryptionFunction) {

	string expression;
	cout << "\nGive me a valid expression (space, a-z): ";
	getline(cin, expression);
	if (!isValidExpressionForEncryption(expression))
		while (!isValidExpressionForEncryption(expression)) {
			cout << "\nInvalid expression! Give me a valid expression (space, a-z): ";
			getline(cin, expression);
		}
	cout << "\n" << encryptExpression(encryptionFunction, expression) << "\n";
}

/*
Function which takes care of the decrypting option in the menu
*/
void decryptExpressionOption(vector<int> decryptionFunction) {

	string expression;
	cout << "\nGive me a valid expression (space, A-Z): ";
	getline(cin, expression);
	if (!isValidExpressionForDecryption(expression))
		while (!isValidExpressionForDecryption(expression)) {
			cout << "\nInvalid expression! Give me a valid expression (space, A-Z): ";
			getline(cin, expression);
		}
	cout << "\n" << decryptExpression(decryptionFunction, expression) << "\n";
}

int main()
{
	vector<int> p;

	for (int i = 0; i < 27; i++)
		p.push_back(i);

	vector<int> encryption (p.begin(), p.end());
	vector<int> decryption (p.begin(), p.end());

	bool ok = true;
	while (ok) {
		printMenu();
		string command;
		getline(cin, command);
		if (command == "1") {
			encryption = p;
			decryption = p;
			encryption = giveEncryptionFunctionOption(encryption);
			decryption = constructDecryptionFunction(encryption, decryption);
			cout << "Encryption Function\n";
			printEncryptionFunction(encryption);
			cout << "\nDecryption Function\n";
			printDecryptionFunction(decryption);
			cout << "\n";
		}
		if (command == "2") 
			encryptExpressionOption(encryption);
		if (command == "3")
			decryptExpressionOption(decryption);
		if (command == "0")
			ok = false;
		if (command != "1" && command != "2" && command != "0" && command != "3")
			cout << "\nNo such option!\n";
	}
}