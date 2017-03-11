#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int p1[] = {2,4,1,3,6,5};
int p2[] = {3,1,4,2,6,5};
int p3[] = {6,4,5,3,1,2};
int p4[] = {6,1,4,5,2,3};
int p5[] = {3,5,1,6,4,2};
int symmetric_encrypt(char message[],char secret_key[])
{
vector<char> msg,key,newmsg;
vector<char>::iterator it;
int i = 0;
msg.resize(6);
key.resize(6);
newmsg.resize(6);
copy ( message, message+6, msg.begin() );
copy ( secret_key, secret_key+6, key.begin() );

for (i=0,it=msg.begin(); it!=msg.end(); ++it,i++)
newmsg[p1[i]-1] = (*it) ^ key[i];
msg = newmsg;
for (i=0,it=msg.begin(); it!=msg.end(); ++it,i++)
newmsg[p2[i]-1] = (*it) ^ key[i];
msg = newmsg;
for (i=0,it=msg.begin(); it!=msg.end(); ++it,i++)
newmsg[p3[i]-1] = (*it) ^ key[i];
msg = newmsg;
for (i=0,it=msg.begin(); it!=msg.end(); ++it,i++)
newmsg[p4[i]-1] = (*it) ^ key[i];
msg = newmsg;
for (i=0,it=msg.begin(); it!=msg.end(); ++it,i++)
newmsg[p5[i]-1] = (*it) ^ key[i];
msg = newmsg;

for (it=msg.begin(); it!=msg.end(); ++it)
cout << " " << int(*it);

return 0;
}

int main()
{
char message[6];
char secret_key[7] = "secret";
cin >> message; 
symmetric_encrypt(message,secret_key);
return 0;
}
