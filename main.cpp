#include "HashMap.h"
#include <string>

using namespace std;


int main()
{
    HashMap ht;
    int s = 0, b = 0 , d = 0;
    string word;
    read(ht,s,b,d);
    cout<<"Grammar Rules:"<<endl;
    ht.get('S',s);
    ht.get('B',b);
    ht.get('D',d);
    
    cout<<"Input a word to check:   ";
    cin>>word;
    if (ht.check(word,s,b,d)) cout << word << " is accepted";
    else cout << word << " is not accepted";

}
