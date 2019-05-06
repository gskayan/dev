#include <iostream>
#include <future>
#include <chrono>
#include <thread>
#include <atomic>

class Kb
{
public:
  Kb(const std::string& );
  ~Kb();
private:
  std::string d_kbName;
};


Kb::Kb( const std::string& name)
  : d_kbName(name)
{};

Kb::~Kb()
{};


namespace gs
{
  const std::string loop_till_killed(int startWith, std::atomic_bool& keepRunning)
  {
    auto f = [](int i) -> void { static auto start=i; std::cout << "Running Lambda " << start++ << std::endl;};
    
    while(keepRunning)
      {
	f(startWith);
	std::this_thread::sleep_for(std::chrono::seconds(1));
      }
    return "Done looping";
  };
};


int main(int argc, char** argv)
{
  std::atomic_bool keepRunning(true);
  int startCount = 10;
  std::future<const std::string> fut = std::async( std::launch::async,
						   [](int i, std::atomic_bool& run) -> const std::string
						   {
						     return gs::loop_till_killed(i, run);
						   },
						   startCount,
						   std::ref(keepRunning)
						   );
  std::string input;
  while(true)
    {
      std::cout << "Continue? "; std::cin >> input;
      if( "no" == input )
	{
	  keepRunning = false;
	  std::cout << "Getting result : " << fut.get() << std::endl;
	  break;
	}
    }
  
  return 0;
}
  
