#include "HashMap.h"
#include <string>

using namespace std;


int main()
{
    HashMap ht;
    int s = 0, a = 0, b = 0 , c = 0;
    string word;
    read(ht,s,d,r);
    cout<<"Grammar Rules:"<<endl;
    ht.get('S',s);
    ht.get('D',a);
    ht.get('R',b);
    ht.get('R',c);
    cout<<"Input a word to check:   ";
    cin>>word;
    if (ht.check(word,s,a,b,c)) cout << word << " is accepted";
    else cout << word << " is not accepted";

}
