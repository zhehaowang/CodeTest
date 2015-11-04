/**
 * Quick test of timeout with two instances of different classes sharing a face
 */

#include <cstdlib>
#include <iostream>
#include <unistd.h>
#include <ndn-cpp/face.hpp>

using namespace std;
using namespace ndn;
using namespace ndn::func_lib;

class Counter1
{
public:
  Counter1(ndn::Face& face) : 
    face_(face)
  {

  }

  void onData(const ptr_lib::shared_ptr<const Interest>& interest, const ptr_lib::shared_ptr<Data>& data)
  {
    cout << "Got data packet with name " << data->getName().toUri() << endl;
    for (size_t i = 0; i < data->getContent().size(); ++i)
      cout << (*data->getContent())[i];
    cout << endl;
  }

  void onTimeout(const ptr_lib::shared_ptr<const Interest>& interest)
  {
    cout << "Instance1: Time out " << interest->getName().toUri() << endl;
  }

  void expressTimeoutInterest(int lifetime)
  {
    Name timeoutName = Name("/localhost/timeout");
    Interest timeoutInterest = Interest(timeoutName);
    timeoutInterest.setInterestLifetimeMilliseconds(lifetime);
    face_.expressInterest(timeoutInterest, bind(&Counter1::onData, this, _1, _2), bind(&Counter1::onTimeout, this, _1));
  }

  ndn::Face& face_;
};

class Counter2
{
public:
  Counter2(ndn::Face& face) : 
    face_(face)
  {

  }

  void onData(const ptr_lib::shared_ptr<const Interest>& interest, const ptr_lib::shared_ptr<Data>& data)
  {
    cout << "Got data packet with name " << data->getName().toUri() << endl;
    for (size_t i = 0; i < data->getContent().size(); ++i)
      cout << (*data->getContent())[i];
    cout << endl;
  }

  void onTimeout(const ptr_lib::shared_ptr<const Interest>& interest)
  {
    cout << "Instance2: Time out " << interest->getName().toUri() << endl;
  }

  void expressTimeoutInterest(int lifetime)
  {
    Name timeoutName = Name("/localhost/timeout");
    Interest timeoutInterest = Interest(timeoutName);
    timeoutInterest.setInterestLifetimeMilliseconds(lifetime);
    face_.expressInterest(timeoutInterest, bind(&Counter2::onData, this, _1, _2), bind(&Counter2::onTimeout, this, _1));
  }

  ndn::Face& face_;
};

int main(int argc, char** argv)
{
  try {
    // The default Face will connect using a Unix socket, or to "localhost".
    Face face;

    // Counter holds data used by the callbacks.
    Counter1 counter1 = Counter1(face);
    Counter2 counter2 = Counter2(face);

    counter1.expressTimeoutInterest(10000);
    counter2.expressTimeoutInterest(200);
    
    //Counter1 counter12 = Counter1(face);
    //counter12.expressTimeoutInterest(4000);

    // The main event loop.
    while (true) {
      face.processEvents();
      // We need to sleep for a few milliseconds so we don't use 100% of the CPU.
      usleep(100);
    }
  } catch (std::exception& e) {
    cout << "exception: " << e.what() << endl;
  }
  return 0;
}