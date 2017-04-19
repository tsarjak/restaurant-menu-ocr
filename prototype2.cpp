//it's going to be Legen...
#include<iostream>
#include<conio.h>
#include<fstream>
#include<cstring>
#include<ctype.h>
#include<string>
#include<algorithm>
using namespace std;

int counter=0, cnt=0, cnt2=0;

struct wordTree{
	string data;
	struct wordTree *i[11] = {NULL};
};



int minimum(int a, int b, int c){
		int temp=a;
		if(temp>b){
			temp = b;
		}
		if(temp>c){
			temp = c;
		}
		
		return temp;
}


int levenDis(string a1, string a2){
	
	
	int n1 = a1.size();
	int n2 = a2.size();
	
	
	int i,j;
	
	int checkArray[20][20];
	
	for(i=0;i<=n1;i++)
		checkArray[i][0]=i; 
		
	for(i=0;i<=n2;i++)
		checkArray[0][i]=i;
		
	
	for(i=1;i<=n1;i++){
		for(j=1;j<=n2;j++){
			if(a1[i-1]==a2[j-1]){
			checkArray[i][j]=minimum(checkArray[i-1][j],checkArray[i][j-1],checkArray[i-1][j-1]);
			}
			else{
			checkArray[i][j]=(minimum(checkArray[i-1][j],checkArray[i][j-1],checkArray[i-1][j-1])+1);	
			}
			
		}
	
	}	
	
	return checkArray[n1][n2];
}

void addRoot(string word, wordTree *root){
	root->data = word;
}

void addTree(string word, string rootWord, wordTree *node){
	int dist;
	wordTree *temp = new wordTree;
	dist = levenDis(word,rootWord);
	
	if(node->i[dist]==NULL){
			wordTree *nWord = new wordTree;
			node->i[dist]=nWord;
			nWord->data=word;
			}
		else{
			temp=node->i[dist];
			addTree(word, temp->data, temp);		
			}
	
}

void spellCorrector(string word, string rootWord, wordTree *node){
	int dist;
	dist = levenDis(word,rootWord);
	if(dist==0){
		cnt++;
		if(cnt==1){
			cnt2++;
			if(cnt2==1){
			}
		}
		cout<<rootWord<<"\t";
		}
	
	else if(dist==1){
		wordTree *temp = new wordTree;
		wordTree *temp2 = new wordTree;
		cnt++;
		if(cnt==1){
			cnt2++;
			if(cnt2==1){
			
			}

		}
		cout<<rootWord<<"\t";
		
		if(node->i[1]!=NULL && node->i[2]!=NULL){
			temp = node->i[1];
			temp2 = node->i[2];
			spellCorrector(word, temp->data, temp);
			counter++;
			spellCorrector(word, temp2->data, temp2);
			counter++;	
		}
		
		else if(node->i[1]!=NULL && node->i[2]==NULL){
			temp = node->i[1];
			spellCorrector(word, temp->data, temp);
			counter++;
			}
		
		else if(node->i[1]==NULL && node->i[2]!=NULL){
			temp2 = node->i[2];
			spellCorrector(word, temp2->data, temp2);	
			counter++;
		}
	}
	
	else{
		wordTree *temp1 = new wordTree;
		wordTree *temp2 = new wordTree;
		wordTree *temp3 = new wordTree;
		
		if(node->i[dist-1]!=NULL && node->i[dist]!=NULL && node->i[dist+1]!=NULL){			//None of them is NULL
			temp1=node->i[dist-1];
			temp2=node->i[dist];
			temp3=node->i[dist+1];
			spellCorrector(word, temp1->data, temp1);
			counter++;
			spellCorrector(word, temp2->data, temp2);
			counter++;
			spellCorrector(word, temp3->data, temp3);
			counter++;
		}
		
		else if(node->i[dist-1]!=NULL && node->i[dist]!=NULL && node->i[dist+1]==NULL){		//Only dist+1 is NULL
			temp1=node->i[dist-1];
			temp2=node->i[dist];
			spellCorrector(word, temp1->data, temp1);
			counter++;
			spellCorrector(word, temp2->data, temp2);
			counter++;
		}
		
		else if(node->i[dist-1]!=NULL && node->i[dist]==NULL && node->i[dist+1]!=NULL){		//Only dist is NULL
			temp1=node->i[dist-1];
			temp3=node->i[dist+1];
			spellCorrector(word, temp1->data, temp1);
			counter++;
			spellCorrector(word, temp3->data, temp3);
			counter++;
		}
		
		else if(node->i[dist-1]==NULL && node->i[dist]!=NULL && node->i[dist+1]!=NULL){		//Only dist-1 is NULL
			temp2=node->i[dist];
			temp3=node->i[dist+1];//...WaitForIt....
			spellCorrector(word, temp2->data, temp2);
			counter++;
			spellCorrector(word, temp3->data, temp3);
			counter++;
		}
		
		else if(node->i[dist-1]!=NULL && node->i[dist]==NULL && node->i[dist+1]==NULL){		//Only dist-1 is NOT NULL
			temp1=node->i[dist-1];
			spellCorrector(word, temp1->data, temp1);
			counter++;
		}
		
		else if(node->i[dist-1]==NULL && node->i[dist]!=NULL && node->i[dist+1]==NULL){		//Only dist is NOT NULL
			temp2=node->i[dist];
			spellCorrector(word, temp2->data, temp2);
			counter++;
		}
		
		else if(node->i[dist-1]==NULL && node->i[dist]==NULL && node->i[dist+1]!=NULL){		//Only dist+1 is NOT NULL
			temp3=node->i[dist+1];
			spellCorrector(word, temp3->data, temp3);
			counter++;
		}
	}
	
}

int countVar=0;

void searchWord(string word, string rootWord, wordTree *node){
	int dist;
	wordTree *temp = new wordTree;
	dist = levenDis(word,rootWord);
	
	if(dist==0){
		countVar++;
	}
	else{
		if(node->i[dist]!=NULL){
			temp = node->i[dist];
			searchWord(word, temp->data, temp);
		}
		else{
		
		}
	}
}

void sentenceCorrection(string sen, wordTree *node){
		int i=0;
		transform(sen.begin(), sen.end(), sen.begin(),::toupper);
		int checker;
		string wrod;
		for(i=0;i<sen.length();i++){
			if(sen[i]!=' ' && sen[i]!='.' && sen[i]!=',' && sen[i]!='?' && sen[i]!='!'){
				wrod+=sen[i];
			}
			else{
		
			    searchWord(wrod, "AA", node);
			    if(countVar==0){
			    	if(wrod.length()!=0){
			   		cout<<endl<<wrod<<"\t\t---\t";
			    	spellCorrector(wrod,"AA",node);
			    }
				}
				else{
					cout<<endl<<wrod;
				}
				countVar=0;
			    wrod.clear();
			   }
		}
    	
			}


void display(wordTree *root){
	wordTree *temp = new wordTree;
	temp = root;
	while(temp->i[5]!=NULL){
		cout<<temp->data<<endl;
		temp = temp->i[5];
	}
	cout<<temp->data<<endl;
}

int main(){
	
	wordTree *root = new wordTree;	
	addRoot("AA", root);

	char ch='y';
	int opt;

	string addWord;
	
	ifstream myfile ("TwoLetterWords.txt");
	  if (myfile.is_open()){
    	while ( getline (myfile,addWord)){
      	addTree(addWord, root->data, root);
    	}
    	myfile.close();
  	}

  		else cout << "Unable to open file"; 
  		
	string wrd;
	string sen;
	
	while(ch=='y' || ch=='Y'){
		cout<<"Select one option :\n1. Check if word exists in the dictionary";
		cout<<"\n2. Correct a Word\n3. Correct a sentence\n4. Exit\n\nYour Choice : ";
		cin>>opt;
		
		switch (opt){
			
			
			case 1 :
				cout<<"\nEnter the Word you want to search : ";
				cin>>wrd;
				transform(wrd.begin(), wrd.end(), wrd.begin(),::toupper);
				countVar=0;
				searchWord(wrd,"AA",root);
					if(countVar!=0)
						cout<<endl<<"The word exists in the dictionary!"<<endl;
					else
						cout<<endl<<"The word doesn't exist in the dictionary. Try our spell corrector!"<<endl;
				break;
				
				
			case 2 : 
				cout<<"\nEnter the Word you want to correct : ";
				cin>>wrd;
				transform(wrd.begin(), wrd.end(), wrd.begin(),::toupper);
				countVar=0;
				searchWord(wrd,"AA",root);
				if(countVar==0){
				cout<<"The suggestions are : \n\n";
					spellCorrector(wrd,"AA",root);
				}
				else
					cout<<"Come on bro. That already is a correct word!";
					
				if(cnt==0){
						cout<<endl<<"No Suggestions found!";
					}
				break;
				
				
			case 3 : 			
				fflush(stdin);
				cout<<"Enter the sentence (Use a full stop before terminating the sentence) : ";
				fflush(stdin);
				getline(cin,sen);
				sentenceCorrection(sen, root);
				break;
				
				
			case 4 : 
				exit(0);
				
			default : 
				cout<<"Enter a Valid option!";
				
		}	
		cout<<"\n\n";	
	}
	
	getch();
	return 0;
}
//...Dary...
