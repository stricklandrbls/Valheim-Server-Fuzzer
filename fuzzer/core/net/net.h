#include <iostream>
#include <ifaddrs.h>

auto getInterface(const std::string &iface)
{
  ifaddrs *interface = nullptr;
  if (getifaddrs(&interface) != -1)
  {
  }
}