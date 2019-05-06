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
  A_Test(){};
  
  A_Test(const A_Test& other)
  {
    cout << "A_Test(const A_Test& other)" << endl;
  }

  A_Test(A_Test&& other)
  {
    cout << "A_Test(A_Test&& other)" << endl;
  }
  
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

A_Test&& new_A_Test()
{
  return forward<A_Test&&>(A_Test());
};

int main(int argc, char** argv)
{
  cout << testRvalue().append(" - Rvalue test") << endl;
  A_Test at;

  A_Test z(at);
  A_Test w(new_A_Test());
  
  int i = 5;
  at.testRvalue(7);
  at.testRvalue(sizeof(A_Test));
  at.testRvalue(i);
  
  return 0;
}
