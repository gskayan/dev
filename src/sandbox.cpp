#include<iostream>
#include<string>
#include<vector>
#include<utility>


using namespace std;


string testRvalue()
{
  
  string &&s = string("This ") + string(" is A ") + string("test!");

  cout << __LINE__ << " : " << s << endl;

  return forward<string&>(s);
  //return (s + " : Yep It is Rvalue");
};

struct A_Test
{
  void testRvalue( int&& x)
  {
    x += 8;
    cout << "As rval : " << x << endl;
  };

  void testRvalue( int& x)
  {
    x += 10;
    cout << "As lval : " << x << endl; 
  };
};

int main(int argc, char** argv)
{
  cout << testRvalue().append(" - Rvalue test") << endl;
  A_Test at;
  
  int i = 5;
  at.testRvalue(7);
  at.testRvalue(sizeof(A_Test));
  at.testRvalue(i);
  
  return 0;
}
