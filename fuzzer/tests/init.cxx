#include <gtest/gtest.h>
#include <vsc.h>
TEST(INIT, CanUseLibrary)
{
  std::string hostname{"192.168.1.253"};
  unsigned short port{2456};

  TargetServer betelguese{{hostname, port}};

  ASSERT_EQ(betelguese.hostname(), hostname);
  ASSERT_EQ(betelguese.port(), port);
}