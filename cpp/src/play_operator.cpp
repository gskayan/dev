#include <iostream>
#include <string>

namespace
{
  unsigned long long operator""_word(unsigned long long  w)
  {
    return w * 1024ULL;
  };
};

int main()
{
  std::cout << 10_word << std::endl;
  return 0;
}
