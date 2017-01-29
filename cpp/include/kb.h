#ifndef INCLUDED_KB_H
#define INCLUDED_KB_H

#include <string>

class Kb
{
 public:
  struct Key
  {
    string d_key;
  };
  
  class Info
  {
  public:
    Info( const std::string& data );
    const 
    const string& data() const;
    virtual ~Info();
  private:
    string d_data;
  };
  
  Kb( const string name="KnowledgeBase");
  Kb& operator +( const Info& info);
  bool operator exists?( const Info& info);
  bool operator exists?( const Key& infoKey);
  Kb& operator -( const Key& infoKey );
  virtual ~K();
 private:
  const string& d_kbName;
  KbStore d_kbStore;
};

#endif
